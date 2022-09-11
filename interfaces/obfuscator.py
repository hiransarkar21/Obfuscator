from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# master class
class Obfuscator(QWidget):
    def __init__(self):
        super(Obfuscator, self).__init__()

        # global attributes
        self.heading_font = QFont("Poppins", 18)
        self.heading_font.setWordSpacing(2)
        self.heading_font.setLetterSpacing(QFont.AbsoluteSpacing, 1)

        self.secondary_heading_font = QFont("Poppins", 16)
        self.secondary_heading_font.setWordSpacing(2)
        self.secondary_heading_font.setLetterSapcing(QFont.AbsoluteSpacing, 1)

        self.paragraph_font = QFont("Poppins", 13)
        self.paragraph_font.setWordSpacing(2)
        self.paragraph_font.setLetterSpacing(QFont.AbsoluteSpacing, 1)

        self.screen_size = QApplication.primaryScreen().availableSize()

        # instance methods
        self.window_configurations()
        self.user_interface()

    def window_configurations(self):
        pass

    def user_interface(self):
        pass
