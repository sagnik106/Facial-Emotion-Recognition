# Facial-Emotion-Recognition
Ever felt no one understands your emotions? Here's a Computer Vision project that does.</br>
This project repurposes SOTA ResNet-152 Architecture trained on ImageNet and fine tuned on human emotion dataset to detect human emotions.

## Requirements/Libraries:
* Python 3.8.2
* Tensorflow 2.2
* Keras 2.2.4
* Numpy 1.15.4
* Matplotlib 3.0.2
* OpenCV 4.2.0
* Pandas 1.0.3

## Dataset:
The dataset is taken from kaggle - [FER(Facial Emotion Recognition) Challenge](https://www.kaggle.com/ashishpatel26/facial-expression-recognitionferchallenge)

## Model Performance:
Accuracy</br>
![Neural Network Accuracy](https://github.com/sagnik106/Facial-Emotion-Recognition/blob/master/resources/Accuracy.png)</br>
Loss</br>
![Neural Network Loss](https://github.com/sagnik106/Facial-Emotion-Recognition/blob/master/resources/Loss.png)

## File Architecture
* [Model.ipynb](https://github.com/sagnik106/Facial-Emotion-Recognition/blob/master/Model.ipynb) - A jupyter notebook to train and test the model
* [reader.py](https://github.com/sagnik106/Facial-Emotion-Recognition/blob/master/reader.py) - Classifies the emotion of the face detected in the camera