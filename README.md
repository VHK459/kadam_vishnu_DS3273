## Problem Description
Traffic sign classification is a critical task in autonomous driving systems and intelligent transportation systems. The objective of this project is to develop a Convolutional Neural Network (CNN) model that can classify images of traffic signs into one of 58 categories. Each category corresponds to a specific type of traffic sign, such as speed limits, stop signs, and warning signs. The dataset contains around 58 classes, with each class having approximately 120 images. The dataset also includes a **labels.csv** file, which provides descriptions of each class. This project will utilize CNN architecture to classify traffic sign images with a reasonable degree of accuracy.

## Input-Output
1. Input: Images of traffic signs in various formats (**.jpg**, **.png**), where each image corresponds to one of the 58 traffic sign classes.
2. **Output**: A classification label representing the type of traffic sign. The output will be a class ID, which can be mapped to a descriptive label using the provided **labels.csv** file.

## Data Source
The dataset used in this project consists of traffic sign images collected from a variety of sources, including public datasets and real-world images. The dataset is structured into 58 classes, with each class having approximately 120 images, totaling around 6960 images. Additionally, the dataset includes around 2000 test images for evaluating the model’s performance. A **labels.csv** file accompanies the dataset, containing the respective descriptions of the traffic sign classes, which can be mapped to the class IDs during model evaluation.

## Model Architecture
For this classification task, I will use a basic Convolutional Neural Network (CNN) model due to its effectiveness in image classification tasks. The CNN model will consist of several convolutional layers, followed by pooling layers to reduce dimensionality, and fully connected layers to make final predictions. A softmax activation function will be used in the output layer to classify images into one of the 58 classes.

## Downloading dataset
The dataset was downloaded from kaggle. [Download page ](https://www.kaggle.com/datasets/ahemateja19bec1025/traffic-sign-dataset-classification)
