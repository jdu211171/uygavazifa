import sys

from PyQt6.QtWidgets import QApplication, QLineEdit, QTextEdit, QWidget
from components import Input, Button


class RegisterPage(QWidget):

    def __init__(self) -> None:
            super().__init__()

            self.setFixedSize(400, 500)

            self.setWindowTitle("Ro'yxatdan o'tish")

            self.nameInput = Input(self, 60, "Enter fullname...")
            self.emailInput = Input(self, 110, "Enter email...")
            self.loginInput = Input(self, 160, "Enter login...")
            self.passwordInput = Input(self, 210, "Enter password...")

            self.loginButton = Button('Login', self, 270)

            self.show()


App = QApplication(sys.argv)
window = RegisterPage()
sys.exit(App.exec())
