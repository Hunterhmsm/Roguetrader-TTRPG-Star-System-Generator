#does all the random generation for the system features, star type, etc

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
    
    systemfeature = random.randint(1, 10)
    feature = ""

    if systemfeature == 1:
        feature = "Bountiful"
    elif systemfeature == 2:
        feature = "Gravity_Tides"
    elif systemfeature == 3:
        feature = "Haven"
    elif systemfeature == 4:
        feature = "Ill_Omened"
    elif systemfeature == 5:
        feature = "Pirate_Den"
    elif systemfeature == 6:
        feature = "Ruined_Empire"
    elif systemfeature == 7:
        feature = "Starfarers"
    elif systemfeature == 8:
        feature = "Stellar_Anomoly"
    elif systemfeature == 9:
        feature = "Warp_Stasis"
    elif systemfeature == 10:
        feature = "Warp_Turbulence"
    return feature

#generates the star type
def starType():

    star = random.randint(1,10)
    type = ""

    if star == 1:
        type = "Mighty"
    elif 2 <=  star <= 4:
        type = "Vigorous"
    elif 5 <= star <= 7:
        type = "Luminous"
    elif star == 8:
        type = "Dull"
    elif star == 9:
        type = "Anomalous"
    elif star == 10:
        type = "Binary"
    
    return type



    #DEBUGGING

def main():
    print(starType())

if __name__ == "__main__":
    main()

