# Project proposal (Neural networks - FIIT - 2019/2020)

## Motivation
The key goal of this project, is to create ALPR (automatic license plate recognition) program, that will be able to run on a small computer such as NVIDIA Jetson Nano. Motivation behind this, is that we want to have a camera connected to this device, which will be set up in a car and automatically send license plate of cars in front, to an API of HAKA application. 

HAKA is a simple mobile app, in which user can enter a license plate number of any car and in few seconds, it shows the user basic information about that car. This is supposed to help people reveal a stolen car. 

When this whole project is finished, people will be able to detect a stolen car during driving, without having to manually enter their license plate into this application, because this will be all automatic. All they will need, will be a small, portable NVIDIA Jetson Nano computer and a camera placed inside a car. 

## Related work
There are many ALPR projects on either GitHub or throughout the internet, that we can make use of. For example in this article [https://towardsdatascience.com/automatic-license-plate-detection-recognition-using-deep-learning-624def07eaaf](https://towardsdatascience.com/automatic-license-plate-detection-recognition-using-deep-learning-624def07eaaf) they use YOLO (You Only Look Once) architecture. They also mentioned creating dataset of 700 images, that was labeled using application called LabelImg. After that they used Darknet project, which is used to retrain YOLO pretrained models.

There is also an OpenALPR website, which provides a complete solution also with documentation, from which we can definitely take an inspiration [https://www.openalpr.com/](https://www.openalpr.com/).

It is important to mention, that most of ALPR projects and solutions use neural networks for identifing a license plate in an image or video and then use OCR for text recognition. 

We can also make big use of some demo projects on NVIDIA website, which will guide us, how to make our solution suitable for NVIDIA Jetson Nano board. [https://developer.nvidia.com/embedded/community/jetson-projects](https://developer.nvidia.com/embedded/community/jetson-projects). For example this project [https://github.com/dusty-nv/jetson-inference](https://github.com/dusty-nv/jetson-inference) is also prepared to be used with live cameras.
## Datasets
At first, we will try to use some ALPR datasets available on the internet and later, if it does not perform well, we will create our own dataset with labeled images of cars and their license plates. 

There are many datasets available on the internet, but at the moment it is not clear, whether we will need images of slovak license plates, or the model will still perform well, when trained with dataset of foreign countries cars images.
## High level solution proposal
Our solution will be a desktop application that need to run on Ubuntu system (default OS of NVIDIA Jetson Nano). This application will consist of 3 components. First component will be our neural network that will be doing the object recognition part. It will take a real time video from camera as an input and its output will be the part of the image, where the license plate is located. This image will be then processed by our second component that will do the OCR part. It will return the license plate as a string that will be passed to the third component, which will be the "connector" to HAKA API. Response from this API will be then displayed on display connected to the board, so that the user can see the basic information about the car and whether it was stolen or not.

We will try our best, but since HAKA API is not public at the moment, we can not surely say if this part will be successfully fulfilled. If not, the project will be considered done as soon as it will be able to show the license plate string as an output to the user. 
