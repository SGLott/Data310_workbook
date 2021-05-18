# Final Project: Image Classification of Ground Penetrating Radar Profiles

### Abstract
Ground penetrating radar (GPR) is a tool used to determine changes in sediment properties, such as mineralogy, grain size, and water content, under the surface of the earth by sending radar waves underground and measuring their time to return. The resultant GPR profiles (Figure 1) show a picture of the structure of sediment under the earth’s surface. The orientation of features within a radargram can give us information about how land formed through time. Typically, to analyze a GPR profile, someone would individually trace every reflection within a profile. This can lead to human error as certain features might not be noticed by the human eye, or importance of a feature may be over or under valued by the interpreter. A first step in reducing error is to see if a model can identify and classify features within a GPR transect. Seven GPR profiles totaling 5 km were broken into 740 50x50 pixel tiles. The tiles were then split into a training and testing dataset and classified based on feature presence and dip direction. The three classes were no feature/no dip direction, feature dipping left, and feature dipping right. Using a convolutional neural network (CNN), the model was fit with the training data and tested with the testing data. Model accuracy was low (21.6%), but increasing robustness of the dataset and increasing number of classes have the potential to increase accuracy in the future. 

![image](https://user-images.githubusercontent.com/78218309/116883931-266d4f80-abf4-11eb-85da-b2d2080abfda.png)
#### Figure 1. 
A) Processed and B) interpreted GPR profile from east-central part of study area (Notated in Figure 1 as Figure 11). 
Notice three different sequences of obliquely dipping reflectors. In interpreted profile, different dips and directions indicate different environments of deposition.

### Presentation Recording
[Final Presentation Video on YouTube](https://youtu.be/bncq5uhIf7M)

### Presentation Slides
[Download Presentation slides used in Recording](https://sglott.github.io/Data310_workbook/Presentation1.pptx)
