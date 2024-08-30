from os import system
from typing import NamedTuple, Optional, List
import sys

from PyQt6.QtWidgets import QApplication, QMessageBox, QListWidget, QWidget, QVBoxLayout, QTextEdit, QListWidgetItem

from mainpage import MainPage
from loginpage import LoginPage
from registerpage import RegisterPage
from myposts import MyPostsPage
from addpost import AddPostPage
from allposts import AllPostsPage
from components import TextArea
from database import Database, User
from errors import UsernameAlreadyExistsError

system("clear")


class ListWidgetWithTextArea(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(50, 120, 350, 450)

    def addTextAreaItem(self, text: str):
        widget = QWidget()

        layout = QVBoxLayout()

        text_edit = TextArea(widget, 0)
        text_edit.setText(text)
        text_edit.setEnabled(False)

        layout.addWidget(text_edit)

        widget.setLayout(layout)

        item = QListWidgetItem()

        item.setSizeHint(widget.sizeHint())

        self.addItem(item)

        self.setItemWidget(item, widget)

class App:
    USER: Optional[User] = None
    ALL_POSTS: List[dict] = []
    MY_POSTS: List[dict] = []

    def __init__(self) -> None:
        self.boshSahifaOyna = MainPage()
        self.loginOyna = LoginPage()
        self.registerOyna = RegisterPage()
        self.meningPostlarimOyna = MyPostsPage()
        self.hammaPostlarOyna = AllPostsPage()

        self.database = Database()
        self.postsCollectionLW = ListWidgetWithTextArea(self.hammaPostlarOyna)
        self.postsCollectionRW = ListWidgetWithTextArea(self.meningPostlarimOyna)

        self.boshSahifaOyna.loginBtn.clicked.connect(self.showLoginPage)
        self.boshSahifaOyna.registerBtn.clicked.connect(self.showRegisterPage)

        self.loginOyna.loginBtn.clicked.connect(self.loginFunction)
        self.registerOyna.registerBtn.clicked.connect(self.registerFunction)

        self.hammaPostlarOyna.myPostsBtn.clicked.connect(self.showMyPostsPage)

        self.hammaPostlarOyna.writePostBtn.clicked.connect(self.showAddPostPage)

        self.boshSahifaOyna.show()

    def loginFunction(self):
        username = self.loginOyna.usernameInput.text()
        password = self.loginOyna.passwordInput.text()

        foundUser = self.database.login(username, password)

        if not foundUser:
            return self.alert("Foydalanuvchi nomi topilmadi!")

        self.USER = User(**foundUser)
        self.showAllPostsPage()

    def registerFunction(self):
        try:
            name = self.registerOyna.nameInput.text().strip()
            surname = self.registerOyna.surnameInput.text().strip()
            username = self.registerOyna.usernameInput.text().strip()
            password = self.registerOyna.passwordInput.text().strip()

            new_user = self.database.register(name, surname, username, password)
            self.USER = User(**new_user)

            return self.showAllPostsPage()
        except UsernameAlreadyExistsError as message:
            errorMessage = message.args[0]
            return self.alert(errorMessage)

    def alert(self, text: str):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Icon.Warning)
        msgbox.setText(text)
        msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)

        return msgbox.exec()

    def showLoginPage(self):
        self.loginOyna.show()
        self.boshSahifaOyna.close()

    def showRegisterPage(self):
        self.registerOyna.show()
        self.boshSahifaOyna.close()

    def showAllPostsPage(self):
        self.ALL_POSTS = self.database.selectAllPosts()

        for POST in self.ALL_POSTS:
            self.postsCollectionLW.addTextAreaItem(POST['text'])

        self.hammaPostlarOyna.show()
        self.loginOyna.close()
        self.registerOyna.close()

    def showMyPostsPage(self):
        if self.USER is None:
            return self.alert("User not logged in!")

        self.MY_POSTS = self.database.selectUserPosts(self.USER.id)

        for POST in self.MY_POSTS:
            self.postsCollectionRW.addTextAreaItem(POST['text'])

        self.meningPostlarimOyna.show()
        self.hammaPostlarOyna.close()

    def showAddPostPage(self):
        if self.USER is None:
            return self.alert("User not logged in!")

        self.postQoshishOyna = AddPostPage(self.USER.id)
        self.postQoshishOyna.show()
        self.hammaPostlarOyna.close()

app = QApplication(sys.argv)

dastur = App()
sys.exit(app.exec())
