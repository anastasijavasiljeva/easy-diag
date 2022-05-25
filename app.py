from keras.models import Model, load_model
import numpy as np
import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
from PIL import Image
from io import BytesIO 
from flask import request, Flask, make_response, jsonify, render_template
from flask_cors import CORS
import base64
from keras.applications.imagenet_utils import preprocess_input
from math import ceil
from dotenv import load_dotenv
from flask_compress import Compress
from flask_static_compress import FlaskStaticCompress
from flask_squeeze import Squeeze

class GradCAM:
    def __init__(self, model, classIdx, layerName=None):
        self.model = model
        self.classIdx = classIdx
        self.layerName = layerName
        if self.layerName is None:
            self.layerName = self.find_target_layer()

    def find_target_layer(self):
        for layer in reversed(self.model.layers):
            if len(layer.output_shape) == 4:
                return layer.name
        raise ValueError("Could not find 4D layer. Cannot apply GradCAM.")

    def compute_heatmap(self, image, eps=1e-8):
        gradModel = Model(inputs=[self.model.inputs], outputs=[self.model.get_layer(self.layerName).output, self.model.output])
        with tf.GradientTape() as tape:
            inputs = tf.cast(image, tf.float32)
            (convOutputs, predictions) = gradModel(inputs)
            loss = predictions[:, self.classIdx]
        grads = tape.gradient(loss, convOutputs)
        castConvOutputs = tf.cast(convOutputs > 0, "float32")
        castGrads = tf.cast(grads > 0, "float32")
        guidedGrads = castConvOutputs * castGrads * grads
        convOutputs = convOutputs[0]
        guidedGrads = guidedGrads[0]
        weights = tf.reduce_mean(guidedGrads, axis=(0, 1))
        cam = tf.reduce_sum(tf.multiply(weights, convOutputs), axis=-1)
        (w, h) = (image.shape[2], image.shape[1])
        heatmap = cv2.resize(cam.numpy(), (w, h))
        numer = heatmap - np.min(heatmap)
        denom = (heatmap.max() - heatmap.min()) + eps
        heatmap = numer / denom
        heatmap = (heatmap * 255).astype("uint8")
        return heatmap

    def overlay_heatmap(self, heatmap, image, alpha=0.5, colormap=cv2.COLORMAP_VIRIDIS):
        heatmap = cv2.applyColorMap(heatmap, colormap)
        output = cv2.addWeighted(image, alpha, heatmap, 1 - alpha, 0)
        return (heatmap, output)

def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    image = image.convert('RGB')
    np_array = np.array(image.getdata())
    reshaped = np_array.reshape((im_height, im_width, 3))
    return reshaped.astype(np.uint8)

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG', quality=90)
    img_io.seek(0)
    img_base64 = base64.b64encode(img_io.read()).decode('ascii')
    return str(img_base64)


compress = Compress()
squeeze = Squeeze()

def start_app():
    app = Flask(__name__)
    CORS(app)
    compress.init_app(app)
    stat_compress = FlaskStaticCompress(app)
    stat_compress.init_app(app)
    squeeze.init_app(app)
    return app
    
load_dotenv()
app = start_app()
model = load_model(os.environ.get('MODEL_PATH'))

@app.route("/")
def mainpage():
    return render_template("index.html")

@app.route("/about-us")
def abtus():
    return render_template("index.html")

@app.route("/upload", methods = ['GET', 'POST'])
def upload():    
    if 'file' not in request.files:
        return make_response(406, 'No file was found')
    file = request.files['file']
    width, height = Image.open(file).size
    img = Image.open(file).resize((int(os.environ.get('IMG_WIDTH')), int(os.environ.get('IMG_HEIGHT'))), 0)
    img = load_image_into_numpy_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    fact_resp= model.predict(img)
    print (fact_resp)
    cam = GradCAM(model, np.argmax(fact_resp[0]))
    heatmap = cam.compute_heatmap(img)
    heatmap = cv2.resize(heatmap, (width, height))
    (heatmap, output) = cam.overlay_heatmap(heatmap, load_image_into_numpy_array(Image.open(file)), alpha=0.7)
    construct_response = jsonify({"result": str(np.argmax(fact_resp[0])), "negative": str(ceil(fact_resp[0][1] * 100)), "positive": str(ceil(fact_resp[0][0] * 100)), "image": serve_pil_image(Image.fromarray(output))})
    return construct_response

if __name__ == "__main__":
    context = ('selfsigned.crt', 'private.key')
    app.run(ssl_context=context)#('cert.pem', 'key.pem'))#run()