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

### EDA

From the EDA process, we saw that the data is quite balanced and we did not have one breed over- or under-represented. I also printed a sample of what the 120 breeds look like. There are several breeds that look alike either because they belong to the same breed dog, share an ancestor, or or in the case of Poodles and Schnauzer, they are the same breed but different sizes.

#### Limitations highlighted by the EDA Process

Note: though not printed in the notebook. When manually browsing through the images, I noticed that the data presented a few issues as mentioned above, including:
- Multiple breeds in one picture
- The wrong breed present in a breed's dataset
- For the Eskimo Dog, the entire dataset had wrong images, so the model never learned what the Eskimo Dog breed looks like

Prior to training the final model, I attemped to clean the data for the issues above (although I did not catch the issue with the Eskimo Dog dataset until after the model had trained), but only was able to clean 30% of my data due to time constrains.

### Modeling

This project used transfer learning, with InceptionV3, to train the dog classifying model. The benefit of using InceptionV3 is that the model maintain (relatively) low number of parameters, so it trains (relatively) quickly.

Model Structure:
- Sequential
- Input Layer:
    - InceptionV3
    - GlobalAveragePooling2D
    - Dropout, 0.2
- Output layer:
    - Dense, 'softmax'
- Relularization:
    - EarlyStop
    - ReduceLROnPlateau

#### Training-outcomes

I used a loss function of categorical cross entropy, and Adam optimizer, and tracked accuracy.
- Performance:
    - Validation loss: 0.6287
    - Validation accuracy: 0.8087

## Model Metrics Analysis

#### Single-breed classification

- Global Accuracy (across all breeds): 86%
- Global Precision (across all breeds): 86%

**Breed-by-breed performance**
For a report that outlines the precision, recall, and f1-score for each of the 120 breeds, please refer to the notebook. Some highlights include:

- Over 60% of breeds have recall scores of 0.90 or above
- Only 9 breeds had recall scores of

#### Mixed-breed classification
Because I did not train a multi-label classification model, in order to do mixed-breed predictions I simply took the top 10 predictions and compared it to the actual breed makeup.

I tested the model's ability to do multi-breed classification by testing it on 120 different dogs that were of only two different breeds.

Results:
- Any matches: Out of the top ten predictions, the model correctly matches at least one of the two breeds 88% of the time.  
- All matches: Out of the top then predictions, the model matches both breeds at a rate of 30%.

#### Misclassification Analysis

Please refer to the Model Metrics notebook for a more-in-depth analysis of the main misclassification issues. Three main reasons that I found for misclassifications include:
- Cases when the dog breeds simply look too similar:
  - dog breeds that look very similar experience some of the highest rate of misclassification. This is no surprise, since the model if being trained on visual cues, if two breeds are visually similar, then yes, the model will tend to make more mistakes.
- Cases where the breeds belong to the same breed dog:
  - i.e. Standard Poodles, Miniature Poodles, Toy Poodles. Some breeds are essentially the same breed with variation in scale. In these cases, the model had a more difficult time distinguishing within the same breed group.
- Cases where the data was not reliable (the dataset had many errors in general). I've mentioned the data for the Eskimo Dog was 100% inaccurate. Another instance of incorrect data is with the Cocker Spaniel. There are actually two Cocker Spaniels, American and English and pictures of both were grouped together, but both breeds look quite different.

## Conclusions
- When used as a single breed classifier, the model performs well with an 85% accuracy score, and a global precision score of 86%.
  - The high performance of this model, despite the problems with the data, suggests that with cleaner data, and a more complex neural network (i.e. EfficentNetB7), we may have a model that performs with enough certainty that it can boost shelter's ability to classify pure-breed dogs.

- Pit Bulls:  the model was able to identify bullterriers with precisions scores of 71% or more and can provide help reduce the False Positive rate for Pit Bulls at shelters.

- As a mixed-breed classifier, I use this model for fun only. More importantly, as a next step, I will make a proper multilabel classification model.
