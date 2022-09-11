from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# master class
class ObfuscatorWindow(QWidget):
    def __init__(self):
        super(ObfuscatorWindow, self).__init__()

        # global attributes
        self.heading_font = QFont("Poppins", 18)
        self.heading_font.setBold(True)
        self.heading_font.setWordSpacing(2)
        self.heading_font.setLetterSpacing(QFont.AbsoluteSpacing, 1)

        self.secondary_heading_font = QFont("Poppins", 16)
        self.secondary_heading_font.setWordSpacing(2)
        self.secondary_heading_font.setLetterSpacing(QFont.AbsoluteSpacing, 1)

        self.paragraph_font = QFont("Poppins", 13)
        self.paragraph_font.setWordSpacing(2)
        self.paragraph_font.setLetterSpacing(QFont.AbsoluteSpacing, 1)

        self.screen_size = QApplication.primaryScreen().availableSize()
        self.obfuscator_screen_width = self.screen_size.width() // 2.7
        self.obfuscator_screen_height = self.screen_size.height() // 1.6

        # instance methods
        self.window_configurations()
        self.user_interface()

    def window_configurations(self):
        self.setFixedSize(int(self.obfuscator_screen_width), int(self.obfuscator_screen_height))
        self.setWindowTitle("Obfuscator")

    def user_interface(self):
        self.master_layout = QVBoxLayout()
        self.master_layout.setContentsMargins(50, 50, 50, 10)
        self.header_layout = QVBoxLayout()
        self.body_layout = QVBoxLayout()
        self.body_layout.setContentsMargins(0, 30, 0, 0)
        self.child_target_file_layout_browse = QHBoxLayout()
        self.additional_options_layout = QVBoxLayout()
        self.footer_layout = QHBoxLayout()

        # adding widgets

        self.welcome_label = QLabel()
        self.welcome_label.setFont(self.heading_font)
        self.welcome_label.setText("Welcome to PYTHON OBFUSCATOR Tool")

        self.modules_and_libraries_used_label = QLabel()
        self.modules_and_libraries_used_label.setFont(self.secondary_heading_font)
        self.modules_and_libraries_used_label.setText("PyQt5 | Python-Obfuscator | MySQL")

        self.choose_target_file_label = QLabel()
        self.choose_target_file_label.setText("Choose Target File")
        self.choose_target_file_label.setFont(self.paragraph_font)

        self.get_target_file_name = QLineEdit()
        self.get_target_file_name.setFont(self.paragraph_font)
        self.get_target_file_name.setReadOnly(True)
        self.get_target_file_name.setPlaceholderText("click browse button ...")
        self.get_target_file_name.setFixedSize(int(self.width() // 1.5), int(self.height() // 14))
        self.get_target_file_name.setStyleSheet("""QLineEdit{border-radius: 5px; padding-right: 10px;
        padding-left: 10px;}""")

        self.browse_button = QPushButton()
        self.browse_button.setFont(self.paragraph_font)
        self.browse_button.setText("Browse")
        self.browse_button.clicked.connect(self.browse_button_clicked)
        self.browse_button.setFixedSize(int(self.width() // 7), int(self.height() // 14))
        self.browse_button.setStyleSheet("""QPushButton{color: white; background-color: black;}""")

        self.additional_options_label = QLabel()
        self.additional_options_label.setFont(self.paragraph_font)
        self.additional_options_label.setText("Additional Options")

        self.additional_options_groupbox = QGroupBox()
        self.additional_options_groupbox.setFont(self.paragraph_font)
        self.additional_options_groupbox.setStyleSheet("""QGroupBox{background-color: transparent; 
        border: 2px solid silver; border-radius: 7px;}""")

        self.one_liner_option = QCheckBox()
        self.one_liner_option.setFont(self.paragraph_font)
        self.one_liner_option.setText(" Convert to One Liner ")

        self.save_directly_to_input_file_option = QRadioButton()
        self.save_directly_to_input_file_option.setFont(self.paragraph_font)
        self.save_directly_to_input_file_option.setText(" Save Directly to Input File")
        self.save_directly_to_input_file_option.setStyleSheet("""QRadioButton::indicator{width:17px; height:17px;}""")

        self.show_save_as_prompt_option = QRadioButton()
        self.show_save_as_prompt_option.setFont(self.paragraph_font)
        self.show_save_as_prompt_option.setText(" Show Save As Prompt")
        self.show_save_as_prompt_option.setStyleSheet("""QRadioButton::indicator{width:17px; height:17px;}""")

        self.ready_set_go_button = QPushButton()
        self.ready_set_go_button.setFont(self.paragraph_font)
        self.ready_set_go_button.setText("Ready! Set! Go !")
        self.ready_set_go_button.setFixedSize(int(self.width() // 3), int(self.height() // 10))
        self.ready_set_go_button.setStyleSheet("""QPushButton{border-radius: 30px; background-color: green; color: white;}""")

        # adding widgets to layouts
        self.header_layout.addWidget(self.welcome_label, alignment=Qt.AlignHCenter)
        self.header_layout.addWidget(self.modules_and_libraries_used_label, alignment=Qt.AlignHCenter)

        self.child_target_file_layout_browse.addWidget(self.get_target_file_name, alignment=Qt.AlignLeft)
        self.child_target_file_layout_browse.addWidget(self.browse_button)

        self.additional_options_layout.addSpacing(10)
        self.additional_options_layout.addWidget(self.one_liner_option)
        self.additional_options_layout.addSpacing(5)
        self.additional_options_layout.addWidget(self.show_save_as_prompt_option)
        self.additional_options_layout.addSpacing(5)
        self.additional_options_layout.addWidget(self.save_directly_to_input_file_option)
        self.additional_options_layout.addSpacing(10)
        self.additional_options_groupbox.setLayout(self.additional_options_layout)

        self.footer_layout.addWidget(self.ready_set_go_button, alignment=Qt.AlignHCenter)

        # adding child body layouts to parent body_layout
        self.body_layout.addWidget(self.choose_target_file_label)
        self.body_layout.addLayout(self.child_target_file_layout_browse)
        self.body_layout.addSpacing(30)
        self.body_layout.addWidget(self.additional_options_label)
        self.body_layout.addWidget(self.additional_options_groupbox)

        # adding header, body and footer layout to master_layout
        self.master_layout.addLayout(self.header_layout)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.body_layout)
        self.master_layout.addStretch()
        self.master_layout.addLayout(self.footer_layout)
        self.master_layout.addStretch()

        self.setLayout(self.master_layout)

    def browse_button_clicked(self):
        open_file_dialog_box = QFileDialog.getOpenFileName(self, "Choose Python File", "", "Python Files (*.py)")
        self.target_file = open_file_dialog_box[0]

        # writing file location to get_target_file_name LineEdit
        self.get_target_file_name.setText(self.target_file)
