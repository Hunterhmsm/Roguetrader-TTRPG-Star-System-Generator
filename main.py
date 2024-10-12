import random
import numpy
from generation import amountOfSystemFeatures, systemFeatures, starType





def main():
    #gets the system features and stores them in a list
    features = []
    systemFeaturesNumber = amountOfSystemFeatures()
    while systemFeaturesNumber > 0:
        tempFeature = systemFeatures()
        if tempFeature not in features:
            features.append(tempFeature)
            systemFeaturesNumber -= 1

    #gets the type of star
    typeOfStar = starType()


if __name__ == "__main__":
    main()
