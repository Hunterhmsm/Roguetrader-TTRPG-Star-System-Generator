# generation.py will generate the random elements of the star system
#
# it will NOT generate the image of the star system
#
#
#

#imports
import random
import array

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

#NEED TO FIND WAY TO DEAL WITH A FEW CERTAIN STAR TYPES AND SYSTEM TYPES
#returns a list of elements in the Primary Bioshere
def primaryBioshereElements(star):
    elements = [] #list of elements
    #do the few stars that specifically influence the inner cauldron
    if star == "Mighty":
        amount = random.randint(1, 5) - 2
    else: #every other star
        amount = random.randint(1, 5)
    #if less than 1, is 1
    if amount <= 0:
        amount = 1
    #d100 roll
    while amount > 0:
        #change for evertime around it goes to different feature
        rollin = random.randint(1,100)
        if 1 == rollin or rollin <= 20:
            elements.append("Nothing") 
        elif 21 == rollin or rollin <= 30:
            elements.append("Asteroid Belt")
        elif 31 == rollin or rollin <= 41:
            elements.append("Asteroid Cluster") 
        elif 42 == rollin or rollin <= 47:
            elements.append("Derelict Station") 
        elif 48 == rollin or rollin <= 58:
            elements.append("Dust Cloud")
        elif 59 == rollin or rollin <= 64:
            elements.append("Gravity Riptide")
        elif 65 == rollin or rollin <= 93:
            elements.append("Planet") 
        elif 94 == rollin or rollin <= 100:
            elements.append("Starship Graveyard")  
        amount -= 1
    return elements

#NEED TO FIND WAY TO DEAL WITH A FEW CERTAIN STAR TYPES AND SYSTEM TYPES
#returns a list of elements in the Outer Reaches
#good for single genereations
def outerReachesElements(star):
    elements = [] #list of elements
    #do the few stars that specifically influence the inner cauldron
    if star == "Dull":
        amount = random.randint(1, 5) + 2
    else: #every other star
        amount = random.randint(1, 5)
    #if less than 1, is 1
    if amount <= 0:
        amount = 1
    #d100 roll
    while amount > 0:
        #change for evertime around it goes to different feature
        rollin = random.randint(1,100)
        if 1 == rollin or rollin <= 20:
            elements.append("Nothing")
        elif 21 == rollin or rollin <= 29:
            elements.append("Asteroid Belt")
        elif 30 == rollin or rollin <= 40:
            elements.append("Asteroid Cluster")  
        elif 41 == rollin or rollin <= 46:
            elements.append("Derelict Station")  
        elif 47 == rollin or rollin <= 55:
            elements.append("Dust Cloud") 
        elif 56 == rollin or rollin <= 73:
            elements.append("Gas Gaint") 
        elif 74 == rollin or rollin <= 80:
            elements.append("Gravity Riptide")
        elif 81 == rollin or rollin <= 93:
            elements.append("Planet")
        elif 94 == rollin or rollin <= 100:
            elements.append("Starship Graveyard")
        amount -= 1
    return elements

