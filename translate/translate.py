from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Translate(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('Translate.ui', None)
        self.ui.show()

        self.file_to_list()

        self.ui.translate.clicked.connect(self.translate)

    def file_to_list(self):
        self.WORDS = []
        try:
            file = open('translate.txt' , 'r' , encoding="utf-8")
            my_words = file.read().split('\n')
            for i in range(len(my_words)):
                if i%2 == 0:
                    dict = {}
                    dict['english'] = my_words[i]
                else:
                    dict['persian'] = my_words[i]
                    self.WORDS.append(dict)
        except:
            pass
    
    def translate(self):
        sentence = self.ui.input.text().lower()
        words = sentence.split(' ')
        translate_text = ''

        if self.ui.persian.isChecked():
            for word in words:
                for trans in self.WORDS:
                    if word == trans['persian']:
                        if word == words[-1]:
                            translate_text += trans['english']
                        else:
                            translate_text += trans['english'] + ' '
        
        elif self.ui.english.isChecked():
            for word in words:
                for trans in self.WORDS:
                    if word == trans['english']:
                        if word == words[-1]:
                            translate_text += trans['persian']
                        else:
                            translate_text += trans['persian'] + ' '

        self.ui.output.setText(translate_text)

app = QApplication()
window = Translate()

app.exec()