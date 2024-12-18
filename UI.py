from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QListWidget, QSplitter, QListWidgetItem, QApplication
from PyQt5.QtCore import Qt

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
        sidebar_layout = QVBoxLayout(sidebar)

        label = QLabel("Sidebar Menu")
        label.setAlignment(Qt.AlignCenter)
        sidebar_layout.addWidget(label)

        sidebar_layout.addStretch()
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