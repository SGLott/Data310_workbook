# Final Project: Image Classification of Ground Penetrating Radar Profiles

### Abstract
Ground penetrating radar (GPR) is a tool used to determine changes in sediment properties, such as mineralogy, grain size, and water content, under the surface of the earth by 
sending radar waves underground and measuring their time to return. The resultant GPR profiles (Figure 1) show a picture of the structure of sediment under the earth’s surface. 
The orientation of features within a radargram can give us information about how land formed through time. Typically, to analyze a GPR profile, someone would 
individually trace every reflection within a profile. This can lead to human error as certain features might not be noticed by the human eye, or importance of a 
feature may be over or under valued by the interpreter. A first step in reducing error is to see if a model can identify and classify features within a GPR transect.
Seven GPR profiles totaling 5 km were broken into 740 50x50 pixel tiles. The tiles were then split into a training and testing dataset and classified based on feature 
presence and dip direction. The three classes were no feature/no dip direction, feature dipping left, and feature dipping right. Using 