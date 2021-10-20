import random

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Sudoku(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('Sudoku.ui', None)
        self.ui.show()

        self.game = [[None for i in range(9)]for j in range(9)]

        for i in range(9):
            for j in range(9):
                tb = QLineEdit()
                tb.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                tb.setAlignment(Qt.AlignCenter)
                tb.setStyleSheet('font-size : 22px')
                self.game[i][j] = tb
                self.ui.grid.addWidget(tb, i, j)
                self.game[i][j].textChanged.connect(self.check)

        self.ui.btn_newgame.clicked.connect(self.newGame)
        self.ui.btn_check.clicked.connect(self.check)
        self.ui.btn_reset.clicked.connect(self.reset)
        self.ui.btn_mode.clicked.connect(self.mode)

        self.dark = 0

    def check(self):
        self.win = 1

        for i in range(9):
            for j in range(9):
                if self.dark == 0:
                    if self.game[i][j].isReadOnly() == False:
                        self.game[i][j].setStyleSheet('font-size : 22px; color : blue; background-color : white')
                    else:
                        self.game[i][j].setStyleSheet('font-size : 22px; background-color : white')
                else:
                    if self.game[i][j].isReadOnly() == False:
                        self.game[i][j].setStyleSheet('font-size : 22px; color : blue; background-color : gray')
                    else:
                        self.game[i][j].setStyleSheet('font-size : 22px; background-color : gray')

        #check rows
        for row in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[row][i].text() == self.game[row][j].text() and i!=j and self.game[row][i].text()!='':
                        self.game[row][i].setStyleSheet('font-size : 22px; color : red; background-color : pink')
                        self.win = 0

        #check columns
        for col in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[i][col].text() == self.game[j][col].text() and i!=j and self.game[i][col].text()!='':
                        self.game[i][col].setStyleSheet('font-size : 22px; color : red; background-color : pink')
                        self.win = 0

        #check 3*3
        for row in range(0, 3):
            for i in range(0, 3):
                for col in range(0, 3):
                    for j in range(0, 3):
                        self.quadrangle(row, i, col, j) 

                for col in range(3, 6):
                    for j in range(3, 6):
                        self.quadrangle(row, i, col, j) 

                for col in range(6, 9):
                    for j in range(6, 9):
                        self.quadrangle(row, i, col, j) 

        for row in range(3, 6):
            for i in range(3, 6):
                for col in range(0, 3):
                    for j in range(0, 3):
                        self.quadrangle(row, i, col, j) 

                for col in range(3, 6):
                    for j in range(3, 6):
                        self.quadrangle(row, i, col, j) 

                for col in range(6, 9):
                    for j in range(6, 9):
                        self.quadrangle(row, i, col, j) 

        for row in range(6, 9):
            for i in range(6, 9):
                for col in range(0, 3):
                    for j in range(0, 3):
                        self.quadrangle(row, i, col, j) 

                for col in range(3, 6):
                    for j in range(3, 6):
                        self.quadrangle(row, i, col, j) 

                for col in range(6, 9):
                    for j in range(6, 9):
                        self.quadrangle(row, i, col, j)

        for i in range(9):
            for j in range(9):
                if self.game[i][j].text() == '':
                    self.win = 0

        if self.win == 1:
            msgBoxWin = QMessageBox()
            msgBoxWin.setText('YES. YOU WIN :)')
            msgBoxWin.exec()

    def quadrangle(self, r, i, c, j):
        if self.game[r][c].text() == self.game[i][j].text() and r!=i and c!=j and self.game[r][c].text()!='':
            self.game[r][c].setStyleSheet('font-size : 22px; color : red; background-color : pink')
            self.win = 0

    def reset(self):
        for i in range(9):
            for j in range(9):
                if self.game[i][j].isReadOnly() == False:
                    self.game[i][j].setText('')

    def newGame(self):
        for i in range(9):
            for j in range(9):
                self.game[i][j].setText('')

        try:
            r = random.randint(1, 6)
            file_path = f'data/s{r}.txt'
            file = open(file_path, 'r')
            text = file.read()
            rows = text.split('\n')
            for i in range(9):
                numbers = rows[i].split(' ')
                for j in range(9):
                    if numbers[j] != '0':
                        if self.dark == 1:
                            self.game[i][j].setStyleSheet('font-size : 22px; color : gray')
                        elif self.dark == 0:
                            self.game[i][j].setStyleSheet('font-size : 22px; color : white')

                        self.game[i][j].setText(numbers[j])
                        self.game[i][j].setReadOnly(True)
                    else:
                        self.game[i][j].setReadOnly(False)
        except:
            msgBox = QMessageBox()
            msgBox.setText('Cant find data file!!')
            msgBox.exec()

    def mode(self):
        if self.ui.btn_mode.text() == 'Dark Mode':
            self.ui.setStyleSheet('background-color : black')
            self.ui.btn_mode.setText('Light Mode')
            self.dark = 1
            for i in range(9):
                for j in range(9):
                    self.game[i][j].setStyleSheet('font-size : 22px; background-color : gray')
        else:
            self.ui.setStyleSheet('background-color : lightgray')
            self.ui.btn_mode.setText('Dark Mode')
            self.dark = 0
            for i in range(9):
                for j in range(9):
                    self.game[i][j].setStyleSheet('font-size : 22px; background-color : white')

app = QApplication()
window = Sudoku()
app.exec()