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
       4: "Ill Omened",
       5: "Pirate Den",
       6: "Ruined Empire",
       7: "Starfarers",
       8: "Stellar Anomoly",
       9: "Warp Stasis",
       10: "Warp Turbulence"
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
            element = "No Feature"
        elif 21 <= roll100 <= 29:
            element = "Asteroid Cluster"
        elif 30 <= roll100 <= 41:
            element = "Dust Cloud"
        elif 42 <= roll100 <= 45:
            element = "Gas Giant"
        elif 46 <= roll100 <= 56:
            element = "Gravity Riptide"
        elif 57 <= roll100 <= 76:
            element = "Planet"
        elif 77 <= roll100 <= 88:
            element = "Radiation Bursts"
        elif 89 <= roll100 <= 100:
            element = "Solar Flares"
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
    #LOOKS SLIGHTLY BETTER 
    #Seperates System Elements
    return print("Inner Cauldron's Elements: ",InnerCauldronElements,"\nPrimary Bioshpere's Elements: ",PrimaryBiosphereElements,"\nOuter Feature's Elements: ",OuterFeaturesElements)





    system = { #dictonary or 

    }

    #DEBUGGING

#Generates what the derelict station, origin's is 
#probably could write a better way to read the descriptions
def derelictStationOrigins():
    #roll d100
    rollin = random.randint(1,100)
    #produces what the station was used for and the description of the station
    if 1 == rollin or rollin <= 10:
        reason = "Egarian Void-maze"
        description = "The station is a baffling construct of crystals with no readily apparent purpose or function but, \nbuilt along similar geometrical principles as the dead cities of the Egarian Dominion."
    elif 11 == rollin or rollin <= 20:
        reason = "Eldar Orrery"
        description = "The station is constructed of the smooth, bone-like material from which the Eldar make their ships, and is riddled with cloistered cells. \nExamination by a Navigator or psyker hints at a long-vanished power permeating the structure."
    elif 21 == rollin or rollin <= 25:
        reason = "Eldar Gate"
        description = "This vast Eldar contraption resembles nothing so much as the frame of an enormous door, but only the empty void shows through it. \nNo amount of searching yields a sign of its purpose or function."
    elif 26 == rollin or rollin <= 40:
        reason = "Ork Rok"
        description = "From the outside, this “station” appears to be nothing more than a lonely, out of the way asteroid. \nDespite its appearance, it has been thoroughly hollowed out, and filled with dubious Orky technology. Some of the technology might even have worked at one point."
    elif 41 == rollin or rollin <= 50:
        reason = "STC Defence Station"
        description = "The core of the station is based off a standard pattern derived from Standard Template Construct technology, like countless others throughout the Imperium. \nWhat remains of the banks of weapon batteries and torpedo bays indicates that it was once intended to safeguard a human colony from attack"
    elif 51 == rollin or rollin <= 65:
        reason = "STC Monitor Station"
        description = "The core of the station is based off a standard pattern derived from Standard Template Construct technology, like countless others throughout the Imperium. \nDespite its age, the hull still bristles with auger arrays and reception panels that indicate its former use as a communications or intelligence hub."
    elif 66 == rollin or rollin <= 75:
        reason = "Stryxis Collection"
        description = "Calling this accumulation of wreckage and junk a space station would insult an Ork Mek, much less a shipwright of the Adeptus Mechanicus. \nThe only explanation for its accretion comes from the vox-beacon broadcasting some kind of territorial claim by the Stryxis"
    elif 77 == rollin or rollin <= 85:
        reason = "Xenos Defence Station"
        description = "The architecture of the station does not match any examples yet encountered, but it is clearly inhuman in origin. \nThough the technology that comprises it is strange, there is no mistaking the intended purpose of its decaying armaments"
    elif 86 == rollin or rollin <= 100:
        reason = "Xenos Monitor Station"
        description = "The architecture of the station does not match any examples yet encountered, but it is clearly inhuman in origin. \nIts purpose is hard to ascertain for sure, but some of the arcane devices that line its hull resemble vox hubs and other necessities for a deep space monitor station."
    return print("Reason:", reason, "\nDescription:", description)

#Generates Starship Graveyard Origins
#probably could write a better way to read the descriptions
#The nature of the race or races that produced the ships is left to the GM’s discretion.
#possibly put together with system elements
#or leave as is to generate later
def starshipGraveyardOrigins():
    #roll d100
    rollin = random.randint(1,100)
    #produces what the caused the graveyard 
    if 1 == rollin or rollin <= 15:
        reason = "Crushed Defence Force/Routed Invasion"
        #these descriptions are really long
        description = "The wreckage is all that remains of a defeated battlefleet. Whichever side of the long-ago conflict that fielded these vessels was decisively defeated, \nwith most or all of the hulks belonging to the same force. The graveyard consists of 2d5 ships, of which most or all have been shattered beyond any value."
        ships = (random.randint(1,5)+random.randint(1,5))
    elif 16 == rollin or rollin <= 20:
        reason = "Fleet Engagement"
        description = ": A massive conflict once raged here, as evidenced by the abundance of battle-scarred hulls left behind by both sides. \nThe graveyard consists of 1d10+6 hulks, and can also include vast fields of unexploded mines, spent volleys of torpedoes, or the drifting wings of attack craft. \nRoughly half of the ships and materiel expended came from each side. \nThe fury of the conflict consumed much of value, but the sturdy construction of warships means that at least a few of them might be worth salvaging."
        ships = random.randint(1,10)+6
    elif 21 == rollin or rollin <= 35:
        reason = "Lost Explorers"
        description = "These ships were not lost to enemy action, but to overextended supply vaults, or the failure of long suffering vital systems. \nThe expedition is unlikely to include as many as even half a dozen ships, but few (if any) of them have deteriorated enough to prohibit salvage efforts."
        #up to DM usally less than half a dozen
        ships = "up to DM usally less than half a dozen"
    elif 36 == rollin or rollin <= 65:
        reason = "Plundered Convoy"
        description = "A lost shipping lane of some kind might have once crossed this system, as evidenced by this gutted procession of transports and cargo vessels. \nTheir holds have been long since emptied, but it is possible their attackers might have missed something of value. \nThere are 1d5+2 ships in the convoy, of which most or all remain intact enough to allow boarding, but little else"
        ships = random.randint(1,5)+2
    elif 66 == rollin or rollin <= 90:
        reason = "Skirmish"
        description = " Elements from two different battlefleets clashed here, with each leaving behind a handful of their complement. The graveyard consists of 1d5+3 hulks. \nRoughly half of the ships came from each side. The fury of the conflict all ships involved, \nbut the sturdy construction of warships means that at least a few of them might be worth salvaging."
        ships = random.randint(1,5)+3
    elif 91 == rollin or rollin <= 100:
        reason = "Unknown Provenance"
        description = "The bizarre assortment of different vessels drifting past defies easy explanation. \nIt is likely to bring to mind the eerie legends of the Processional of the Damned, where broken ships from across the Expanse arrive like spectres in some strange afterlife. \nWhether associated with that haunted realm, or the result of some more mundane confusion, \nthe graveyard consists of the twisted wreckage of dozens of utterly ruined ships of all kinds, as well as 1d5 hulks in varying degrees of integrity. \nNone of the hulks share an origin"
        ships = random.randint(1,5)
    #Template possible for latter use
    #elif == rollin or rollin <= :
    #   reason = ""
    #    description = ""
    return print("Reason: ",reason,"\nDescription: ",description,"\nShips: ",ships)

