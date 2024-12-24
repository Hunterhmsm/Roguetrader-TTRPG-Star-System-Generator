from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QListWidget, QSplitter, QListWidgetItem, QApplication, QScrollArea
from PyQt5.QtCore import Qt
from generation import rockPlanetCreation, gasPlanetCreation, moonCreation

class StarGeneratorUI(QWidget):
    def __init__(self, generate_callback):
        super().__init__()
        
        # Set up the window
        self.setWindowTitle("Star Type Generator")
        layout = QVBoxLayout()

        # Background color
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
            }
        """)

        # Setting up the sidebar with a scroll area
        self.sidebar_scroll = QScrollArea()
        self.sidebar_scroll.setWidgetResizable(True)
        self.sidebar_scroll.setStyleSheet("background-color: #2E3440; color: white;")

        # Sidebar content container
        self.sidebar_content = QWidget()
        self.sidebar_layout = QVBoxLayout(self.sidebar_content)

        # Add default text and labels
        self.sidebar_label_systemfeatures = QLabel("")
        self.sidebar_label_star = QLabel("")
        self.sidebar_label_systemfeatures.setAlignment(Qt.AlignCenter)
        self.sidebar_label_star.setAlignment(Qt.AlignCenter)
        self.sidebar_layout.addWidget(self.sidebar_label_systemfeatures)
        self.sidebar_layout.addWidget(self.sidebar_label_star)

        # Add stretch to fill extra space
        self.sidebar_layout.addStretch()

        # Set the sidebar content widget to the scroll area
        self.sidebar_scroll.setWidget(self.sidebar_content)
        # Match previous design width
        # This may need to change
        self.sidebar_scroll.setFixedWidth(200)  
        
        # Add the scroll area to the main layout
        layout.addWidget(self.sidebar_scroll)

        # Custom style labels
        self.label = QLabel("Click 'Generate' to get a star type", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                color: #f0f0f0;
                font-size: 16px;
                font-weight: bold;
            }
        """)

        self.button = QPushButton("Generate", self)
        self.button.clicked.connect(generate_callback)  # Connect button to callback
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #4caf50;
                color: white;
                border-radius: 10px;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #388e3c;
            }
        """)

        # Add widgets to the layout
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)


    #for updating labels
    def updateLabel(self, text):
        """Update the label with the generated star type."""
        self.label.setText(f"Generated Star Type: {text}")

    #puts it in fullscreen
    def showFullScreenMode(self):
        """Launch the UI in fullscreen mode."""
        self.showFullScreen()

    #sets it to 3/4ths scren size
    def setThreeFourthsScreenSize(self):
        """Resize the window to take up 3/4ths of the screen."""
        screen = QApplication.primaryScreen().geometry()
        screen_width, screen_height = screen.width(), screen.height()

        #calculate 3/4ths of the screen size
        width = int(screen_width * 0.75)
        height = int(screen_height * 0.75)

        #center the window on the screen
        left = (screen_width - width) // 2
        top = (screen_height - height) // 2

        #set the window size and position
        self.setGeometry(left, top, width, height)
    
    def setOneHalfScreenSize(self):
        """Resize the window to take up 1/2 of the screen."""
        screen = QApplication.primaryScreen().geometry()
        screen_width, screen_height = screen.width(), screen.height()

        #calculate 1/2 of the screen size
        width = int(screen_width * 0.5)
        height = int(screen_height * 0.5)

        #center the window
        left = (screen_width - width) // 2
        top = (screen_height - height) // 2

        #set window size and pos
        self.setGeometry(left, top, width, height)

    def updateSidebarStars(self, star):
        self.sidebar_label_star.setText(star)
    
    def updateSidebarSystemFeatures(self, features):
        for index in reversed(range(self.sidebar_layout.count())):
            widget = self.sidebar_layout.itemAt(index).widget()
            if widget is not None and widget.objectName().startswith("feature_label_"):
                widget.deleteLater()

        for index, feature in enumerate(features):
            label = QLabel(feature)
            #THIS IS CHANGED TO BE VISABLE
            #AlignCenter -> AlignLeft
            label.setAlignment(Qt.AlignLeft)
            label.setStyleSheet("color: white; font-size: 12px;")
            label.setObjectName(f"feature_label_{index}")
            self.sidebar_layout.addWidget(label)
        self.sidebar_layout.addStretch()
        
   
    # Adding the method to the StarGeneratorUI class
    #Probably should change to make look more like the other sidebar elements
    def updateSystemElements(self, systemElements):
        """Updates the sidebar with the system elements based on the star type."""
        InnerCauldronElements, PrimaryBiosphereElements, OuterFeaturesElements = systemElements

        # Clear existing sidebar system elements
        for index in reversed(range(self.sidebar_layout.count())):
            widget = self.sidebar_layout.itemAt(index).widget()
            if widget is not None and widget.objectName().startswith("element_label_"):
                widget.deleteLater()
        # Clear existing sidebar of names of system elements
        # without this it will keep the names of these elements for some reason.    
        for index in reversed(range(self.sidebar_layout.count())):
            widget = self.sidebar_layout.itemAt(index).widget()
            if widget is not None and widget.objectName().startswith("zone_label_"):
                widget.deleteLater()
        #List to count the zones for deletion later
        self.zone_labels = []

        # Update sidebar with new elements
        elements_dict = {
            "Inner Cauldron": InnerCauldronElements,
            "Primary Biosphere": PrimaryBiosphereElements,
            "Outer Features": OuterFeaturesElements,
        }
        #Loops and displays each element based on the zone that they are attached to.
        for zone, elements in elements_dict.items():
            label_zone = QLabel(f"{zone}:")
            label_zone.setAlignment(Qt.AlignLeft)
            label_zone.setStyleSheet("color: #FFD700; font-size: 14px; font-weight: bold;")
            label_zone.setObjectName(f"zone_label_{zone.replace(' ', '_')}")
            self.sidebar_layout.addWidget(label_zone)
            #Line Below appends them to make sure this gets deleted when 
            #a new generation takes placce
            self.zone_labels.append(label_zone)
            for element in elements:
                label_element = QLabel(f"  - {element}")
                label_element.setAlignment(Qt.AlignLeft)
                label_element.setStyleSheet("color: white; font-size: 12px;")
                label_element.setObjectName(f"element_label_{element}")
                self.sidebar_layout.addWidget(label_element)
        self.sidebar_layout.addStretch()

    
    
    # Triggers planet generation whenever a planet shows up
    # Moon triggers are built into update planet and update GasGiant
    # may need to make this look better or add compressable segments 
    def triggerPlanetGen(self, systemElements):
        """Triggers updatePlanetGen when 'Planet' is found in any of the elements."""
        #takes system elements and makes them into variables
        InnerCauldronElements, PrimaryBiosphereElements, OuterFeaturesElements = systemElements
        
        
        #puts variables into a readable list
        elements_dict = {
            "Inner Cauldron": InnerCauldronElements,
            "Primary Biosphere": PrimaryBiosphereElements,
            "Outer Features": OuterFeaturesElements,
        }
        #REMOVES EVERTHING RELATED TO PLANET GENERATION
        #Removes Body, Gravity, ... labels gets run evertime so it should be done here not in update planet gen
        for index in reversed(range(self.sidebar_layout.count())):
            widget = self.sidebar_layout.itemAt(index).widget()
            if widget is not None and widget.objectName().startswith("part_label_"):
                widget.deleteLater()
        for index in reversed(range(self.sidebar_layout.count())):
            widget = self.sidebar_layout.itemAt(index).widget()
            if widget is not None and widget.objectName().startswith("info_label_"):
                widget.deleteLater()
        for index in reversed(range(self.sidebar_layout.count())):
            widget = self.sidebar_layout.itemAt(index).widget()
            if widget is not None and widget.objectName().startswith("gas_label_"):
                widget.deleteLater()
        for index in reversed(range(self.sidebar_layout.count())):
            widget = self.sidebar_layout.itemAt(index).widget()
            if widget is not None and widget.objectName().startswith("bits_label_"):
                widget.deleteLater()
    
        # Loop through each zone and its elements
        for zone, elements in elements_dict.items():
            # Create and store zone label
            label_zone = QLabel(f"{zone}:")
            self.zone_labels.append(label_zone)
        
            # Loop through elements in the current zone
            for element in elements:
                # Check if the element is "Planet"
                if element == "Planet":
                     # Inform the user which planet is being generated
                    print(f"Generating a planet for the {zone} zone...")
                
                    # Optionally display this in the UI
                    label_info = QLabel(f"Generating a planet for the {zone} zone...")
                    label_info.setAlignment(Qt.AlignLeft)
                    label_info.setStyleSheet("color: #FFD700; font-size: 12px;")
                    label_info.setObjectName(f"info_label_{zone.replace(' ', '_')}")
                    self.sidebar_layout.addWidget(label_info)

                    # Call the updatePlanetGen to generate the planet
                    self.updatePlanetGen(zone)
                if element == "Gas Gaint":
                     # Inform the user which planet is being generated
                    print(f"Generating a planet for the {zone} zone...")
                
                    # Optionally display this in the UI
                    label_info = QLabel(f"Generating a Gas Giant for the {zone} zone...")
                    label_info.setAlignment(Qt.AlignLeft)
                    label_info.setStyleSheet("color: #FFD700; font-size: 12px;")
                    label_info.setObjectName(f"info_label_{zone.replace(' ', '_')}")
                    self.sidebar_layout.addWidget(label_info)

                    # Call the updatePlanetGen to generate the planet
                    self.updateGasGiant(zone)    
                    
                    
    
    #Generates said planet
    #If system Elements generates a planet
    def updatePlanetGen(self, zone):
        #Debugging line
        print(f"Planet found in the {zone}!")
        #Grabs variables from planet generation
        body, gravity, combinedOrbitFeatures, Atmosphere, atmosphericComp, climate, habitability, Landmasses, LandDesc, moons = rockPlanetCreation(zone)
        
        #Commented section below not nessicary just in case something bricks first segment pervented
        #Systemelements from showing up and secound segment is taken care of in trigger planet gen now
        # Clear existing sidebar planet elements
        #for index in reversed(range(self.sidebar_layout.count())):
            #widget = self.sidebar_layout.itemAt(index).widget()
            #if widget is not None and widget.objectName().startswith("element_label_"):
                #widget.deleteLater()
                
                
        # Clear existing sidebar of names of system elements
        # without this it will keep the names of these elements for some reason.    
        
        #for index in reversed(range(self.sidebar_layout.count())):
            #widget = self.sidebar_layout.itemAt(index).widget()
            #if widget is not None and widget.objectName().startswith("part_label_"):
                #widget.deleteLater()
        
        #List to count the parts of a planet for deletion later
        self.part_labels = []
        
         
            
        #puts variables into a list
        planet_parts = {
            "Body": body,
            "Gravity": gravity,
            "Orbital Features": combinedOrbitFeatures,
            "Atmoshere": Atmosphere,
            "Atomsheric Composition": atmosphericComp,
            "Climate": climate,
            "Habitability": habitability,
            "Landmasses": Landmasses,
            "Landmass Description": LandDesc,
        }
        
        #This makes it so if it is a single item it doesn't get turned into a list
        for part, elements in planet_parts.items():
            if not isinstance(elements, list):  # If it's not a list, make it one
                elements = [str(elements)]
            else:
                elements = [str(element) for element in elements]
            #Setting up yellow bolded text to show part
            label_part = QLabel(f"{part}:")
            label_part.setAlignment(Qt.AlignLeft)
            label_part.setStyleSheet("color: #FFD700; font-size: 14px; font-weight: bold;")
            label_part.setObjectName(f"part_label_{part.replace(' ', '_')}")
            self.sidebar_layout.addWidget(label_part)
            #Line Below appends them to make sure this gets deleted when 
            #a new generation takes placce
            self.part_labels.append(label_part)
            #Prints the list of elements where they are suppost to be in corilation to the yellow bolds
            for element in elements:
                label_element = QLabel(f"  - {element}")
                label_element.setAlignment(Qt.AlignLeft)
                label_element.setStyleSheet("color: white; font-size: 12px;")
                label_element.setObjectName(f"element_label_{element}")
                self.sidebar_layout.addWidget(label_element)
        #used to generate moons based on how many moons are attached to the planet
        while moons >= 1:
           
            # Inform the user which planet is being generated
            print(f"Generating a Moon for the Planet in the {zone} zone...")
                
            # Optionally display this in the UI
            label_info = QLabel(f"Generating a Moon for the Planet in the {zone} zone...")
            label_info.setAlignment(Qt.AlignLeft)
            label_info.setStyleSheet("color: #FFD700; font-size: 12px;")
            label_info.setObjectName(f"info_label_{zone.replace(' ', '_')}")
            self.sidebar_layout.addWidget(label_info)
            self.updateMOONS(body, zone) 
            moons -=1
        self.sidebar_layout.addStretch()
    
    #Generates a Gas Giant
    def updateGasGiant(self, zone):
        #Debug line
        print(f"Gas Giant found in the {zone}!")
        #Grabs variables from creating gas giant
        body, gravity, combinedOrbitFeatures, moons = gasPlanetCreation(zone)
        
        #list so it can be deleted on new gen
        self.gas_labels = []
        
        #makes variables into readable list
        gasGiant_parts = {
            "Body": body,
            "Gravity": gravity,
            "Orbital Features": combinedOrbitFeatures
        }
        
        #This makes it so if it is a single item it doesn't get turned into a list
        for gas, elements in gasGiant_parts.items():
            if not isinstance(elements, list):  # If it's not a list, make it one
                elements = [str(elements)]
            else:
                elements = [str(element) for element in elements]
                
            label_gas = QLabel(f"{gas}:")
            label_gas.setAlignment(Qt.AlignLeft)
            label_gas.setStyleSheet("color: #FFD700; font-size: 14px; font-weight: bold;")
            label_gas.setObjectName(f"gas_label_{gas.replace(' ', '_')}")
            self.sidebar_layout.addWidget(label_gas)
            #Line Below appends them to make sure this gets deleted when 
            #a new generation takes placce
            self.gas_labels.append(label_gas)
            #Prints the list of elements where they are suppost to be in corilation to the yellow bolds
            for element in elements:
                label_element = QLabel(f"  - {element}")
                label_element.setAlignment(Qt.AlignLeft)
                label_element.setStyleSheet("color: white; font-size: 12px;")
                label_element.setObjectName(f"element_label_{element}")
                self.sidebar_layout.addWidget(label_element)
        #used to generate moons based on how many moons are attached to the planet
        while moons >= 1:
            
            # Inform the user which planet is being generated
            print(f"Generating a Moon for the Gas Gaint in the {zone} zone...")
                
            # Optionally display this in the UI
            label_info = QLabel(f"Generating a Moon for the Gas Gaint in the {zone} zone...")
            label_info.setAlignment(Qt.AlignLeft)
            label_info.setStyleSheet("color: #FFD700; font-size: 12px;")
            label_info.setObjectName(f"info_label_{zone.replace(' ', '_')}")
            self.sidebar_layout.addWidget(label_info)
            self.updateMOONS(body, zone)
            
            moons -=1
        self.sidebar_layout.addStretch()
        
    #Generates a Moon
    def updateMOONS(self, pbody, zone):
        #debugline
        print(f'Oh a moon orbiting planet in the {zone}! AMAZING')
        #Grabs all variables from a generated moon
        body, gravity, Atmosphere, atmosphericComp, climate, habitability, Landmasses, LandDesc = moonCreation(pbody, zone)
        self.bits_labels = []
        
        #Seperates the variables into different parts
        moon_parts = {
            "Body": body,
            "Gravity": gravity,
            "Atmoshere": Atmosphere,
            "Atomsheric Composition": atmosphericComp,
            "Climate": climate,
            "Habitability": habitability,
            "Landmasses": Landmasses,
            "Landmass Description": LandDesc,
        }
        
        #This makes it so if it is a single item it doesn't get turned into a list
        for bits, elements in moon_parts.items():
            if not isinstance(elements, list):  # If it's not a list, make it one
                elements = [str(elements)]
            else:
                elements = [str(element) for element in elements]

            label_bits = QLabel(f"{bits}:")
            label_bits.setAlignment(Qt.AlignLeft)
            label_bits.setStyleSheet("color: #FFD700; font-size: 14px; font-weight: bold;")
            label_bits.setObjectName(f"bits_label_{bits.replace(' ', '_')}")
            self.sidebar_layout.addWidget(label_bits)
            #Line Below appends them to make sure this gets deleted when 
            #a new generation takes placce
            self.bits_labels.append(label_bits)
            #Prints the list of elements where they are suppost to be in corilation to the yellow bolds
            for element in elements:
                label_element = QLabel(f"  - {element}")
                label_element.setAlignment(Qt.AlignLeft)
                label_element.setStyleSheet("color: white; font-size: 12px;")
                label_element.setObjectName(f"element_label_{element}")
                self.sidebar_layout.addWidget(label_element)
        self.sidebar_layout.addStretch()
        
        
    # Maybe works need more testing probably should be used in the future
    def clearSidebar(self):
        """Removes all widgets from the sidebar layout."""
        for index in reversed(range(self.sidebar_layout.count())):
            widget = self.sidebar_layout.itemAt(index).widget()
            if widget is not None:
                widget.deleteLater()
