from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, 
                             QListWidget, QSplitter, QListWidgetItem, QApplication, 
                             QScrollArea, QFrame, QSizePolicy)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QCursor
from generation import rockPlanetCreation, gasPlanetCreation, moonCreation
# a clickable label that can trigger planet generation
class ClickableLabel(QLabel):
    clicked = pyqtSignal(str, str)  # element_type, zone
    
    def __init__(self, text, element_type=None, zone=None, parent=None):
        super().__init__(text, parent)
        self.element_type = element_type
        self.zone = zone
        self.setWordWrap(True)
        
        if element_type in ["Planet", "Gas Gaint"]:
            self.setCursor(QCursor(Qt.PointingHandCursor))
            self.setStyleSheet("""
                QLabel {
                    color: #88C0D0;
                    font-size: 11px;
                    padding: 0px 0px 0px 10px;
                    margin: 0px;
                }
                QLabel:hover {
                    color: #81A1C1;
                    text-decoration: underline;
                }
            """)
        else:
            self.setStyleSheet("""
                QLabel {
                    color: white;
                    font-size: 11px;
                    padding: 0px 0px 0px 10px;
                    margin: 0px;
                }
            """)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.element_type in ["Planet", "Gas Gaint"]:
            self.clicked.emit(self.element_type, self.zone)
        super().mousePressEvent(event)

# a custom widget that combines a planet header label with a close button
class PlanetHeaderWidget(QWidget):
    close_clicked = pyqtSignal(str)  # planet_id
    
    def __init__(self, title, planet_id, parent=None):
        super().__init__(parent)
        self.planet_id = planet_id
        
        # create horizontal layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        
        # create the title label
        self.title_label = QLabel(title)
        self.title_label.setStyleSheet("""
            QLabel {
                color: #FFD700;
                font-size: 13px;
                font-weight: bold;
                padding: 2px 0px 0px 5px;
                margin: 0px;
            }
        """)
        
        # create the close button
        self.close_button = QPushButton("✕")
        self.close_button.setFixedSize(20, 20)
        self.close_button.clicked.connect(lambda: self.close_clicked.emit(self.planet_id))
        self.close_button.setStyleSheet("""
            QPushButton {
                background-color: #BF616A;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #D08770;
            }
            QPushButton:pressed {
                background-color: #A3515A;
            }
        """)
        self.close_button.setToolTip("Remove this planet's details")
        
        # add widgets to layout
        layout.addWidget(self.title_label)
        layout.addStretch()  # Push the close button to the right
        layout.addWidget(self.close_button)

# a collapsible section widget with a title and content area
class CollapsibleSection(QFrame):
    
    def __init__(self, title="", parent=None):
        super(CollapsibleSection, self).__init__(parent)
        
        self.toggle_button = QPushButton(title)
        self.toggle_button.setCheckable(True)
        self.toggle_button.setChecked(False)  # start collapsed
        self.toggle_button.clicked.connect(self.on_toggle)
        
        # style the toggle button
        self.toggle_button.setStyleSheet("""
            QPushButton {
                background-color: #3B4252;
                color: #ECEFF4;
                border: none;
                padding: 8px;
                text-align: left;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #434C5E;
            }
            QPushButton:checked {
                background-color: #5E81AC;
            }
        """)
        
        # content area
        self.content_area = QFrame()
        self.content_area.setStyleSheet("""
            QFrame {
                background-color: #2E3440;
                border: none;
                padding: 0px;
            }
        """)
        self.content_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.content_area.hide()  # start hidden
        
        # layout for content
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(1)
        
        # main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.toggle_button)
        main_layout.addWidget(self.content_area)
        
    # toggle the visibility of the content area
    def on_toggle(self):
        if self.toggle_button.isChecked():
            self.content_area.show()
            self.toggle_button.setText(f"▼ {self.toggle_button.text().replace('▶ ', '').replace('▼ ', '')}")
        else:
            self.content_area.hide()
            self.toggle_button.setText(f"▶ {self.toggle_button.text().replace('▶ ', '').replace('▼ ', '')}")
    
    # add a widget to the content area
    def add_content_widget(self, widget):
        self.content_layout.addWidget(widget)
    
    # remove all widgets from the content area
    def clear_content(self):
        while self.content_layout.count():
            child = self.content_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    # set the expanded state programmatically
    def set_expanded(self, expanded):
        self.toggle_button.setChecked(expanded)
        self.on_toggle()


