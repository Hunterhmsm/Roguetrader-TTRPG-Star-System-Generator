# main.py will import in everything else we create to
# generate the random star system and then display it in the UI
# 
# 
#
#

#list of imports
import random
import numpy
from generation import amountOfSystemFeatures, systemFeatures, starType, innerCauldronElements

def main():
    #gets the system features and stores them in a list
    features = [] #list of system features
    systemFeaturesNumber = amountOfSystemFeatures() #1d5-2
    while systemFeaturesNumber > 0: #while 1d5-2 > 0
        tempFeature = systemFeatures() #pulls a random system feature
        if tempFeature not in features: #if the feature isnt already in the list   
            features.append(tempFeature) #add it to the list
            systemFeaturesNumber -= 1 #reduce the amount of features left by 1
    
    #gets the type of star randomly
    typeOfStar = starType()

    #gets inner cauldron elements
    innerCauldron = innerCauldronElements(typeOfStar)


    #debugging
    for feature in features:
        print("System Feature" , feature)
    print("Star" , typeOfStar)
    for element in innerCauldron:
        print("Inner Cauldron Element", element)

if __name__ == "__main__":
    main()
