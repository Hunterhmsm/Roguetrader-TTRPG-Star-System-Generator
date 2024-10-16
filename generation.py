# generation.py will generate the random elements of the star system
#
# it will NOT generate the image of the star system
#
#
#

#imports
import random

#determines the amount of system features
def amountOfSystemFeatures():
    int = random.randint(1,5)
    int -= 2
    
    if int <= 0:
        int = 1
    return int

#generates the system feature
def systemFeatures():
    
    systemFeature = random.randint(1, 10) # random int 1-10 assigned to systemFeature

    features = {      # dictonary of features based on roll
       1: "Bountiful",
       2: "Gravity_Tides",
       3: "Haven",
       4: "Ill_Omened",
       5: "Pirate_Den",
       6: "Ruined_Empire",
       7: "Starfarers",
       8: "Stellar_Anomoly",
       9: "Warp_Stasis",
       10: "Warp_Turbulence"
   }
    #return feature based on roll
    return features[systemFeature]



    #UGLY WAY OF DOING IT GO AWAY
    #if systemfeature == 1:
     #  feature = "Bountiful"
  #  elif systemfeature == 2:
   #     feature = "Gravity_Tides"
  #  elif systemfeature == 3:
  #      feature = "Haven"
   # elif systemfeature == 4:
   #     feature = "Ill_Omened"
   # elif systemfeature == 5:
   #     feature = "Pirate_Den"
   # elif systemfeature == 6:
   #     feature = "Ruined_Empire"
   # elif systemfeature == 7:
   #     feature = "Starfarers"
   # elif systemfeature == 8:
    #    feature = "Stellar_Anomoly"
    #elif systemfeature == 9:
   #     feature = "Warp_Stasis"
   # elif systemfeature == 10:
       # feature = "Warp_Turbulence"
    #return feature


#generates the star type
def starType():

    star = random.randint(1,10) # random int 1-10 assigned to star

    starMap = {     # dictonary of star types based on roll   
        1: "Mighty",
        2: "Vigorous",
        3: "Vigorous",         
        4: "Vigorous",
        5: "Luminous",
        6: "Luminous",
        7: "Luminous",
        8: "Dull",
        9: "Anomalous",
        10: "Binary"
    }
    #return star type based on roll
    return starMap[star]

    #DEBUGGING

def main():
    print(starType())

if __name__ == "__main__":
    main()

