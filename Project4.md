# Project 4

## Problem Statement:
Ground penetrating radar (GPR) is a tool used to determine changes in sediment properties, such as mineralogy, grain size, and water content, under the surface of the earth by sending radar waves underground and measuring their time to return. The resultant GPR profiles (Figure 1) show a picture of the structure of sediment under the earth’s surface. The orientation of features within a radargram can give us information about how land formed through time.

Typically, to analyze a GPR profile, someone would individually trace every reflection within a profile. This can lead to human error as certain features might not be noticed by the human eye, or importance of a feature may be over or under valued by the interpreter. In order to reduce human error, I would like to implement a convolutional neural network to try and identify the prominent features within a GPR profile. The goal would be for the model to identify the most prominent reflectors, what I identify as lines in the the idealized lines in Figure 1. To do this, I am creating a density plot and using the model to identify the most dense areas in the plot. 


## Description of Data:
Previous research has applied CNNs to GPR profiles in a lab setting where GPR transects are run along a constructed topography (Park et al., 2019). These studies have found that CNNs are able to identify prominent features, such as a change in material within the topography. The study that I will be basing my model on, used a constructed surface of concrete and metal bars. Metal appears in GPR as a parabola because of the refraction of radar waves around the feature. The study found that a trained CNN was able to identify parabolas within the radargram. 

My data will be a single GPR profile that was taken over top of relatively homogenous sediment along the coast of southern Brazil (Figure 2). The GPR profile has been post-processed using DC removal, time-zero adjustment, background removal, two-dimensional spatial filtering, amplitude correlation, predictive deconvolution, bandpass filtering, and Stolt F-K migration. I have analyzed this GPR profile to identify the features that I thought were important in interpreting land formation. Typically, the key features are linear and represent different points of beach as it grew over time. The radargram I selected for analysis is over 1 km long and 8m deep. The profile was vertically exaggerated to enhance the prominence of features within the profile. This should also increase model accuracy. Another way I plan on increasing model accuracy, is to split the radargram into smaller square images, similar to the image size of the training dataset. 

![image](https://user-images.githubusercontent.com/78218309/116883931-266d4f80-abf4-11eb-85da-b2d2080abfda.png)
#### Figure 1. 
A) Processed and B) interpreted GPR profile from east-central part of study area (Notated in Figure 1 as Figure 11). 
Notice three different sequences of obliquely dipping reflectors. In interpreted profile, different dips and directions indicate different environments of deposition.


![image](https://user-images.githubusercontent.com/78218309/116883625-cf677a80-abf3-11eb-8442-e2870f25179c.png)
#### Figure 2.
Study site: São Francisco do Sul Island, located at the southern entrance and margin of Babitonga Bay, Santa Catarina, Brazil. A) Overview map of the study area. B) Digital elevation 
model of the northeast study site showing 45 ground-penetrating radar (GPR) profile locations (Selected GPR profile noted as figures 11 and 7 will be used for this analysis), four optically 
stimulated luminescence (OSL) sample locations, and 17 hand auger sampling locations. C) Enlarged image of the Ubatuba. Figure taken from my senior thesis. Elevation data from SIGSC.

## Applied Machine Learning Method:
To train their model, the study used a gray-scale version of the CiFar10 database which includes images that are 32x32 pixels. Ground penetrating radar can either be displayed in red-blue couples, or in grayscale. In order to increase model accuracy, the CiFar10 data converted to grayscale and the GPR data used was displayed in grayscale. 

I plan on using the same model structure as the study because they were able to identify features in their simulated GPR profile. Their CNN included “3 convolution layers of 16, 32 and 64 filters of size 5×5 pixels (each one is followed by a ReLu activation and a max-pooling layer of size 2×2 pixels) and one fully-connected layer of 64 neurons.” They trained and tested their model on simulated data using 60 training radargrams and 40 testing. I plan on splitting my single radargram into images and using the same proportion as the study. In order to identify features, I plan on creating a density plot relating to the color variation in the GPR profile. Denser dots are equivalent to darker colors in the profile which correlates to a key feature.

## Conclusion about predicted Model Performance:
I predict that my model will not perform as well as the study because the features I am aiming at identifying with the model are not as differentiated as the parabolas that the study was trying to identify. Instead, I am asking my model to identify important features, which in my radargram are steeply dipping reflections. Most of my profiles have steeply dipping reflections, so I am interested in seeing what features the model will identify as most important compared to my own interpretations. 