class StarGeneratorUI(QWidget):
    def __init__(self, generate_callback):
        super().__init__()
        
        # set up the window
        self.setWindowTitle("Star Type Generator")
        layout = QVBoxLayout()

        # background color
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
            }
        """)

        # setting up the sidebar with a scroll area
        self.sidebar_scroll = QScrollArea()
        self.sidebar_scroll.setWidgetResizable(True)
        self.sidebar_scroll.setStyleSheet("background-color: #2E3440; color: white;")

        # sidebar content container
        self.sidebar_content = QWidget()
        self.sidebar_layout = QVBoxLayout(self.sidebar_content)
        self.sidebar_layout.setSpacing(2)

        # initialize collapsible sections
        self.star_section = CollapsibleSection("▶ Star Information")
        self.features_section = CollapsibleSection("▶ System Features")
        self.elements_section = CollapsibleSection("▶ System Elements")
        self.planets_section = CollapsibleSection("▶ Planet Details")
        
        # store planet data for on-demand generation
        self.planet_data_cache = {}
        self.planet_counter = 0
        self.planet_widgets = {}  # track widgets for each planet for removal
        
        # add sections to sidebar
        self.sidebar_layout.addWidget(self.star_section)
        self.sidebar_layout.addWidget(self.features_section)
        self.sidebar_layout.addWidget(self.elements_section)
        self.sidebar_layout.addWidget(self.planets_section)
        
        # add stretch to fill extra space
        self.sidebar_layout.addStretch()

        # set the sidebar content widget to the scroll area
        self.sidebar_scroll.setWidget(self.sidebar_content)
        self.sidebar_scroll.setFixedWidth(400)  # width of the sidebar
        
        # add the scroll area to the main layout
        layout.addWidget(self.sidebar_scroll)

        # custom style labels
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
        self.button.clicked.connect(generate_callback)  # connect button to callback
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

        # add widgets to the layout
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    # create a styled label for information display with proper indentation
    def create_info_label(self, text, is_header=False, indent_level=0):
        label = QLabel(text)
        label.setAlignment(Qt.AlignLeft)
        label.setWordWrap(True)
        
        # calculate padding based on indent level and bullet alignment
        base_padding = 5  # base padding from left edge
        bullet_width = 10  # space for bullet character "• "
        indent_spacing = 15  # additional spacing per indent level
        
        if is_header:
            # headers use base padding plus indent spacing
            left_padding = base_padding + (indent_level * indent_spacing)
            label.setStyleSheet(f"""
                QLabel {{
                    color: #FFD700;
                    font-size: 13px;
                    font-weight: bold;
                    padding: 2px 0px 0px {left_padding}px;
                    margin: 0px;
                }}
            """)
        else:
            # for bullet points, use base padding + indent + bullet space
            # for non-bullet text, align with where bullet text would start
            if text.strip().startswith('•'):
                left_padding = base_padding + (indent_level * indent_spacing)
            else:
                # align with bullet text (after the bullet symbol)
                left_padding = base_padding + (indent_level * indent_spacing) + bullet_width
            
            label.setStyleSheet(f"""
                QLabel {{
                    color: white;
                    font-size: 11px;
                    padding: 0px 0px 0px {left_padding}px;
                    margin: 0px;
                }}
            """)
        return label

    # update the label with the generated star type
    def updateLabel(self, text):
        self.label.setText(f"Generated Star Type: {text}")

    # launch the UI in fullscreen mode
    def showFullScreenMode(self):
        self.showFullScreen()

    # resize the window to take up 3/4ths of the screen
    def setThreeFourthsScreenSize(self):
        screen = QApplication.primaryScreen().geometry()
        screen_width, screen_height = screen.width(), screen.height()

        width = int(screen_width * 0.75)
        height = int(screen_height * 0.75)

        left = (screen_width - width) // 2
        top = (screen_height - height) // 2

        self.setGeometry(left, top, width, height)

    # resize the window to take up half the screen
    def setOneHalfScreenSize(self):
        screen = QApplication.primaryScreen().geometry()
        screen_width, screen_height = screen.width(), screen.height()

        width = int(screen_width * 0.5)
        height = int(screen_height * 0.5)

        left = (screen_width - width) // 2
        top = (screen_height - height) // 2

        self.setGeometry(left, top, width, height)
    # update the star information section
    def updateSidebarStars(self, star):
        self.star_section.clear_content()
        star_label = self.create_info_label(f"Star Type: {star}")
        self.star_section.add_content_widget(star_label)
    
    # update the system features section
    def updateSidebarSystemFeatures(self, features):
        self.features_section.clear_content()
        
        for feature in features:
            feature_label = self.create_info_label(f"• {feature}")
            self.features_section.add_content_widget(feature_label)

    # update the system elements section with clickable planet labels
    def updateSystemElements(self, systemElements):
        InnerCauldronElements, PrimaryBiosphereElements, OuterFeaturesElements = systemElements
        
        self.elements_section.clear_content()
        self.planets_section.clear_content()
        self.planet_data_cache.clear()
        self.planet_widgets.clear()
        self.planet_counter = 0
        
        elements_dict = {
            "Inner Cauldron": InnerCauldronElements,
            "Primary Biosphere": PrimaryBiosphereElements,
            "Outer Features": OuterFeaturesElements,
        }
        
        for zone, elements in elements_dict.items():
            zone_label = self.create_info_label(f"{zone}:", is_header=True)
            self.elements_section.add_content_widget(zone_label)
            
            for element in elements:
                if element in ["Planet", "Gas Gaint"]:
                    # create clickable label for planets and gas giants
                    self.planet_counter += 1
                    planet_id = f"{element}_{zone}_{self.planet_counter}"
                    
                    clickable_label = ClickableLabel(f"• {element} (click for details)", element, zone)
                    clickable_label.clicked.connect(lambda elem_type, z, pid=planet_id: self.generate_planet_details(elem_type, z, pid))
                    self.elements_section.add_content_widget(clickable_label)
                    
                    # store the planet info for later generation
                    self.planet_data_cache[planet_id] = {
                        'type': element,
                        'zone': zone,
                        'generated': False
                    }
                else:
                    element_label = self.create_info_label(f"• {element}")
                    self.elements_section.add_content_widget(element_label)

    # generate planet details on demand
    def generate_planet_details(self, element_type, zone, planet_id):
        if planet_id in self.planet_data_cache and not self.planet_data_cache[planet_id]['generated']:
            print(f"Generating details for {element_type} in {zone}")
            
            # generate the planet data
            if element_type == "Planet":
                planet_data = self.generate_rock_planet_details(zone, planet_id)
            elif element_type == "Gas Gaint":
                planet_data = self.generate_gas_giant_details(zone, planet_id)
            
            # marrk as generated
            self.planet_data_cache[planet_id]['generated'] = True
            self.planet_data_cache[planet_id]['data'] = planet_data
            
            # expand the planets section to show the new details
            self.planets_section.set_expanded(True)
        else:
            print(f"Details for {planet_id} already generated or not found")

    # generate rock planet details and return the widgets created 
    def generate_rock_planet_details(self, zone, planet_id):
        body, gravity, combinedOrbitFeatures, Atmosphere, atmosphericComp, climate, habitability, Landmasses, LandDesc, moons = rockPlanetCreation(zone)
        
        # store widgets for this planet so we can remove them later
        self.planet_widgets[planet_id] = []
        
        # add header for this specific planet with close button
        planet_header_widget = PlanetHeaderWidget(f"Rock Planet in {zone} ({planet_id}):", planet_id)
        planet_header_widget.close_clicked.connect(self.remove_planet_details)
        self.planets_section.add_content_widget(planet_header_widget)
        self.planet_widgets[planet_id].append(planet_header_widget)
        
        planet_parts = {
            "Body": body,
            "Gravity": gravity,
            "Atmosphere": Atmosphere,
            "Atmospheric Composition": atmosphericComp,
            "Climate": climate,
            "Habitability": habitability,
            "Landmasses": Landmasses,
            "Landmass Description": LandDesc,
        }
        
        for part, elements in planet_parts.items():
            if not isinstance(elements, list):
                elements = [str(elements)]
            else:
                elements = [str(element) for element in elements]
            
            part_header = self.create_info_label(f"{part}:", is_header=True, indent_level=1)
            self.planets_section.add_content_widget(part_header)
            self.planet_widgets[planet_id].append(part_header)
            
            for element in elements:
                element_label = self.create_info_label(f"• {element}", indent_level=1)
                self.planets_section.add_content_widget(element_label)
                self.planet_widgets[planet_id].append(element_label)
        
        # handle Orbital Features separately
        if combinedOrbitFeatures:
            orbital_header = self.create_info_label("Orbital Features:", is_header=True, indent_level=1)
            self.planets_section.add_content_widget(orbital_header)
            self.planet_widgets[planet_id].append(orbital_header)
            
            for i in range(0, len(combinedOrbitFeatures), 2):
                if i < len(combinedOrbitFeatures):
                    feature_name = combinedOrbitFeatures[i]
                    feature_label = self.create_info_label(f"• {feature_name}", indent_level=1)
                    self.planets_section.add_content_widget(feature_label)
                    self.planet_widgets[planet_id].append(feature_label)
                    
                    if i + 1 < len(combinedOrbitFeatures):
                        description = combinedOrbitFeatures[i + 1]
                        if description and not description.startswith("\nOrbital Feature Description:"):
                            clean_desc = description.replace("\nOrbital Feature Description:", "").strip()
                            if clean_desc and clean_desc != "nothing":
                                desc_label = self.create_info_label(clean_desc, indent_level=1)
                                self.planets_section.add_content_widget(desc_label)
                                self.planet_widgets[planet_id].append(desc_label)
        
        # generate moons if any
        moon_counter = 1
        while moons >= 1:
            moon_header = self.create_info_label(f"Moon {moon_counter}:", is_header=True, indent_level=1)
            self.planets_section.add_content_widget(moon_header)
            self.planet_widgets[planet_id].append(moon_header)
            
            moon_widgets = self.generate_moon_details(body, zone)
            self.planet_widgets[planet_id].extend(moon_widgets)
            moons -= 1
            moon_counter += 1
        
        # add separator
        separator = self.create_info_label("─" * 50)
        self.planets_section.add_content_widget(separator)
        self.planet_widgets[planet_id].append(separator)
        
        return {"type": "rock", "zone": zone, "moons": moon_counter - 1}
    
    # generate gas giant details and return the widgets created
    def generate_gas_giant_details(self, zone, planet_id):
        body, gravity, combinedOrbitFeatures, moons = gasPlanetCreation(zone)
        
        # store widgets for this gas giant so we can remove them later
        self.planet_widgets[planet_id] = []
        
        # add header for this specific gas giant with close button
        giant_header_widget = PlanetHeaderWidget(f"Gas Giant in {zone} ({planet_id}):", planet_id)
        giant_header_widget.close_clicked.connect(self.remove_planet_details)
        self.planets_section.add_content_widget(giant_header_widget)
        self.planet_widgets[planet_id].append(giant_header_widget)
        
        gasGiant_parts = {
            "Body": body,
            "Gravity": gravity
        }
        
        for gas, elements in gasGiant_parts.items():
            if not isinstance(elements, list):
                elements = [str(elements)]
            else:
                elements = [str(element) for element in elements]
                
            part_header = self.create_info_label(f"{gas}:", is_header=True, indent_level=1)
            self.planets_section.add_content_widget(part_header)
            self.planet_widgets[planet_id].append(part_header)
            
            for element in elements:
                element_label = self.create_info_label(f"• {element}", indent_level=1)
                self.planets_section.add_content_widget(element_label)
                self.planet_widgets[planet_id].append(element_label)
        
        # handle Orbital Features separately for gas giants
        if combinedOrbitFeatures:
            orbital_header = self.create_info_label("Orbital Features:", is_header=True, indent_level=1)
            self.planets_section.add_content_widget(orbital_header)
            self.planet_widgets[planet_id].append(orbital_header)
            
            for i in range(0, len(combinedOrbitFeatures), 2):
                if i < len(combinedOrbitFeatures):
                    feature_name = combinedOrbitFeatures[i]
                    feature_label = self.create_info_label(f"• {feature_name}", indent_level=1)
                    self.planets_section.add_content_widget(feature_label)
                    self.planet_widgets[planet_id].append(feature_label)
                    
                    if i + 1 < len(combinedOrbitFeatures):
                        description = combinedOrbitFeatures[i + 1]
                        if description and description.strip():
                            clean_desc = description.strip()
                            if clean_desc and clean_desc != "No notable features are added to the Gas Giant's orbit":
                                desc_label = self.create_info_label(clean_desc, indent_level=1)
                                self.planets_section.add_content_widget(desc_label)
                                self.planet_widgets[planet_id].append(desc_label)
        
        # generate moons if any
        moon_counter = 1
        while moons >= 1:
            moon_header = self.create_info_label(f"Moon {moon_counter}:", is_header=True, indent_level=1)
            self.planets_section.add_content_widget(moon_header)
            self.planet_widgets[planet_id].append(moon_header)
            
            moon_widgets = self.generate_moon_details(body, zone)
            self.planet_widgets[planet_id].extend(moon_widgets)
            moons -= 1
            moon_counter += 1
        
        # add separator
        separator = self.create_info_label("─" * 50)
        self.planets_section.add_content_widget(separator)
        self.planet_widgets[planet_id].append(separator)
        
        return {"type": "gas", "zone": zone, "moons": moon_counter - 1}
    
    # generate moon details and return the widgets created
    def generate_moon_details(self, pbody, zone):
        body, gravity, Atmosphere, atmosphericComp, climate, habitability, Landmasses, LandDesc = moonCreation(pbody, zone)
        
        moon_widgets = []
        
        moon_parts = {
            "Body": body,
            "Gravity": gravity,
            "Atmosphere": Atmosphere,
            "Atmospheric Composition": atmosphericComp,
            "Climate": climate,
            "Habitability": habitability,
            "Landmasses": Landmasses,
            "Landmass Description": LandDesc,
        }
        
        for bits, elements in moon_parts.items():
            if not isinstance(elements, list):
                elements = [str(elements)]
            else:
                elements = [str(element) for element in elements]

            part_header = self.create_info_label(f"{bits}:", is_header=True, indent_level=2)
            self.planets_section.add_content_widget(part_header)
            moon_widgets.append(part_header)
            
            for element in elements:
                element_label = self.create_info_label(f"• {element}", indent_level=2)
                self.planets_section.add_content_widget(element_label)
                moon_widgets.append(element_label)
        
        return moon_widgets
    
    # remove all widgets associated with a specific planet
    def remove_planet_details(self, planet_id):
        if planet_id in self.planet_widgets:
            # remove all widgets from the layout
            for widget in self.planet_widgets[planet_id]:
                self.planets_section.content_layout.removeWidget(widget)
                widget.deleteLater()
            
            # clean up the tracking dictionaries
            del self.planet_widgets[planet_id]
            if planet_id in self.planet_data_cache:
                # reset the generated flag so it can be regenerated if clicked again
                self.planet_data_cache[planet_id]['generated'] = False
            
            print(f"Removed details for {planet_id}")

    # removes all content from all sidebar sections    
    def clearSidebar(self):
        self.star_section.clear_content()
        self.features_section.clear_content()
        self.elements_section.clear_content()
        self.planets_section.clear_content()
        self.planet_widgets.clear()
        self.planet_data_cache.clear()