#Uses a normal Planet, generate its Body, Gravity, Orbital Features, Atmosphere, Climate, Habitability, and Landmasses
#Used to generate ROCK PLANETS
#Generates the Entire planet
#Find Way to get generation to look cleaner with the moons situation perferably put it into a file or something 
#Find way to get Orbital Feature not to dupe don't understand why it dupes
def rockPlanetCreation(Location):
    bodyRoll = random.randint(1,10)
    #rolls a d10 for the body 
    #gets the body type of a rock planet
    if 1 == bodyRoll:
        body = "Low-Mass"
        #another set of unending descriptions
        bodyDesc = "The world is even lower in mass than its small size would suggest. It is likely comprised of light materials, \nor it has large pockets of trapped gas making up much of its volume. \nApply -7 to the result of any roll on Table 1-7: Gravity. Generate Resources and Environments as if the world was Small. \nMineral Resource deposits cannot exceed Limited in abundance."
        #-7 to gravity
        gravityRoll = random.randint(1,10)-7
    elif 2 == bodyRoll or bodyRoll == 3:
        body = "Small"
        bodyDesc = "This world lacks the mass and size to support significant gravity or resources. Apply -5 to the result of anyroll on Table 1-7: Gravity."
        #-5 to gravity
        gravityRoll = random.randint(1,10)-5
    elif 4 == bodyRoll:
        body = "Small and Dense"
        bodyDesc = "The shrunken silhouette of this Planet belies the strength of its gravity well and the richness of its crust. Generate Resources and Environments as if the world was Small. \nAdd +10 to the result of any on Table 1-19: Resource Abundance for any Mineral Resources"
        #+5 to Resource Abundance
        gravityRoll = random.randint(1,10)
    elif 5 == bodyRoll or bodyRoll <= 7:
        body = "Large"
        bodyDesc = "Worlds of this size can range across a vast spectrum of possible types."
        #NOTHING
        gravityRoll = random.randint(1,10)
    elif 8 == bodyRoll:
        body = "Large and Dense"
        bodyDesc = "Though impressive in volume, the mass of this world is, in fact, compressed significantly. Add +5 to the result of any roll on Table 1-7: Gravity. \nGenerate Resources and Environments as if the world was Large. \nAdd +10 to the result of any roll on Table 1–19: Resource Abundance for any Mineral Resources"
        #+5 to gravity and +10 to Resouce Abundance, Generate as if world was large
        gravityRoll = random.randint(1,10)+5
    elif 9 == bodyRoll or bodyRoll == 10:
        body = "Vast"
        bodyDesc = " Huge and voluminous, worlds of this type strain the upper edges of the possible size for a single world. \nSuch Planets tend to be of middling density, as they are already more massive than is common. \nAdd +4 to the result of any roll on Table 1-7: Gravity."
        #+4 to gravity 
        gravityRoll = random.randint(1,10)+4
    #makes sure gravityRoll is not negative
    if gravityRoll < 1:
        gravityRoll = 1
    if 1 == gravityRoll or gravityRoll == 2:
        gravity = "Low Gravity"
        gravityDesc = " Apply -10 to any roll on Table 1-8: Orbital Features. Apply -2 to any roll on Table 1-9: Atmospheric Presence. \nIt follows all the rules for Low Gravity Worlds (see page 269 of the ROGUE TRADER Core Rulebook)."
        #Follow low Gravity rules
        #-10 to rolls on orbital Features
        #-2 to rolls on atomspheric presence
        orbitalFeatureRoll = random.randint(1,5)-3 #rolls how many orbital features there are
        atmosphericPresnceRoll = random.randint(1,10)-2 #rolls for what the atmospheric presnce is
    elif 3 == gravityRoll or gravityRoll <= 8:
        gravity = "Normal Gravity"
        gravityDesc = "This Planet's gravity is roughly Terran Standard."
        #NOTHING
        orbitalFeatureRoll = random.randint(1,5)-2 #rolls how many orbital features there are
        atmosphericPresnceRoll = random.randint(1,10) #rolls for what the atmospheric presnce is
    elif gravityRoll >= 9:
        gravity = "High Gravity"
        gravityDesc = "Add +10 to any roll on Table 1-8: Orbital Features. Add +1 to the roll on Table 1-9: Atmospheric Presence. \nThis Planet follows all the rules for High Gravity Worlds (see page 269 of the ROGUE TRADER Core Rulebook)."
        #+10 to rolls on orbital features
        #+1 to rolls on Atmosheric Presence
        #Follow High Gravity rules
        orbitalFeatureRoll = random.randint(1,5)-1 #rolls how many orbital features there are
        atmosphericPresnceRoll = random.randint(1,10)+1 #rolls for what the atmospheric presnce is
    #makes sure orbital Feature roll is min 1
    if orbitalFeatureRoll <= 1:
        orbitalFeatureRoll = 1
    orbitalFeature = [] #list of orbital features
    orbitalFeatDESC = [] #Description of orbital feature
    while orbitalFeatureRoll >= 1:
        if gravity == "Low Gravity":
            rollOrbitalFeat = random.randint(1,100)-10
        elif gravity == "High Gravity":
            rollOrbitalFeat = random.randint(1,100)+10
        else:
            rollOrbitalFeat = random.randint(1,100)
        if rollOrbitalFeat <= 45:
            orbitalFeature.append("nothing")
            orbitalFeatDESC.append("\nOrbital Feature Description: nothing")
        elif 46 == rollOrbitalFeat or rollOrbitalFeat <= 60: 
            orbitalFeature.append("Large Asteroid")
            orbitalFeatDESC.append("\nOrbital Feature Description: An asteroid of unusual size has been captured by the Planet's gravity well, and now occupies a stable orbit around it. \nIt is just large enough to be noted by an orbital survey, but not enough to be seen from the Planet's surface without visual enhancement.")
        elif 61 == rollOrbitalFeat or rollOrbitalFeat <= 90:
            orbitalFeature.append("Lesser Moon")
            mineral = random.randint(1,10)
            if mineral >= 6:
                #Roll for abundace with -5 to roll
                minRec = mineralResource()
                abundRoll = random.randint(1,100)-5
                abundance = resourceAbundance(abundRoll)
            else:
                minRec = "None :("
                abundance = "None no minerals"
            orbitalFeatDESC.append("\nOrbital Feature Description: An orbital body somewhere between an extremely large asteroid and a very small moon orbits the Planet. \nIt has its own extremely limited gravity well, allowing low-gravity travel across the surface, as described on page 269 of the ROGUE TRADER Core Rulebook. \nWhen generating a Lesser Moon, roll 1d10; on a result of 6 or higher, it houses sufficient mineral wealth to count as a Resource. \nRoll once on Table 1–20: Mineral Resources and once on Table 1–19: Mineral Abundance, receiving a –5 penalty to the latter roll.\nMinerals on Lesser Moon: "+ minRec +"\nAbundance of Resource: "+ abundance)
        elif 91 <= rollOrbitalFeat:
            orbitalFeature.append("MOON")
            orbitalFeatDESC.append("\nOrbital Feature Description: A true moon is generated as a Planet, using the rules for Planet Creation (see page 19). \nUnder normal circumstances, a moon cannot have a higher Planetary Body than the world around which it orbits. \nIn addition, a moon never generates its own Orbital Features.")
            #create another method for MOON creation using the same as planets but without the moon to get a bigger size than the planets
            moonCreation(body, Location)
        orbitalFeatureRoll -= 1 
    #Used to generate the atmoshere of the planet
    if atmosphericPresnceRoll <= 1:
        Atmosphere = "None :("
        atmosphereDesc = "The Planet has no atmosphere, or it has one so thin as to be effectively nonexistent. \nActivity on the Planet is treated as being in vacuum, as covered on pages 262-263 of the ROGUE TRADER Core Rulebook. \nNormally, this means that there is no need to roll on Table 1-10: Atmospheric Composition"
    elif 2 == atmosphericPresnceRoll or atmosphericPresnceRoll <= 4:
        Atmosphere = "Thin"
        atmosphereDesc = " The Planet's atmosphere is weak, but avoids the problems of an actual vacuum. \nTests to avoid harm from a Toxic or Corrosive atmosphere are made at a +10 bonus. However, the lack of air makes strenuous activity difficult. \nAny time an Explorer relying on the outside air gains Fatigue, he gains the normal amount plus one additional level of Fatigue instead."
    elif 5 == atmosphericPresnceRoll or atmosphericPresnceRoll <= 9:
        Atmosphere = "Moderate"
        atmosphereDesc = "Atmospheres in this range produce no ill effects due to lack or overabundance of air, though they can still be Toxic or Corrosive"
    elif atmosphericPresnceRoll >= 10:
        Atmosphere = "Heavy"
        atmosphereDesc = " A thick blanket of air presses down on the Planet, coming just short of smothering those beneath it. This oppressive weight imposes a -5 penalty on Strength or Toughness Tests, at the GM's discretion. \nTests to avoid harm from a Toxic or Corrosive Atmosphere are made at a -10 penalty. If the atmosphere is breathable, the thickness of the air makes it difficult to take in. \nA full hour of relying on such an atmosphere for air inflicts a single level of Fatigue. This effect is not cumulative, no matter how long a character relies on the air. \nHowever, recovery from this level of Fatigue cannot occur while relying on such an atmosphere." 

    #Checks to see if there is an Atmoshpere
    if Atmosphere == "None :(":
        atmosphericComp = "None No Atmosphere"
        atmoshericCompDesc = "None No Atmoshere"
    #if Atmoshpere
    #Does an Atmosheric Composition set and implements it
    else:    
        #Rolls for Atmospheric Composition
        atmosphericCompRoll = random.randint(1,10)
        if atmosphericCompRoll == 1:
           atmosphericComp = "Deadly"
           atmoshericCompDesc = "An atmosphere of this sort is little more than a vast acid bath. \nAnyone not protected by a full environmental seal suffers 1d5+1 Damage each Round that ignore Toughness Bonus and Armour. \nIf the atmosphere is also Heavy, it wears away at resistance, breaking into environmental seals after 1d10+2 hours."
           #if heavy atmoshpere breaks environmental seal after 1d10+2 hours
           #maybe add the 1d5+1 and 1d10+2 later if needed
        elif atmosphericCompRoll == 2:
            atmosphericComp = "Corrosive"
            atmoshericCompDesc = "This atmosphere is both poisonous to breathe and deadly on any sort of contact. \nAnyone not protected by a full environmental seal must make a Difficult (-10) Toughness Test each Round, or suffer 1d5 Damage that ignores Armour and Toughness Bonus. \nContinued exposure results in suffocation, as per page 261 of the ROGUE TRADER Core Rulebook."
        elif 3 == atmosphericCompRoll or atmosphericCompRoll <= 5:
            atmosphericComp = "Toxic"
            atmoshericCompDesc = "Poisonous gases and vapours fill the Planet's atmosphere. \nSimply breathing the air requires a Challenging (+0) Toughness Test each Round to avoid suffering 1 Damage that ignores Toughness Bonus and Armour. \nAdditionally, continued exposure results in suffocation, as per the rules on page 261 of the ROGUE TRADER Core Rulebook."
        elif 6 == atmosphericCompRoll or atmosphericCompRoll == 7:
            atmosphericComp = "Tainted"
            atmoshericCompDesc = "Though capable of sustaining human life, this atmosphere is not entirely safe, stained by trace elements of toxins. \nThough it does not directly affect the Explorers, it might influence the viability or costs of long-term colonisation"
        elif atmosphericCompRoll >= 8:
            atmosphericComp = "Pure"
            atmoshericCompDesc = "The atmosphere is entirely safe for humans and most other common life forms to breathe."
    
    #No atmoshpere changes how climites work
    if Atmosphere == "None :(":
        if Location == "Inner Cauldron":
            #creates a climate and its description
            climate = "Burning World"
            climateDesc = " A fierce heat blankets the Planet in its entirety. The heat usually recedes at night, but it is likely still too warm for comfort. \nThe entire Planet is affected by extreme heat. Tests made to resist the heat are Very Hard (–30)."
        elif Location == "Outer Reaches":
            #creates a climate and its description
            climate = "Ice World"
            climateDesc = "The Planet is frozen, from pole to pole. The entire Planet is affected by extreme cold. Tests made to resist the cold are Very Hard (-30)."
        else:
            coin = random.randint(1,2)
            if coin == 1:
                #creates a climate and its description
                climate = "Burning World"
                climateDesc = " A fierce heat blankets the Planet in its entirety. The heat usually recedes at night, but it is likely still too warm for comfort. \nThe entire Planet is affected by extreme heat. Tests made to resist the heat are Very Hard (–30)."
            else:
                #creates a climate and its description
                climate = "Ice World"
                climateDesc = "The Planet is frozen, from pole to pole. The entire Planet is affected by extreme cold. Tests made to resist the cold are Very Hard (-30)."
    else:
        if Location == "Inner Cauldron":
            climateRoll = random.randint(1,10)-6
        elif Location == "Outer Reaches":
            climateRoll = random.randint(1,10)+6
        else:
            climateRoll = random.randint(1,10)
        #Generates the rest of the climate infromation
        if climateRoll <= 0:
            climate = "Burning World"
            climateDesc = "A fierce heat blankets the Planet in its entirety. The heat usually recedes at night, but it is likely still too warm for comfort. \nThe entire Planet is affected by extreme heat. Tests made to resist the heat are Very Hard (–30)."
        elif 1 == climateRoll or climateRoll <= 3:
            climate = "Hot World"
            climateDesc = "Most of this Planet is dangerously hot, but various regions can be found with more moderate microclimates. \nOutside of these sheltered regions, the entire Planet is affected by extreme heat. \nTests made to resist the heat generally range from Challenging (+0) to Hard (–20). \nIn some cases, the sheltered regions are also afflicted by extreme heat, but of a less severe degree than the rest of the Planet."
        elif 4 == climateRoll or climateRoll <= 7:
            climate = "Temperate World"
            climateDesc = "Temperate Planets are exclusively found in or near a system’s Primary Biosphere. They might contain regions of either extreme heat or extreme cold, and in many cases, have some of both. \nThe Tests made to resist temperature extremes on these Planets rarely exceed Difficult (–10)."
        elif 8 == climateRoll or climateRoll <= 10:
            climate = "Cold World"
            climateDesc = " Most of this Planet is dangerously cold, but various regions can found with more moderate microclimates. \nOutside of these sheltered regions, the entire Planet is affected by extreme cold. \nTests made to resist the heat generally range from Challenging (+0) to Hard (–20). \nIn some cases, the sheltered regions are also afflicted by extreme cold, but of a less severe degree than the rest of the Planet."
        elif climateRoll >= 11:
            climate = "Ice World"
            climateDesc = "The Planet is frozen, from pole to pole. The entire Planet is affected by extreme cold. Tests made to resist the cold are Very Hard (-30)."
        #can be changed at DMS descresion to allow bad atmoshere planets to be habitable
        #this rolls for Habitability
    habRoll = 100
    if atmosphericComp == "Pure" or atmosphericComp == "Tainted":
        if climate == "Cold World" or climate == "Hot World":
            habRoll = random.randint(1,10)-2
        elif climate == "Ice World" or climate == "Burning World": #also makes sure habroll doesnt get better than a 3
            habRoll = random.randint(1,10)-7
            if habRoll > 3:
                 habRoll = 3
        else:
                 habRoll=random.randint(1,10)
    else:
         #used to Initialize in case planet not habitable
        habRoll = 30 #just to initialize variable (habroll of 3000 not obtainable normally) 
    if habRoll <= 1:
        habitability = "Inhospitable"
        habDesc = "There is no life or water to be found on this Planet."
    elif habRoll == 2 or habRoll == 3:
        habitability = "Trapped Water"
        habDesc = "There is water on this Planet, but it is in a form that requires processing before it can be used or consumed. \nIt might be frozen or have boiled away to vapour on Planets with extreme climates. \nAlternatively, the water could be locked away in deep channels underground, or contaminated with other materials."
    elif habRoll == 4 or habRoll == 5:
        habitability = "Liquid Water"
        habDesc = "Liquid water is accessible on the Planet's surface, but no native life has arisen to make use of it."
    elif habRoll == 6 or habRoll == 7:
        habitability = "Limited Ecosystem"
        habDesc = ": The Planet has native life of a limited variety. It could be that this Planet’s species have not advnced beyond basic proto-biology, \nor their spread across the Planet was restricted by local conditions. This might also indicate a Planet on the decline, or recovering from a devastating natural disaster."
    elif habRoll >= 8 and habRoll < 30:
        habitability = "Verdant"
        habDesc = "The Planet has a thriving ecosystem. A variety of species can be found almost anywhere on the Planet."
    elif habRoll == 30: #Change if you are DM and want a habitable planet with bad or no atmoshere
        habitability = "BAD ATMOSHERE :("
        habDesc = "NONE"
    else:
        habitability = "Error generating habitability"
        habDesc = "Error generating habitability"
    #Rolls for landmass
    landROll = random.randint(1,10)
    if landROll >= 8:
        Landmasses = random.randint(1,5)
        LandDesc = "Planet has " + str(Landmasses) + " Continent/s or Archipelegoes with a GM's discretion of small islands"
    elif landROll >= 4 and habRoll >= 4:
        Landmasses = random.randint(1,5)
        LandDesc = "Planet has  " + str(Landmasses) + " Continent/s or Archipelegoes with a GM's discretion of small islands"
    elif habRoll >= 4:
        Landmasses = 1
        LandDesc = "Planet has a single main landmass with rivers, streams and lakes"
    else:
        Landmasses = 1
        LandDesc = "Yep thats a Rock Floating in space"
    #combines orbit and features ?
    combinedOrbitFeatures = [item for pair in zip(orbitalFeature, orbitalFeatDESC) for item in pair]
    combinedOrbitFeatures += orbitalFeature[len(orbitalFeatDESC):] + orbitalFeatDESC[len(orbitalFeature):]

    #CHANGE orbital features to make more sense if it looks like shit (it will)
    #Find a way to get it so that orbital features and orbital feature description are together (FIXED)
    #rare chance that Habitability wont get filled out (It was because it was one line over in an else statement that only gets filled out when no atmoshere)
    #old version below
    #return print("Body: "+ body + "\nBody Description: "+ bodyDesc + "\n\nGravity: "+ gravity + "\nGravity Description: " + gravityDesc + "\n\nOrbital Feature: "+"\nOrbital Feature: ".join(orbitalFeature) + "\nOrbital Feature Description" + "\n\n".join(orbitalFeatDESC) + "\n\nAtmoshere: " + Atmosphere + "\nAtmoshere Description: " + atmosphereDesc + "\n\nAtmosheric Composition: "+ atmosphericComp+ "\nAtmosheric Compositon Description: "+ atmoshericCompDesc + "\n\nCLimate: " + climate + "\nClimate Discription: " + climateDesc + "\n\nHabitablility: " + habitability + "\nHabitablility Discription: " + habDesc + "\n\nLandmasses: " + str(Landmasses) + "\nLandmass Discription: " + LandDesc)
    return print("Body: "+ body + "\nBody Description: "+ bodyDesc + "\n\nGravity: "+ gravity + "\nGravity Description: " + gravityDesc + "\n\nOrbital Feature: ".join(combinedOrbitFeatures) + "\n\nAtmoshere: " + Atmosphere + "\nAtmoshere Description: " + atmosphereDesc + "\n\nAtmosheric Composition: "+ atmosphericComp+ "\nAtmosheric Compositon Description: "+ atmoshericCompDesc + "\n\nCLimate: " + climate + "\nClimate Discription: " + climateDesc + "\n\nHabitablility: " + habitability + "\nHabitablility Discription: " + habDesc + "\n\nLandmasses: " + str(Landmasses) + "\nLandmass Discription: " + LandDesc)
    