#Generates ALL System Elemets
#Doesnt work well for Binary stars 
#Binary stars need the stronger of the 2 to declare the solarzones in a area
#THIS LOOKS LIKE SHIT
def systemElements(star):
    solarzoneI = random.randint(1,5)
    solarzoneP = random.randint(1,5)
    solarzoneO = random.randint(1,5)
    InnerCauldron = 0
    InnerCauldronElements = []
    PrimaryBiosphere = 0
    PrimaryBiosphereElements = []
    OuterReaches = 0
    OuterFeaturesElements = []
    #solarzones detemin how many system elemets are in a system
    #solar zones use starMap index to determin which star is 
    initialize = 0
    while initialize == 0:
        if star == "Mighty":
            InnerCauldron = solarzoneI+2
            PrimaryBiosphere = solarzoneP-2
            OuterReaches = solarzoneO
        elif star == "Vigorous":
            InnerCauldron = solarzoneI
            PrimaryBiosphere = solarzoneP
            OuterReaches = solarzoneO
        elif star == "Luminous":
            InnerCauldron = solarzoneI-2
            PrimaryBiosphere = solarzoneP
            OuterReaches = solarzoneO
        elif star == "Dull":
            InnerCauldron = solarzoneI
            PrimaryBiosphere = solarzoneP
            OuterReaches = solarzoneO+2
        elif star == "Anomalous":
            #Should allow one zone to be +2 and one zone -2
            gamble = random.randint(1,3)
            again = random.randint(1,3)
            #should make it so gamble and again do not equal eachother
            #this is a moster code
            if gamble == again:
                if gamble == 1:
                    again+1
                elif gamble == 2:
                    again+1
                elif gamble == 3:
                    again-1
            #gamble adds 2 to solarzone by making it a DOMINANT zone
            #again subtracts 2 to solar by making it a WEAK zone
            #since gamble and again are different went through combinations manually
            elif gamble == 1 and again == 2:
                InnerCauldron = solarzoneI + 2
                PrimaryBiosphere = solarzoneP - 2
                OuterReaches = solarzoneO
            #this looks like manually input values to view if something is even.
            elif gamble == 1 and again == 3:
                InnerCauldron = solarzoneI + 2
                PrimaryBiosphere = solarzoneP
                OuterReaches = solarzoneO - 2
            elif gamble == 2 and again == 1:
                InnerCauldron = solarzoneI - 1
                PrimaryBiosphere = solarzoneP + 2
                OuterReaches = solarzoneO
            elif gamble == 2 and again == 3:
                InnerCauldron = solarzoneI
                PrimaryBiosphere = solarzoneP + 2
                OuterReaches = solarzoneO - 2
            elif gamble == 3 and again == 1:
                InnerCauldron = solarzoneI - 2
                PrimaryBiosphere = solarzoneP
                OuterReaches = solarzoneO + 2
            elif gamble == 3 and again == 2:
                InnerCauldron = solarzoneI
                PrimaryBiosphere = solarzoneP - 2
                OuterReaches = solarzoneO + 2
        elif star == "Binary":
            #this is complicated using the solarzone of the most powerful star in the binary system
            #Needs to be added to later for now assuming a Vigorous formation is most powerful in formation
            InnerCauldron = solarzoneI
            PrimaryBiosphere = solarzoneP
            OuterReaches = solarzoneO
        initialize = 1
    #makes sure there is not a negative number or a zero for solar zones in a location
    #solar zones can have nothing but should have the chance to have something
    while initialize == 1:
        if InnerCauldron <= 0:
            InnerCauldron = 1
        if PrimaryBiosphere <= 0:
            PrimaryBiosphere = 1
        if OuterReaches <= 0:
            OuterReaches = 1
        initialize = 2
    #Displays different sytem elements make sure to put into a different variable everytime
    i = 1
    
    while InnerCauldron >= i:
        #change for evertime around it goes into a differnt feature
        #This works but looks ugly
        rollin = random.randint(1,100)
        if 1 == rollin or rollin <= 20:
            InnerCauldronElements.append("Nothing")
        elif 21 == rollin or rollin <= 29:
            InnerCauldronElements.append("Asteroid Cluster")
        elif 30 == rollin or rollin <= 41:
            InnerCauldronElements.append("Dust Cloud")
        elif 42 == rollin or rollin <= 45:
            InnerCauldronElements.append("Gas Giant")
        elif 46 == rollin or rollin <= 56:
            InnerCauldronElements.append("Gravity Riptide") 
        elif 57 == rollin or rollin <= 76:
            InnerCauldronElements.append("Planet")
        elif 77 == rollin or rollin <= 88:
            InnerCauldronElements.append("Radiation Burts")
        elif 89 == rollin or rollin <= 100:
            InnerCauldronElements.append("Solar Flares")
        i = i+1
    i = 1
    #Same as before but with Primary Biosphere 
    while PrimaryBiosphere >= i:
        #change for evertime around it goes to different feature
        rollin = random.randint(1,100)
        if 1 == rollin or rollin <= 20:
            PrimaryBiosphereElements.append("Nothing") 
        elif 21 == rollin or rollin <= 30:
            PrimaryBiosphereElements.append("Asteroid Belt")
        elif 31 == rollin or rollin <= 41:
            PrimaryBiosphereElements.append("Asteroid Cluster") 
        elif 42 == rollin or rollin <= 47:
            PrimaryBiosphereElements.append("Derelict Station") 
        elif 48 == rollin or rollin <= 58:
            PrimaryBiosphereElements.append("Dust Cloud")
        elif 59 == rollin or rollin <= 64:
            PrimaryBiosphereElements.append("Gravity Riptide")
        elif 65 == rollin or rollin <= 93:
            PrimaryBiosphereElements.append("Planet") 
        elif 94 == rollin or rollin <= 100:
            PrimaryBiosphereElements.append("Starship Graveyard")  
        i = i+1
    i = 1
    while OuterReaches >= i:
        #Initializes and rolles for outer reaches
        rollin = random.randint(1,100)
        if 1 == rollin or rollin <= 20:
            OuterFeaturesElements.append("Nothing")
        elif 21 == rollin or rollin <= 29:
            OuterFeaturesElements.append("Asteroid Belt")
        elif 30 == rollin or rollin <= 40:
            OuterFeaturesElements.append("Asteroid Cluster")  
        elif 41 == rollin or rollin <= 46:
            OuterFeaturesElements.append("Derelict Station")  
        elif 47 == rollin or rollin <= 55:
            OuterFeaturesElements.append("Dust Cloud") 
        elif 56 == rollin or rollin <= 73:
            OuterFeaturesElements.append("Gas Gaint") 
        elif 74 == rollin or rollin <= 80:
            OuterFeaturesElements.append("Gravity Riptide")
        elif 81 == rollin or rollin <= 93:
            OuterFeaturesElements.append("Planet")
        elif 94 == rollin or rollin <= 100:
            OuterFeaturesElements.append("Starship Graveyard")
        i = i+1
    #NOW IMPROVED VERSION
    #LOOKS LIKE SHIT
    return print(InnerCauldronElements, PrimaryBiosphereElements, OuterFeaturesElements)





    system = { #dictonary or 

    }

    #DEBUGGING


def main():
    print(starType())
    #proof that sytemelements works for now
    print(innerCauldronElements(starType()))
    print(primaryBioshereElements(starType()))
    print(outerReachesElements(starType()))
    #print(systemElements(starType()))

if __name__ == "__main__":
    main()

