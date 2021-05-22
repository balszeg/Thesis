# Traffic Image Detection With Deep Learning  
  
<p align="center">
  <img src="Traffic.gif" alt="animated" />
</p>
  
This repository was made for the above named thesis.  
Deep neural networks were trained for classifying and object detecting.  
    
The used datasets were:  
-[OID](https://storage.googleapis.com/openimages/web/index.html)  
-[KITTI](http://www.cvlibs.net/datasets/kitti/)  
-[BDD100K](https://www.bdd100k.com/)  
All of them are freely available to anyone.  
  
The used models were:  
-VGG16 (from [Keras Application](https://keras.io/api/applications/))  
-[YOLOv4](https://arxiv.org/abs/2004.10934)  
-[Faster R-CNN](https://arxiv.org/abs/1506.01497)  
  
For optimizing purpose [TenrosRT](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html) was used on an Nvidia Jetson Nano 2Gb.  
  
The repository contains the followings:  
-all the trained model's codes as .ipynb, these can be executed in Google Colab  
-all the trained and optimized weights  
-all the support scripts and codes  
  
With these every training can be reproduced  
Important to note, when the codes refer to uploading/copying from the user's Google Drive, then the instructions are meant the above listed ones.