#Used to generate MOONS
#Same as Rock moons but without orbital features
#Maybe Add GAS moons? (pretty gay)
#ALWAYS displays above planet that it is orbiting
#possibly change it to be in the orbital feature but that would be right in the middle of the planets inforamtion
def moonCreation(pbody,Location):
    bodyRoll = random.randint(1,10)
    #rolls a d10 for the body 
    #gets the body type of a rock planet
    if pbody == "Low-Mass":
        bodyRoll = 1
    elif pbody == "Small":
        if bodyRoll >= 2:
            bodyRoll = 2
    elif pbody == "Small and Dense":
        if bodyRoll >= 4:
            bodyRoll = 4
    elif pbody == "Large":
        if bodyRoll >= 7:
            bodyRoll = 7
    elif pbody == "Large and Dense":
        if bodyRoll >= 8:
            bodyRoll = 8
    if 1 == bodyRoll:
        body = "Low-Mass"
        #another set of unending descriptions
        bodyDesc = "The world is even lower in mass than its small size would suggest. It is likely comprised of light materials, \nor it has large pockets of trapped gas making up much of its volume. \nApply -7 to the result of any roll on Table 1-7: Gravity. Generate Resources and Environments as if the world was Small. \nMineral Resource deposits cannot exceed Limited in abundance."
        #-7 to gravity
        gravityRoll = random.randint(1,10)-7
    elif 2 == bodyRoll or bodyRoll == 3:
        body = "Small"
        bodyDesc = "This world lacks the mass and size to support significant gravity or resources. Apply -5 to the result of anyroll on Table 1-7: Gravity."
        #-5 to gravity
        gravityRoll = random.randint(1,10)-5
    elif 4 == bodyRoll:
        body = "Small and Dense"
        bodyDesc = "The shrunken silhouette of this Planet belies the strength of its gravity well and the richness of its crust. Generate Resources and Environments as if the world was Small. \nAdd +10 to the result of any on Table 1-19: Resource Abundance for any Mineral Resources"
        #+5 to Resource Abundance
        gravityRoll = random.randint(1,10)
    elif 5 == bodyRoll or bodyRoll <= 7:
        body = "Large"
        bodyDesc = "Worlds of this size can range across a vast spectrum of possible types."
        #NOTHING
        gravityRoll = random.randint(1,10)
    elif 8 == bodyRoll:
        body = "Large and Dense"
        bodyDesc = "Though impressive in volume, the mass of this world is, in fact, compressed significantly. Add +5 to the result of any roll on Table 1-7: Gravity. \nGenerate Resources and Environments as if the world was Large. \nAdd +10 to the result of any roll on Table 1–19: Resource Abundance for any Mineral Resources"
        #+5 to gravity and +10 to Resouce Abundance, Generate as if world was large
        gravityRoll = random.randint(1,10)+5
    elif 9 == bodyRoll or bodyRoll == 10:
        body = "Vast"
        bodyDesc = " Huge and voluminous, worlds of this type strain the upper edges of the possible size for a single world. \nSuch Planets tend to be of middling density, as they are already more massive than is common. \nAdd +4 to the result of any roll on Table 1-7: Gravity."
        #+4 to gravity 
        gravityRoll = random.randint(1,10)+4
    #makes sure gravityRoll is not negative
    if gravityRoll < 1:
        gravityRoll = 1
    if 1 == gravityRoll or gravityRoll == 2:
        gravity = "Low Gravity"
        gravityDesc = " Apply -10 to any roll on Table 1-8: Orbital Features. Apply -2 to any roll on Table 1-9: Atmospheric Presence. \nIt follows all the rules for Low Gravity Worlds (see page 269 of the ROGUE TRADER Core Rulebook)."
        #Follow low Gravity rules
        #-2 to rolls on atomspheric presence  
        atmosphericPresnceRoll = random.randint(1,10)-2 #rolls for what the atmospheric presnce is
    elif 3 == gravityRoll or gravityRoll <= 8:
        gravity = "Normal Gravity"
        gravityDesc = "This Planet's gravity is roughly Terran Standard."
        #NOTHING
        atmosphericPresnceRoll = random.randint(1,10) #rolls for what the atmospheric presnce is
    elif gravityRoll >= 9:
        gravity = "High Gravity"
        gravityDesc = "Add +10 to any roll on Table 1-8: Orbital Features. Add +1 to the roll on Table 1-9: Atmospheric Presence. \nThis Planet follows all the rules for High Gravity Worlds (see page 269 of the ROGUE TRADER Core Rulebook)."
        #+10 to rolls on orbital features
        #+1 to rolls on Atmosheric Presence
        #Follow High Gravity rules
        atmosphericPresnceRoll = random.randint(1,10)+1 #rolls for what the atmospheric presnce is
    #Used to generate the atmoshere of the planet
    if atmosphericPresnceRoll <= 1:
        Atmosphere = "None :("
        atmosphereDesc = "The Planet has no atmosphere, or it has one so thin as to be effectively nonexistent. \nActivity on the Planet is treated as being in vacuum, as covered on pages 262-263 of the ROGUE TRADER Core Rulebook. \nNormally, this means that there is no need to roll on Table 1-10: Atmospheric Composition"
    elif 2 == atmosphericPresnceRoll or atmosphericPresnceRoll <= 4:
        Atmosphere = "Thin"
        atmosphereDesc = " The Planet's atmosphere is weak, but avoids the problems of an actual vacuum. \nTests to avoid harm from a Toxic or Corrosive atmosphere are made at a +10 bonus. However, the lack of air makes strenuous activity difficult. \nAny time an Explorer relying on the outside air gains Fatigue, he gains the normal amount plus one additional level of Fatigue instead."
    elif 5 == atmosphericPresnceRoll or atmosphericPresnceRoll <= 9:
        Atmosphere = "Moderate"
        atmosphereDesc = "Atmospheres in this range produce no ill effects due to lack or overabundance of air, though they can still be Toxic or Corrosive"
    elif atmosphericPresnceRoll >= 10:
        Atmosphere = "Heavy"
        atmosphereDesc = " A thick blanket of air presses down on the Planet, coming just short of smothering those beneath it. This oppressive weight imposes a -5 penalty on Strength or Toughness Tests, at the GM's discretion. \nTests to avoid harm from a Toxic or Corrosive Atmosphere are made at a -10 penalty. If the atmosphere is breathable, the thickness of the air makes it difficult to take in. \nA full hour of relying on such an atmosphere for air inflicts a single level of Fatigue. This effect is not cumulative, no matter how long a character relies on the air. \nHowever, recovery from this level of Fatigue cannot occur while relying on such an atmosphere." 

    #Checks to see if there is an Atmoshpere
    if Atmosphere == "None :(":
        atmosphericComp = "None No Atmosphere"
        atmoshericCompDesc = "None No Atmoshere"
    #if Atmoshpere
    #Does an Atmosheric Composition set and implements it
    else:    
        #Rolls for Atmospheric Composition
        atmosphericCompRoll = random.randint(1,10)
        if atmosphericCompRoll == 1:
           atmosphericComp = "Deadly"
           atmoshericCompDesc = "An atmosphere of this sort is little more than a vast acid bath. \nAnyone not protected by a full environmental seal suffers 1d5+1 Damage each Round that ignore Toughness Bonus and Armour. \nIf the atmosphere is also Heavy, it wears away at resistance, breaking into environmental seals after 1d10+2 hours."
           #if heavy atmoshpere breaks environmental seal after 1d10+2 hours
           #maybe add the 1d5+1 and 1d10+2 later if needed
        elif atmosphericCompRoll == 2:
            atmosphericComp = "Corrosive"
            atmoshericCompDesc = "This atmosphere is both poisonous to breathe and deadly on any sort of contact. \nAnyone not protected by a full environmental seal must make a Difficult (-10) Toughness Test each Round, or suffer 1d5 Damage that ignores Armour and Toughness Bonus. \nContinued exposure results in suffocation, as per page 261 of the ROGUE TRADER Core Rulebook."
        elif 3 == atmosphericCompRoll or atmosphericCompRoll <= 5:
            atmosphericComp = "Toxic"
            atmoshericCompDesc = "Poisonous gases and vapours fill the Planet's atmosphere. \nSimply breathing the air requires a Challenging (+0) Toughness Test each Round to avoid suffering 1 Damage that ignores Toughness Bonus and Armour. \nAdditionally, continued exposure results in suffocation, as per the rules on page 261 of the ROGUE TRADER Core Rulebook."
        elif 6 == atmosphericCompRoll or atmosphericCompRoll == 7:
            atmosphericComp = "Tainted"
            atmoshericCompDesc = "Though capable of sustaining human life, this atmosphere is not entirely safe, stained by trace elements of toxins. \nThough it does not directly affect the Explorers, it might influence the viability or costs of long-term colonisation"
        elif atmosphericCompRoll >= 8:
            atmosphericComp = "Pure"
            atmoshericCompDesc = "The atmosphere is entirely safe for humans and most other common life forms to breathe."
    
    #No atmoshpere changes how climites work
    if Atmosphere == "None :(":
        if Location == "Inner Cauldron":
            #creates a climate and its description
            climate = "Burning Moon"
            climateDesc = " A fierce heat blankets the Planet in its entirety. The heat usually recedes at night, but it is likely still too warm for comfort. \nThe entire Planet is affected by extreme heat. Tests made to resist the heat are Very Hard (–30)."
        elif Location == "Outer Reaches":
            #creates a climate and its description
            climate = "Ice Moon"
            climateDesc = "The Planet is frozen, from pole to pole. The entire Planet is affected by extreme cold. Tests made to resist the cold are Very Hard (-30)."
        else:
            coin = random.randint(1,2)
            if coin == 1:
                #creates a climate and its description
                climate = "Burning Moon"
                climateDesc = " A fierce heat blankets the Planet in its entirety. The heat usually recedes at night, but it is likely still too warm for comfort. \nThe entire Planet is affected by extreme heat. Tests made to resist the heat are Very Hard (–30)."
            else:
                #creates a climate and its description
                climate = "Ice Moon"
                climateDesc = "The Planet is frozen, from pole to pole. The entire Planet is affected by extreme cold. Tests made to resist the cold are Very Hard (-30)."
    else:
        if Location == "Inner Cauldron":
            climateRoll = random.randint(1,10)-6
        elif Location == "Outer Reaches":
            climateRoll = random.randint(1,10)+6
        else:
            climateRoll = random.randint(1,10)
        #Generates the rest of the climate infromation
        if climateRoll <= 0:
            climate = "Burning Moon"
            climateDesc = "A fierce heat blankets the Planet in its entirety. The heat usually recedes at night, but it is likely still too warm for comfort. \nThe entire Planet is affected by extreme heat. Tests made to resist the heat are Very Hard (–30)."
        elif 1 == climateRoll or climateRoll <= 3:
            climate = "Hot Moon"
            climateDesc = "Most of this Planet is dangerously hot, but various regions can be found with more moderate microclimates. \nOutside of these sheltered regions, the entire Planet is affected by extreme heat. \nTests made to resist the heat generally range from Challenging (+0) to Hard (–20). \nIn some cases, the sheltered regions are also afflicted by extreme heat, but of a less severe degree than the rest of the Planet."
        elif 4 == climateRoll or climateRoll <= 7:
            climate = "Temperate Moon"
            climateDesc = "Temperate Planets are exclusively found in or near a system’s Primary Biosphere. They might contain regions of either extreme heat or extreme cold, and in many cases, have some of both. \nThe Tests made to resist temperature extremes on these Planets rarely exceed Difficult (–10)."
        elif 8 == climateRoll or climateRoll <= 10:
            climate = "Cold Moon"
            climateDesc = " Most of this Planet is dangerously cold, but various regions can found with more moderate microclimates. \nOutside of these sheltered regions, the entire Planet is affected by extreme cold. \nTests made to resist the heat generally range from Challenging (+0) to Hard (–20). \nIn some cases, the sheltered regions are also afflicted by extreme cold, but of a less severe degree than the rest of the Planet."
        elif climateRoll >= 11:
            climate = "Ice Moon"
            climateDesc = "The Planet is frozen, from pole to pole. The entire Planet is affected by extreme cold. Tests made to resist the cold are Very Hard (-30)."
        #can be changed at DMS descresion to allow bad atmoshere planets to be habitable
        #this rolls for Habitability
    habRoll = 100
    if atmosphericComp == "Pure" or atmosphericComp == "Tainted":
        if climate == "Cold Moon" or climate == "Hot Moon":
            habRoll = random.randint(1,10)-2
        elif climate == "Ice Moon" or climate == "Burning Moon": #also makes sure habroll doesnt get better than a 3
            habRoll = random.randint(1,10)-7
            if habRoll > 3:
                 habRoll = 3
        else:
                 habRoll=random.randint(1,10)
    else:
         #used to Initialize in case planet not habitable
        habRoll = 30 #just to initialize variable (habroll of 3000 not obtainable normally) 
    if habRoll <= 1:
        habitability = "Inhospitable"
        habDesc = "There is no life or water to be found on this Moon."
    elif habRoll == 2 or habRoll == 3:
        habitability = "Trapped Water"
        habDesc = "There is water on this Moon, but it is in a form that requires processing before it can be used or consumed. \nIt might be frozen or have boiled away to vapour on Moons with extreme climates. \nAlternatively, the water could be locked away in deep channels underground, or contaminated with other materials."
    elif habRoll == 4 or habRoll == 5:
        habitability = "Liquid Water"
        habDesc = "Liquid water is accessible on the Moon's surface, but no native life has arisen to make use of it."
    elif habRoll == 6 or habRoll == 7:
        habitability = "Limited Ecosystem"
        habDesc = "The Moon has native life of a limited variety. It could be that this Moon’s species have not advnced beyond basic proto-biology, \nor their spread across the Moon was restricted by local conditions. This might also indicate a Moon on the decline, or recovering from a devastating natural disaster."
    elif habRoll >= 8 and habRoll < 30:
        habitability = "Verdant"
        habDesc = "The Moon has a thriving ecosystem. A variety of species can be found almost anywhere on the Moon."
    elif habRoll == 30: #Change if you are DM and want a habitable planet with bad or no atmoshere
        habitability = "BAD ATMOSHERE :("
        habDesc = "NONE"
    else:
        habitability = "Error generating habitability"
        habDesc = "Error generating habitability"
    #Rolls for landmass
    landROll = random.randint(1,10)
    if landROll >= 8:
        Landmasses = random.randint(1,5)
        LandDesc = "Moon has " + str(Landmasses) + " Continent/s or Archipelegoes with a GM's discretion of small islands"
    elif landROll >= 4 and habRoll >= 4:
        Landmasses = random.randint(1,5)
        LandDesc = "Moon has  " + str(Landmasses) + " Continent/s or Archipelegoes with a GM's discretion of small islands"
    elif habRoll >= 4:
        Landmasses = 1
        LandDesc = "Moon has a single main landmass with rivers, streams and lakes"
    else:
        Landmasses = 1
        LandDesc = "Yep thats a Rock Floating in space"
    #CHANGE orbital features to make more sense if it looks like shit (it will)
    #Find a way to get it so that orbital features and orbital feature description are together
    #rare chance that Habitability wont get filled out (It was because it was one line over in an else statement that only gets filled out when no atmoshere)
    return print("MOON GENERATED LETS GOOOOOO\nBody: "+ body + "\nBody Description: "+ bodyDesc + "\n\nGravity: "+ gravity + "\nGravity Description: " + gravityDesc + "\n\nAtmoshere: " + Atmosphere + "\nAtmoshere Description: " + atmosphereDesc + "\n\nAtmosheric Composition: "+ atmosphericComp+ "\nAtmosheric Compositon Description: "+ atmoshericCompDesc + "\n\nCLimate: " + climate + "\nClimate Discription: " + climateDesc + "\n\nHabitablility: " + habitability + "\nHabitablility Discription: " + habDesc + "\n\nLandmasses: " + str(Landmasses) + "\nLandmass Discription: " + LandDesc + "\nEND OF MOON GENERATION\n\n\n")
    
