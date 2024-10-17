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
    int = random.randint(1,5) - 2
    
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
#
#NEED TO FIND WAY TO DEAL WITH A FEW CERTAIN STAR TYPES AND SYSTEM TYPES
#returns a list of elements in the Inner Cauldron
def innerCauldronElements(star):
    elements = [] #list of elements
    element = "" 
    #do the few stars that specifically influence the inner cauldron
    if star == "Mighty":
        amount = random.randint(1, 5) + 2
    elif star == "Luminous":
        amount = random.randint(1, 5) - 2
    else: #every other star
        amount = random.randint(1, 5)
    #if less than 1, is 1
    if amount <= 0:
        amount = 1
    #d100 roll
    while amount > 0:
        roll100 = random.randint(1, 100)
        if 1 <= roll100 <= 20:
            element = "No_Feature"
        elif 21 <= roll100 <= 29:
            element = "Asteroid_Cluster"
        elif 30 <= roll100 <= 41:
            element = "Dust_Cloud"
        elif 42 <= roll100 <= 45:
            element = "Gas_Giant"
        elif 46 <= roll100 <= 56:
            element = "Gravity_Riptide"
        elif 57 <= roll100 <= 76:
            element = "Planet"
        elif 77 <= roll100 <= 88:
            element = "Radiation_Bursts"
        elif 89 <= roll100 <= 100:
            element = "Solar_Flares"
        #add chosen element to list of elements
        elements.append(element)
        amount -= 1
    #return list of elements
    return elements

       

    #DEBUGGING

def main():
    print(starType())

if __name__ == "__main__":
    main()

