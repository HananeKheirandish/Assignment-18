import random
from string import *

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Pass_Generator(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('Password_Generator.ui', None)
        self.ui.show()

        self.ui.generate.clicked.connect(self.generate)

    def generate(self):
        pass_code = ascii_letters + digits + punctuation
        password = ''

        if self.ui.level_1.isChecked():
            range_pass = 8
        elif self.ui.level_2.isChecked():
            range_pass = 12
        elif self.ui.level_3.isChecked():
            range_pass = 20

        for i in range(range_pass):
            char_pass = random.choice(pass_code)
            password += char_pass

        self.ui.password.setText(password)

app = QApplication()
window = Pass_Generator()

app.exec()