#Uses a Gas Planet, generates its body, gravity, orbital Features
# #Used to generate Gas Planets
#Find Way to get generation to look cleaner with the moons situation perferably put it into a file or something
#Find way to get Orbital Feature not to dupe don't understand why it dupes
def gasPlanetCreation(Location):
    bodyRoll = random.randint(1,10)
    #roll d10 to gen a body
    #generates the body
    mLocation = Location
    if bodyRoll <= 2:
        body = "Gas Dwarf"
        bodyDesc = "Although much smaller than the typical world of this sort, a Gas Dwarf is still considerably more massive than most rocky Planets. \nApply –5 to the result of any roll on Table 1–7: Gravity."
        #-5 to gravity gen
        gravRoll=random.randint(1,10)-5
    elif bodyRoll <= 8:
        body = "Gas Giant"
        bodyDesc = "Typical gas giants are vastly more massive than almost any other world, and tend to have correspondingly powerful gravitational effects"
        gravRoll=random.randint(1,10)
    else:
        body = "Massive Gas Giant"
        bodyDesc = "The largest gas giants can rival weaker stars in size and mass, with some of them having some degree of kinship with such bodies. \nAdd +3 to the result of any roll on Table 1–7: Gravity. In addition, any Massive= Gas Giant not in the Inner Cauldron has a chance of being one of these titans. \nWhen generating a Massive Gas Giant, roll 1d10; on a result of 8 or higher, count the result of the roll made for it on Table 1–7: \nGravity as a result of 10, and its moons are generated as if they were one Solar Zone closer to their star. Otherwise, treat it normally"
        #+3 to gravity
        rollMGG = random.randint(1,10)
        if rollMGG >= 8:
            if rollMGG == 10 and Location != "Inner Cauldron":
                if Location == "Outer Reaches":
                    mLocation = "Primary Bioshpere"
                else:
                    mLocation = "Inner Cauldron"
            gravRoll = random.randint(1,10)+rollMGG+3
        gravRoll=random.randint(1,10)+3
    #Gets the gravity generation  
    if gravRoll <= 2:
        gravity = "Weak"
        gravDesc = "Though puny by the standards of gas giants, this gravity well is stronger than that of almost any solid Planet. \nAdd +10 to any roll on Table 1–8: Orbital Features."
        #+10 Orbital Features
        orbitRoll = random.randint(1,10)-5
    elif gravRoll <= 6:
        gravity = "Strong"
        gravDesc = "This gas giant has the impressive gravity well common to such worlds. \nAdd +15 to any roll on Table 1–8: Orbital Features."
        #+15 Orbital Features
        orbitRoll = random.randint(1,10)-3
    elif gravRoll <= 9:
        gravity = "Powerful"
        gravDesc = "The influence of this gravity well extends well beyond the immediate presence of its source, drawing in whatever passes by. \nAdd +20 to any roll on Table 1–8: Orbital Features."
        #+20 Orbital Features
        orbitRoll = random.randint(1,10)+2
    else:
        gravity = "Titanic"
        gravDesc = "Add +10 to any roll on Table 1–8: Orbital Features. Add +1 to the roll on Table 1–9: Atmospheric Presence. \nThis Planet follows all the rules for High Gravity Worlds (see page 269 of the ROGUE TRADER Core Rulebook)."
        #+30 Orbital Features
        orbitRoll = random.randint(1,5)+random.randint(1,5)+random.randint(1,5)+3
        #rolls 3d5+3
    #Checks to see if orbit roll < 1 if so sets to 1
    if orbitRoll < 1:
        orbitRoll = 1
    orbitalFeature = [] #list of orbital features
    orbitalFeatDESC = [] #Description of orbital feature
    #generation of orbital features
    while orbitRoll >= 1:
        if gravity == "Weak":
            featureRoll = random.randint(1,100)+10
        elif gravity == "Strong":
            featureRoll = random.randint(1,100)+15
        elif gravity == "Powerful":
            featureRoll = random.randint(1,100)+20
        else: 
            featureRoll = random.randint(1,100)+30
        #gets the orbit features
        if featureRoll <= 20:
            orbitalFeature.append("No Feature")
            orbitalFeatDESC.append("No notable features are added to the Gas Giant’s orbit")
        elif featureRoll <= 35:
            orbitalFeature.append("Planetary Rings (Debris)")
            orbitalFeatDESC.append(" A narrow band of asteroids or chunks of ice extends out around the Gas Giant. \nWhile the limited spread means that avoiding the field requires a detour, \na vessel with cause to pass directly through the ring must make a Challenging (+0) Pilot (Space Craft)+Manoeuvrability Test as if passing through an Asteroid Field, as described on pages 226–227 of the ROGUE TRADER Core Rulebook. \nMultiple instances of this Orbital Feature increase the size of the rings. \nTests to pass through safely suffer a –10 penalty for each additional instance of this Orbital Feature.")
        elif featureRoll <= 50:
            orbitalFeature.append("Planetary Rings (Dust)")
            orbitalFeatDESC.append("A wide ring of fine particles encircles the gas giant. \nWhile the limited spread prevents it from becoming a navigational hazard like a true dust cloud or nebula, \nany Tests using the ship’s auger arrays on a target within, on, or directly through the ring are two steps more difficult. \nMultiple instances of this Orbital Feature increase the size of the existing Planetary Rings instead of adding extra sets of Rings. \nIncrease the penalty to use augers through or within the Rings by an additional –5 for every two additional instances of this Feature")
        elif featureRoll <= 85:
            orbitalFeature.append("Lesser Moon")
            rollMin = random.randint(1,10)
            if rollMin >= 6:
                #Roll 5d10+5 for abundance
                minRec = mineralResource()
                abundRoll = random.randint(1,10)+random.randint(1,10)+random.randint(1,10)+random.randint(1,10)+random.randint(1,10)+5
                abundance = resourceAbundance(abundRoll)
            else:
                minRec = "None :("
                abundance = "None no Minerals"
            orbitalFeatDESC.append("An orbital body somewhere between an extremely large asteroid and a very small moon orbits the Planet. \nIt has its own extremely limited gravity well, allowing low-gravity travel across the surface, as described on page 269 of the ROGUE TRADER Core Rulebook. \nWhen generating a Lesser Moon, roll 1d10; on a result of 6 or higher, it houses sufficient mineral wealth to count as a Resource. \nRoll once on Table 1–20: Mineral Resources and determine its Abundance by rolling 5d10+5." + "\n\nMineral Resource of moon: "+ minRec + "\n\nAbundance of Resource on moon: " + abundance)
        else:
            orbitalFeature.append("Moon")
            orbitalFeature.append("A true moon is generated as a Planet, using the rules for Planet Creation (see page 19). \nUnder normal circumstances, a moon cannot have a higher Planetary Body than the world around which it orbits. \nIn addition, a moon never generates its own Orbital Features.")
            #little confused to how this works with gas just letting all values go through
            moonCreation(body,mLocation)
        orbitRoll -= 1
    #combines orbit and features ?
    combinedOrbitFeatures = [item for pair in zip(orbitalFeature, orbitalFeatDESC) for item in pair]
    combinedOrbitFeatures += orbitalFeature[len(orbitalFeatDESC):] + orbitalFeatDESC[len(orbitalFeature):]
    return print("\nBody: "+ body+ "\nBody Description: "+ bodyDesc + "\n\nGravity: "+ gravity + "\n\nGravity Description: "+ gravDesc + "\n\nOrbital Feature: ".join(combinedOrbitFeatures))



