import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QRadioButton, QMessageBox, QTextEdit, QWidget
from components import Button


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Text Area")

        self.move(100, 100)

        self.setFixedSize(400, 500)

        self.UIComponents()

        self.show()

    def UIComponents(self):

        self.label = QLabel("Main Page", self)
        self.label.setStyleSheet("font-size: 26px;")
        self.label.move((self.width() - self.label.width())//2, 30)

        self.registerButton = Button('Register', self, 300)

        self.loginButton = Button("Login", self, 370)

        self.loginButton.resize(self.loginButton.width(), self.loginButton.height())
        self.registerButton.resize(self.loginButton.width(), self.loginButton.height())

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
