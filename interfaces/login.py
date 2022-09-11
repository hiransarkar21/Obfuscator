from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# master class
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # global attributes
        self.heading_font = QFont("Poppins", 20)
        self.heading_font.setBold(True)
        self.heading_font.setWordSpacing(2)
        self.heading_font.setLetterSpacing(QFont.AbsoluteSpacing, 1)

        self.secondary_heading_font = QFont("Poppins", 18)
        self.secondary_heading_font.setWordSpacing(2)
        self.secondary_heading_font.setLetterSpacing(QFont.AbsoluteSpacing, 1)

        self.screen_size = QApplication.primaryScreen().availableSize()
        self.login_screen_width = self.screen_size.width() // 2.7
        self.login_screen_height = self.screen_size.height() // 2

        # instance methods
        self.window_configuration()
        self.user_interface()

    def window_configuration(self):
        self.setFixedSize(int(self.login_screen_width), int(self.login_screen_height))

    def user_interface(self):
        # parent and their respective child layouts
        self.master_layout = QVBoxLayout()
        self.header_layout = QVBoxLayout()
        self.body_layout = QVBoxLayout()
        self.child_email_layout = QVBoxLayout()
        self.child_password_layout = QVBoxLayout()
        self.footer_layout = QHBoxLayout()

        # widgets
        self.welcome_label = QLabel()
        self.welcome_label.setFont(self.heading_font)
        self.welcome_label.setText("Welcome to PYTHON OBFUSCATOR Tool")

        self.modules_and_libraries_used_label = QLabel()
        self.modules_and_libraries_used_label.setFont(self.secondary_heading_font)
        self.modules_and_libraries_used_label.setText("PyQt5 | Python-Obfuscator | MySQL")

        # adding widgets to respective layouts
        self.header_layout.addWidget(self.welcome_label)
        self.header_layout.addWidget(self.modules_and_libraries_used_label)

        # adding child email and password layout to parent body_layout
        self.body_layout.addLayout(self.child_email_layout)
        self.body_layout.addLayout(self.child_password_layout)

        # adding header, body and footer layout to master_layout
        self.master_layout.addLayout(self.header_layout)
        self.master_layout.addLayout(self.body_layout)
        self.master_layout.addLayout(self.footer_layout)

        self.setLayout(self.master_layout)
