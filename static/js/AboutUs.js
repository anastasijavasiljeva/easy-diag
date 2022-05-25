import React from "react";

function AboutUs(){
    return (
        <div className="abt-info">
            <h1>What's that?</h1>
            <div>This is prototype done for my bachelor thesis work. The purpose is to help doctors diagnose forearm fractures by providing helpful (or not really helpful) insights. The insights are provided using VGG-16 architecture network and GradCam algorithm. </div>
            <h1>How does it work?</h1>
            <div>The simplest way possible! Just upload the picture and press 'Upload'. You'll get a processed picture and some more information. The analysis results are presented in this way: </div>
            <ol>
                <li>If a fracture is detected, you get 'Fracture detected', else you get 'No fracture detected'. Pretty simple, right?</li>
                <li>Next goes probability. This is basically AI confidence probability. Please keep in mind that <b>this is purely experimental prototype and the results may be incorrect and totally gibberish.</b></li>
                <li>And finally processed image. This is basically image colored based on AI outputs. If the fracture was detected, yellowish colors mark the places where the fracture is most likely to occur and blueish colors mark the places where it is least likely.</li>
            </ol>
            <h1>References</h1>
            <ol>
                <li>P. Rajpurkar et al., ‘MURA: Large Dataset for Abnormality Detection in Musculoskeletal Radiographs’, arXiv, arXiv:1712.06957, May 2018. doi: 10.48550/arXiv.1712.06957.</li>
                <li>K. Simonyan and A. Zisserman, ‘Very Deep Convolutional Networks for Large-Scale Image Recognition’. arXiv, Apr. 10, 2015. Accessed: May 22, 2022. [Online]. Available: <a href="http://arxiv.org/abs/1409.1556">http://arxiv.org/abs/1409.1556</a></li>
                <li>R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and D. Batra, ‘Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization’, Int J Comput Vis, vol. 128, no. 2, pp. 336–359, Feb. 2020, doi: 10.1007/s11263-019-01228-7.</li>
            </ol>
        </div>
    )
}

export default AboutUs;
