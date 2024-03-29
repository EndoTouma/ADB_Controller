from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget

from ui.about_tab import AboutTab
from ui.control_tab import ControlTab
from utils.data_management import DataManager

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 900
WINDOW_X_POS = 100
WINDOW_Y_POS = 100


class ADBController(QWidget):
    """
    Main widget for the ADB Controller application.
    """

    def __init__(self):
        """
        Initialize the ADBController widget.
        """
        super().__init__()
        
        self.devices, self.commands = DataManager.load_data()
        self.tab_control = ControlTab(self.devices, self.commands)

        self.init_ui()
        
        self.tab_control.refresh_device_list()  # Refresh device list at startup
    
    def init_ui(self):
        """
        Initialize the UI components.
        """
        layout = QVBoxLayout()
        tabs = QTabWidget()

        # Tabs
        tab_about = AboutTab()
        tabs.addTab(self.tab_control, "Control")
        tabs.addTab(tab_about, "About")

        # Layout setup
        layout.addWidget(tabs)
        self.setLayout(layout)
        
        self.setWindowTitle("ADB Controller")
        self.setGeometry(WINDOW_X_POS, WINDOW_Y_POS, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.show()

    def save_data_method(self):
        """
        Save the data using the DataManager.
        """
        DataManager.save_data(self.devices, self.commands)
