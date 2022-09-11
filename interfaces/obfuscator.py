from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# master class
class Obfuscator(QWidget):
    def __init__(self):
        super(Obfuscator, self).__init__()

        # global attributes
        self.active = None

        # instance methods
        self.window_configurations()
        self.user_interface()

    def window_configurations(self):
        pass

    def user_interface(self):
        pass
