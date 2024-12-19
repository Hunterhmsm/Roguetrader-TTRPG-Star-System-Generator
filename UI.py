from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QListWidget, QSplitter, QListWidgetItem, QApplication
from PyQt5.QtCore import Qt
from generation import rockPlanetCreation, gasPlanetCreation, moonCreation

class StarGeneratorUI(QWidget):
    def __init__(self, generate_callback):
        super().__init__()
        
        #set up the window
        self.setWindowTitle("Star Type Generator")
        layout = QVBoxLayout()

        #background color
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
            }
        """)

        #set up the layout and widgets
        layout = QVBoxLayout()


        #setting up the sidebar
        sidebar = QWidget()
        sidebar.setFixedWidth(200)
        self.sidebar_layout = QVBoxLayout(sidebar)
        
        #default text
        #and sidebar labels
        self.sidebar_label_systemfeatures = QLabel("")
        self.sidebar_label_star = QLabel("")
        self.sidebar_label_systemfeatures.setAlignment(Qt.AlignCenter)
        self.sidebar_label_star.setAlignment(Qt.AlignCenter)
        self.sidebar_layout.addWidget(self.sidebar_label_systemfeatures)
        self.sidebar_layout.addWidget(self.sidebar_label_star)

        self.sidebar_layout.addStretch()
        sidebar.setStyleSheet("background-color: #2E3440; color: white;")
        layout.addWidget(sidebar)

        #custom style labels
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
        self.button.clicked.connect(generate_callback)  #connect button to callback IMPORTANT
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

        #add widgets to the layout
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
            label.setAlignment(Qt.AlignCenter)
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
    # Should add trigger for gas giants as well as moons in the future
    # DONT KNOW IF WE WILL NEED A Trigger moon generator as well
    def triggerPlanetGen(self, systemElements):
        """Triggers updatePlanetGen when 'Planet' is found in any of the elements."""
        InnerCauldronElements, PrimaryBiosphereElements, OuterFeaturesElements = systemElements
    
        elements_dict = {
            "Inner Cauldron": InnerCauldronElements,
            "Primary Biosphere": PrimaryBiosphereElements,
            "Outer Features": OuterFeaturesElements,
        }
    
        # Loop through each zone and its elements
        for zone, elements in elements_dict.items():
            # Create and store zone label
            label_zone = QLabel(f"{zone}:")
            self.zone_labels.append(label_zone)
        
            # Loop through elements in the current zone
            for element in elements:
                # Check if the element is "Planet"
                if element == "Planet":
                    # Call the updatePlanetGen when "Planet" is found
                    self.updatePlanetGen(zone)
    
    #Generates said planet suffering from same problem as updateSidebarSystemFeatures
    #This is because the strings are being split apart into individual charactors
    #Becuase of this and lack of scrollbar you are unable to make another generation
    #If system Elements generates a planet
    def updatePlanetGen(self, zone):
        print(f"Planet found in the {zone}!")
        body, gravity, combinedOrbitFeatures, Atmosphere, atmosphericComp, climate, habitability, Landmasses, LandDesc = rockPlanetCreation(zone)
        
        # Clear existing sidebar planet elements
        for index in reversed(range(self.sidebar_layout.count())):
            widget = self.sidebar_layout.itemAt(index).widget()
            if widget is not None and widget.objectName().startswith("element_label_"):
                widget.deleteLater()
        # Clear existing sidebar of names of system elements
        # without this it will keep the names of these elements for some reason.    
        for index in reversed(range(self.sidebar_layout.count())):
            widget = self.sidebar_layout.itemAt(index).widget()
            if widget is not None and widget.objectName().startswith("part_label_"):
                widget.deleteLater()
        #List to count the parts of a planet for deletion later
        self.part_labels = []
        

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
        
        
        for part, elements in planet_parts.items():
            label_part = QLabel(f"{part}:")
            label_part.setAlignment(Qt.AlignLeft)
            label_part.setStyleSheet("color: #FFD700; font-size: 14px; font-weight: bold;")
            label_part.setObjectName(f"part_label_{part.replace(' ', '_')}")
            self.sidebar_layout.addWidget(label_part)
            #Line Below appends them to make sure this gets deleted when 
            #a new generation takes placce
            self.part_labels.append(label_part)
            for element in elements:
                label_element = QLabel(f"  - {element}")
                label_element.setAlignment(Qt.AlignLeft)
                label_element.setStyleSheet("color: white; font-size: 12px;")
                label_element.setObjectName(f"element_label_{element}")
                self.sidebar_layout.addWidget(label_element)
        self.sidebar_layout.addStretch()
    
    # was used to test didnt work as intended
    def clearSidebar(self):
        """Removes all widgets from the sidebar layout."""
        for index in reversed(range(self.sidebar_layout.count())):
            widget = self.sidebar_layout.itemAt(index).widget()
            if widget is not None:
                widget.deleteLater()
