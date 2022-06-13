# Dog Breed Classifier

## Problem Statement 

Over 3 million dogs enter a shelters in the U.S. and about 2 million get adopted each year. About 20-25% of dogs in shelters are purebred and about 75-80% are mixed breed dogs. Studies have shown that shelter staff, despite their experience, misclassify dogs often. When it comes to mixed-breed dogs shelter staff correctly guess the primary breed about 56% of the time. However, when trying to identify a secondary breed, that rate dropped to 10%. 

Correctly identifying breeds is important, as certain breeds have both health and behavioral predispositions. Having a good estimate of your dog breeds can help you provide it with the best environment to thrive. 

Accurately breeds can also be a matter of life and death for dogs are kill shelters. Pit bulls and related breeds have a reputation for aggression, so many families avoid adopting this breed and are euthanized at a high rate. However, a study has shown that shelters suffer a high 'false positive' rate when classifying pit bulls. Of dogs whose DNA was tested, about 50% of dogs that were classified as Pit Bulls by shelters did not have Pit Bull DNA. 

Therefore, I build a image classification model to predict dog breed and measure whether they can improve the classification rate of single-breed dogs compared to shelters. I also saw an opportunity to look at the top 10 predictions from my model, to see if the model (although trained on single breeds), can improve classification rates of mixed-breed dogs. 

## About the Data 

The **training data** was obtained from the Standford Dogs Data set, which you can access [here](http://vision.stanford.edu/aditya86/ImageNetDogs/)
- Over 20000 pictures in total
- Includes 120 breeds (Please refer to the EDA notebook for explore breeds, and how many pictures are available per breed)
- balanced data 

**Note:** I did not realize that until I began training the model that this dataset presents a lot of issues. There is a folder per each breed, however, the data is not clean within each holder. Many pictures feature more than one breed of dog, sometimes the wrong breed is included in the wrong folder. And at worst, the Eskimo Dog's pictures are all incorrect. As part of part two of this project, I will work to clean this dataset. 

For the **testing data**, I used some images from the following [dataset](https://www.kaggle.com/datasets/gpiosenka/70-dog-breedsimage-data-set), as well as conducted my own google images. 
- Includes 120 breeds 
- the data is not balanced, but that's ok since it was used only to test the model

## Approach


