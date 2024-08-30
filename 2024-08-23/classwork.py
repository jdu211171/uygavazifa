import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QRadioButton, QMessageBox

TESTS = [
    {
        'id': 1,
        'question': "Tuxum birinchi paydo bo'lganmi tovuqmi?",
        'answers': {
            'A': "Tuxum",
            'B': "Tovuq",
            'C': "Aziz",
            'D': "Mo'rs"
        },
        'right_answer': 'C'
    },
    {
        'id': 2,
        'question': "O'zbekiston oldin nima deb nomlangan",
        'answers': {
            'A': "O'zbekiston",
            'B': "Qozog'iston",
            'C': "Qirg'iziston",
            'D': "Aziziston"
        },
        'right_answer': 'A'
    },
    {
        'id': 3,
        'question': "Dunyodagi eng katta okean qaysi?",
        'answers': {
            'A': "Atlantika",
            'B': "Tinch okeani",
            'C': "Hind okeani",
            'D': "Shimoliy muz okeani"
        },
        'right_answer': 'B'
    },
    {
        'id': 4,
        'question': "Yerning eng ichki qatlami nima deb ataladi?",
        'answers': {
            'A': "Qobiq",
            'B': "Mantiya",
            'C': "Yadro",
            'D': "Litosfera"
        },
        'right_answer': 'C'
    },
    {
        'id': 5,
        'question': "Eng uzun daryo qaysi?",
        'answers': {
            'A': "Nil",
            'B': "Amazonka",
            'C': "Missisipi",
            'D': "Yangtze"
        },
        'right_answer': 'A'
    },
    {
        'id': 6,
        'question': "Eng katta qit'a qaysi?",
        'answers': {
            'A': "Afrika",
            'B': "Yevropa",
            'C': "Osiyo",
            'D': "Janubiy Amerika"
        },
        'right_answer': 'C'
    },
    {
        'id': 7,
        'question': "Eng baland tog' qaysi?",
        'answers': {
            'A': "Everest",
            'B': "K2",
            'C': "Kilimanjaro",
            'D': "Makalu"
        },
        'right_answer': 'A'
    },
    {
        'id': 8,
        'question': "Eng katta cho'l qaysi?",
        'answers': {
            'A': "Sahara",
            'B': "Gobi",
            'C': "Kalahari",
            'D': "Arabiston"
        },
        'right_answer': 'A'
    },
    {
        'id': 9,
        'question': "Eng katta orol qaysi?",
        'answers': {
            'A': "Madagaskar",
            'B': "Borneo",
            'C': "Yangi Gvineya",
            'D': "Grenlandiya"
        },
        'right_answer': 'D'
    },
    {
        'id': 10,
        'question': "Eng uzun devor qaysi?",
        'answers': {
            'A': "Berlin devori",
            'B': "Xitoy devori",
            'C': "Hadrian devori",
            'D': "Meksika devori"
        },
        'right_answer': 'B'
    },
    {
        'id': 11,
        'question': "Eng katta ko'l qaysi?",
        'answers': {
            'A': "Kaspiy dengizi",
            'B': "Yuqori ko'l",
            'C': "Viktoriya ko'li",
            'D': "Michigan ko'li"
        },
        'right_answer': 'A'
    },
    {
        'id': 12,
        'question': "Eng katta mamlakat qaysi?",
        'answers': {
            'A': "AQSh",
            'B': "Kanada",
            'C': "Rossiya",
            'D': "Xitoy"
        },
        'right_answer': 'C'
    }
]


class Window(QMainWindow):
    last_question_index = 0
    score = 0

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My Custom Calculator")

        self.setGeometry(100, 100, 800, 500)

        self.UiComponents()

        self.show()

    def UiComponents(self):

        self.questionLabel = QLabel("Savol", self)
        self.questionLabel.setStyleSheet("font-size: 22px; font-weight: bold; color: green;")
        self.questionLabel.move(20, 10)

        self.A_variant = QRadioButton("A", self)
        self.A_variant.setStyleSheet("font-size: 16px; color: #111336;")
        self.A_variant.move(50, 50)

        self.B_variant = QRadioButton("B", self)
        self.B_variant.setStyleSheet("font-size: 16px; color: #111336;")
        self.B_variant.move(50, 90)

        self.C_variant = QRadioButton("C", self)
        self.C_variant.setStyleSheet("font-size: 16px; color: #111336;")
        self.C_variant.move(50, 130)

        self.D_variant = QRadioButton("D", self)
        self.D_variant.setStyleSheet("font-size: 16px; color: #111336;")
        self.D_variant.move(50, 170)

        self.nextBtn = QPushButton("Next", self)
        self.nextBtn.setStyleSheet("font-size: 20px;")
        self.nextBtn.move(600, 400)
        self.fillWindowWithQuestion()
        self.nextBtn.clicked.connect(self.nextFunction)

    def clearRadioButtons(self):
        self.A_variant.setChecked(False)
        self.B_variant.setChecked(False)
        self.C_variant.setChecked(False)
        self.D_variant.setChecked(False)

    def fillWindowWithQuestion(self):
        question = TESTS[self.last_question_index]

        self.questionLabel.setText(question['question'])
        self.A_variant.setText(question['answers']['A'])
        self.B_variant.setText(question['answers']['B'])
        self.C_variant.setText(question['answers']['C'])
        self.D_variant.setText(question['answers']['D'])

        self.A_variant.adjustSize()
        self.B_variant.adjustSize()
        self.C_variant.adjustSize()
        self.D_variant.adjustSize()

    def nextFunction(self):
        selected_answer = None
        if self.A_variant.isChecked():
            selected_answer = 'A'
        elif self.B_variant.isChecked():
            selected_answer = 'B'
        elif self.C_variant.isChecked():
            selected_answer = 'C'
        elif self.D_variant.isChecked():
            selected_answer = 'D'

        if selected_answer == TESTS[self.last_question_index]['right_answer']:
            self.score += 1

        self.last_question_index += 1
        if self.last_question_index >= len(TESTS):
            self.showResults()
        else:
            self.fillWindowWithQuestion()

    def showResults(self):
        msg = QMessageBox()
        msg.setWindowTitle("Test Results")
        msg.setText(f"Testlar tugadi. Sizning natijangiz: {self.score}/{len(TESTS)}")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.closeApp)
        msg.exec()

    def closeApp(self):
        self.close()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
