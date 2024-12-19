# main.py will import in everything else we create to
# generate the random star system and then display it in the UI
# 
# 
#
#

#list of imports
import random
import numpy
from generation import amountOfSystemFeatures, systemFeatures, starType, systemElements
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
        system_features = systemFeatures()
        system_Elements = systemElements(startype) 
        window.updateLabel(startype)  #update the UI label
        window.updateSidebarStars(startype) #this updates the sidebar
        window.updateSidebarSystemFeatures(system_features)
        window.updateSystemElements(system_Elements)
        #window.triggerPlanetGen(system_Elements)
        
    #create the UI and pass the callback to the button
    window = StarGeneratorUI(generate)
    window.setThreeFourthsScreenSize()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()