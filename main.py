# main.py will import in everything else we create to
# generate the random star system and then display it in the UI
# 
# 
#
#

#list of imports
import random
import numpy
from generation import amountOfSystemFeatures, systemFeatures, starType, systemElements,allSFeatures
from PyQt5.QtWidgets import QApplication
from UI import StarGeneratorUI
import sys

def main():
    #sets up UI basically
    app = QApplication(sys.argv)

    #UI DEBUGGING STUFF HERE
    #-----------------------
    def generate():
        startype = starType()  #call the starType function from generation.py
        system_features = allSFeatures()#call the all system features from generation.py
        system_Elements = systemElements(startype) #call the systemElements function form generation.py
        window.updateLabel(startype)  #update the UI label
        window.updateSidebarStars(startype) #this updates the sidebar
        window.updateSidebarSystemFeatures(system_features) #This adds system features
        window.updateSystemElements(system_Elements) #this adds system elements
        window.triggerPlanetGen(system_Elements) #this adds planet generation
        
    #create the UI and pass the callback to the button
    window = StarGeneratorUI(generate)
    window.setThreeFourthsScreenSize()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()