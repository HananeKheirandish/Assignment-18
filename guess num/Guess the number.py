import random

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Guess_Number(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('Guess_num.ui', None)
        self.ui.show()

        self.num = random.randint(0, 50)

        self.ui.check.clicked.connect(self.check)

        self.ui.new_game.clicked.connect(self.reset)

    def check(self):
        try:
            guess_num = int(self.ui.hint.text())
            
            if guess_num < self.num:
                self.ui.res.setText(' No! Guess upper! ')
            elif guess_num > self.num:
                self.ui.res.setText(' No! Guess lower! ')
            else:
                self.ui.res.setText(' Yes! You Win! ')
        except:
            pass
        
    def reset(self):
        try:
            self.num = random.randint(0, 50)
            self.ui.res.setText('')
        except:
            pass

app = QApplication()
window = Guess_Number()

app.exec()