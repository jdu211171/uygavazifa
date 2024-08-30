from PyQt6.QtWidgets import QWidget
from components import Button, Input, Label, TextArea
from database import Database

class AddPostPage(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.database = Database()

        self.setFixedSize(600, 400)
        self.setWindowTitle("Add Post Page")

        self.label = Label("Post yozish", self, 50)
        self.postTextArea = TextArea(self, 110)

        self.addPostBtn = Button("Add", self, 320)
        self.addPostBtn.clicked.connect(self.add_post)

        self.database = Database()

    def add_post(self):
        post_text = self.postTextArea.toPlainText()
        if post_text:
            self.database.addPost(self.user_id, post_text)
            self.postTextArea.clear()
            print("Post added successfully!")
        else:
            print("Post text cannot be empty.")
