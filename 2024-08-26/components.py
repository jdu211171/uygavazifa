from PyQt6.QtWidgets import QLabel, QPushButton, QApplication, QLineEdit, QTextEdit, QWidget


MAX_BUTTON_WIDTH = 0
MAX_INPUT_WIDTH = 0

class Button(QPushButton):
    def __init__(self, text: str, window: QWidget, y: int) -> None:
        super().__init__(text, window)
        global MAX_BUTTON_WIDTH
        self.setStyleSheet("""
                QPushButton {
                    font-size: 22px;
                    background-color: black;
                    color: white;
                    border-radius: 15px;
                }
                QPushButton::hover {
                    background-color: #212121;
                }
                QPushButton::pressed {
                    color: #212121;
                    background-color: white;
                }
            """)
        MAX_BUTTON_WIDTH = self.width() if self.width() > MAX_BUTTON_WIDTH else MAX_BUTTON_WIDTH
        self.adjustSize()
        self.resize(MAX_BUTTON_WIDTH + 20, self.height() + 10)
        self.move((window.width() - self.width())//2, y)


class Label(QLabel):

    def __init__(self, window: QWidget, y: int, text: str):
        super().__init__(window)
        global MAX_INPUT_WIDTH
        self.setText(text)
        self.adjustSize()
        self.setStyleSheet("font-size: 26px;")
        self.move((window.width() - self.width())//2, y)


class Input(QLineEdit):

    def __init__(self, window: QWidget, y: int, placeholder: str):
        super().__init__(window)
        global MAX_INPUT_WIDTH
        self.setPlaceholderText(placeholder)
        self.setStyleSheet("""
                QLineEdit {
                    font-size: 22px;
                    color: black;
                    border: 1px solid black;
                }
            """)
        self.adjustSize()
        MAX_INPUT_WIDTH = self.width() if self.width() > MAX_INPUT_WIDTH else MAX_INPUT_WIDTH
        self.resize(MAX_INPUT_WIDTH + 20, self.height() + 10)
        self.move((window.width() - self.width())//2, y)
