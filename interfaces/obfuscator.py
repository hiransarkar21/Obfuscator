from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from python_obfuscator.techniques import *
import re


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
        self.obfuscator_screen_height = self.screen_size.height() // 1.4

        self.obfuscated_code = None
        self.source_code = None

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

        self.one_liner_option = QRadioButton()
        self.one_liner_option.setFont(self.paragraph_font)
        self.one_liner_option.setText(" Convert to One Liner ")
        self.one_liner_option.setStyleSheet("""QRadioButton::indicator{width:17px; height:17px;}""")

        self.variable_renamer_option = QRadioButton()
        self.variable_renamer_option.setFont(self.paragraph_font)
        self.variable_renamer_option.setText(" Variable Renamer  ")
        self.variable_renamer_option.setStyleSheet("""QRadioButton::indicator{width:17px; height:17px;}""")

        self.add_random_variables_option = QRadioButton()
        self.add_random_variables_option.setFont(self.paragraph_font)
        self.add_random_variables_option.setText(" Add Random Variables ")
        self.add_random_variables_option.setStyleSheet("""QRadioButton::indicator{width:17px; height:17px;}""")

        self.apply_all_techniques_option = QRadioButton()
        self.apply_all_techniques_option.setFont(self.paragraph_font)
        self.apply_all_techniques_option.setText(" Apply all Available Techniques")
        self.apply_all_techniques_option.setChecked(True)
        self.apply_all_techniques_option.setStyleSheet("""QRadioButton::indicator{width:17px; height:17px;}""")

        self.ready_set_go_button = QPushButton()
        self.ready_set_go_button.setFont(self.paragraph_font)
        self.ready_set_go_button.setText("Ready! Set! Go !")
        self.ready_set_go_button.setFixedSize(int(self.width() // 3), int(self.height() // 10))
        self.ready_set_go_button.clicked.connect(self.ready_set_go_button_clicked)
        self.ready_set_go_button.setStyleSheet(
            """QPushButton{border-radius: 30px; background-color: green; color: white;}""")

        # adding widgets to layouts
        self.header_layout.addWidget(self.welcome_label, alignment=Qt.AlignHCenter)
        self.header_layout.addWidget(self.modules_and_libraries_used_label, alignment=Qt.AlignHCenter)

        self.child_target_file_layout_browse.addWidget(self.get_target_file_name, alignment=Qt.AlignLeft)
        self.child_target_file_layout_browse.addWidget(self.browse_button)

        self.additional_options_layout.addSpacing(10)
        self.additional_options_layout.addWidget(self.one_liner_option)
        self.additional_options_layout.addSpacing(5)
        self.additional_options_layout.addWidget(self.variable_renamer_option)
        self.additional_options_layout.addSpacing(5)
        self.additional_options_layout.addWidget(self.add_random_variables_option)
        self.additional_options_layout.addSpacing(5)
        self.additional_options_layout.addWidget(self.apply_all_techniques_option)
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

    def ready_set_go_button_clicked(self):
        # python-obfuscator start here .....

        with open(self.target_file, "r") as target_file:
            self.source_code = target_file.read()

        self.obfuscate_code_main(source_code=self.source_code)

    def obfuscate_code_main(self, source_code):
        if self.variable_renamer_option.isChecked():
            self.obfuscated_code = self.variable_renamer_technique(code=source_code)

        elif self.add_random_variables_option.isChecked():
            self.obfuscated_code = self.add_random_variables_technique(code=source_code)

        elif self.one_liner_option.isChecked():
            self.obfuscated_code = self.one_liner_technique(code=source_code)

        else:
            self.obfuscated_code = self.apply_all_methods(code=source_code)

        file_name = QFileDialog.getSaveFileName(self, 'Save File', "", "(*.py)")
        with open(file_name[0], "w") as target_file:
            target_file.write(self.obfuscated_code)

        # restoring window
        self.restore_window()

    @staticmethod
    def one_liner_technique(code):
        formatted_code = re.sub(
            r"(;)\1+", ";", """exec(\"\"\"{};\"\"\")""".format(code.replace("\n", ";").replace('"""', '\\"\\"\\"')),
        )

        if formatted_code[0] == ';':
            return formatted_code[1:]
        return formatted_code

    @staticmethod
    def variable_renamer_technique(code):
        code = "\n" + code
        variable_names = re.findall(r"(\w+)(?=( |)=( |))", code)
        name_generator = VariableNameGenerator()
        for i in range(len(variable_names)):
            obfuscated_name = name_generator.get_random(i + 1)
            code = re.sub(
                r"(?<=[^.])(\b{}\b)".format(variable_names[i][0]), obfuscated_name, code
            )
        return code

    @staticmethod
    def add_random_variables_technique(code):
        useless_variables_to_add = random.randint(100, 400)
        name_generator = VariableNameGenerator()
        data_generator = RandomDataTypeGenerator()
        for v in range(1, useless_variables_to_add):
            rand_data = data_generator.get_random()
            if type(rand_data) == str:
                rand_data = '"{}"'.format(rand_data)
            if v % 2 == 0:
                code = "{} = {}\n".format(name_generator.get_random(v), rand_data) + code
            else:
                code = code + "\n{} = {}".format(name_generator.get_random(v), rand_data)
        return code

    @staticmethod
    def apply_all_methods(code):
        techniques = [variable_renamer, add_random_variables, one_liner]
        for technique in techniques:
            code = technique(code)

        return code

    def restore_window(self):
        self.get_target_file_name.clear()




