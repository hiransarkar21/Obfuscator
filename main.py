import sys
import login
from PyQt5.QtWidgets import QApplication


def main():
    if __name__ == "__main__":
        application = QApplication(sys.argv)
        master_window = login.MainWindow()
        master_window.show()
        application.exec_()


main()
