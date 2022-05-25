import axios from "axios";
import React, { useState } from "react";
import { Row } from 'react-bootstrap';
import Dropzone from "react-dropzone";

function MainForm(){
    const [selectedFiles, setSelectedFiles] = useState(undefined);
    const [tempResult, setTempResult] = useState(undefined);
    const [probability, setProbability] = useState(0);
    const [isFracture, setFracture] = useState(false);
    const [isLoading, setLoading] = useState(false);
    
    function onDrop(files) {
        if (files.length > 0) setSelectedFiles(files);
    }

    function downloadBase64File(contentType, base64Data, fileName) {
      const linkSource = `data:${contentType};base64,${base64Data}`;
      const downloadLink = document.createElement("a");
      downloadLink.href = linkSource;
      downloadLink.download = fileName;
      downloadLink.click();
    }

    function handleUpload(){
      let formData = new FormData();
      formData.append("file", selectedFiles[0]);
      axios.post('/upload', formData, {headers: {
        "Content-Type": "multipart/form-data"
        , "responseType": "arraybuffer"
      }}).then((response) => { 
        console.log(response);
        setTempResult(response.data.image);
        let tempPos = parseFloat(response.data.positive);
        let tempNeg = parseFloat(response.data.negative);
        setProbability(tempPos > tempNeg ? tempPos : tempNeg);
        setFracture(tempPos > tempNeg? true : false);
      }).catch(() => { setSelectedFiles(undefined) });
    setSelectedFiles(undefined);
    }

    if (tempResult === undefined) return (
        <div>
          <div>Upload a fracture image and start diagnosing! </div>
          <div>You can read more about EasyDiag and its purpose <a href="/about-us">here</a></div>
          <Dropzone onDrop={onDrop} multiple={false} accept={{'image/*': ['.jpg', '.png']}}>
            {({ getRootProps, getInputProps }) => (
              <section>
                <div {...getRootProps({ className: "dropzone" })}>
                  <input {...getInputProps()} />
                  {selectedFiles && selectedFiles[0].name ? (
                    <div className="selected-file">
                      <Row><img src={URL.createObjectURL(selectedFiles[0])} alt='' className="imgPreview"/></Row>
                      <Row>{selectedFiles && selectedFiles[0].name}</Row>
                    </div>
                  ) : (
                    "Drag and drop file here, or click to select file"
                  )}
                </div>
                <aside className="selected-file-wrapper">
                  <Row>
                  <button className="btn btn-success" disabled={!selectedFiles} onClick={handleUpload}>Upload</button>
                  <button className="btn btn-secondary" disabled={!selectedFiles} onClick={() => setSelectedFiles(undefined)}>Clear</button>
                  </Row>

                </aside>
              </section>
            )}

          </Dropzone>
        </div>
      )
      else return (<>
        <h2>{isFracture ? `Fracture detected` : `No fracture detected`} (probability {probability}%)</h2>
        <div className="wrapperRes">
          <Row><img className='resultImg' src={`data:image/png;base64,${tempResult}`} alt='Fracture analysis result'/></Row>
          
        </div>
        <div className="txt">Colors to the right mark greater probability:   
          </div><div className="pallette"></div>
        <Row className='resultBtns'>
          <button className="btn btn-success" onClick={() => downloadBase64File('image/png', tempResult, "easydiag_res.png")}>Download</button>
          <button className="btn btn-secondary" onClick={() => setTempResult(undefined)}>Back</button>
        </Row>
            </>
            );
}

export default MainForm;