#used to generate mineral Resources
def mineralResource():
    minerRoll = random.randint(1,10)
    switch = {
        1: "Industrial Metal",
        2: "Industrial Metal",
        3: "Industrial Metal",
        4: "Industrial Metal",
        5: "Ornamental",
        6: "Ornamental",
        7: "Ornamental",
        8: "Radioactive",
        9: "Radioactive",
        10:"Exotic Metals",
    }
    return switch.get(minerRoll)

#used to generate resource abundance
def resourceAbundance(roll):
    if roll <= 15:
        abundance = "Minimal"
        abunDesc = "There are trace amounts of the resource in question, but not enough to sustain an ongoing extraction operation such as a dedicated mining colony. \nShort-term operations are likely to have the best returns upon investment."
    elif roll <= 40: 
        abundance = "Limited"
        abunDesc = "A modest but worthwhile supply of the Resource is present, \nand a sustained operation could focus on exploiting this resource alone for several years before needing to find other sources of income."
    elif roll <= 65:
        abundance = "Sustainable"
        abunDesc = "Extensive reserves exist to ensure that the Resource remains a viable source of income for some time."
    elif roll <= 85:
        abundance = "Significant"
        abunDesc = "The Resource is both rich and accessible, allowing for a wide variety of approaches in making use of it."
    elif roll <= 98:
        abundance = "Major"
        abunDesc = " The Resource’s potential value is vast, both as an immediate commodity and as a long term reserve. \nUnfortunately, significant investment is likely to be required to properly benefit from that potential, and there is enough of a supply to encourage competition."
    else:
        abundance = "Plentiful"
        abunDesc = "The reserves of this Resource are seem limitless. \nThough deposits of this value have been exhausted by the Imperium before, \nit would take at least a decade to deplete this resource, barring the most aggressive efforts."
    return "Abundance Rating: " + abundance + "\nAbundance Description: " + abunDesc



def main():
    #print(starType())
    #proof that sytemelements works for now
    #print(innerCauldronElements(starType()))
    #print(primaryBioshereElements(starType()))
    #print(outerReachesElements(starType()))
    #print(systemElements(starType()))
    #print(derelictStationOrigins())
    #print(starshipGraveyardOrigins())
    #Location = "Inner Cauldron"
    #Location = "Outer Reaches"
    Location = "CENTER" 
    print(rockPlanetCreation(Location))
    #print(moonCreation("Small",Location))
    #print(mineralResource())
    #print(resourceAbundance(15))
    #print(gasPlanetCreation(Location))



if __name__ == "__main__":
    main()

