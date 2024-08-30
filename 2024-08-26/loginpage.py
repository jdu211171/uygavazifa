import sys

from PyQt6.QtWidgets import QApplication, QLineEdit, QTextEdit, QWidget
from components import Input, Button

class LoginPage(QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.setFixedSize(400, 500)

        self.setWindowTitle("Tizimga kirish")

        self.loginInput = Input(self, 100, "Enter login...")
        self.passwordInput = Input(self, 160, "Enter password...")

        self.loginButton = Button('Login', self, 230)

        self.show()



App = QApplication(sys.argv)
window = LoginPage()
sys.exit(App.exec())
