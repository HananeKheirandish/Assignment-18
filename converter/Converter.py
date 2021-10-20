from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Converter(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('Converter.ui', None)
        self.ui.show()

        self.ui.com_kind.currentTextChanged.connect(self.comboBox_change)
        self.ui.btn_res.clicked.connect(self.calculate)

        self.ui.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

    def comboBox_change(self):
        self.ui.com_from.clear()
        self.ui.com_to.clear()
        self.ui.input.setText('')
        self.ui.output.setText('')

        if self.ui.com_kind.currentText() == 'Mass':
            self.ui.com_from.addItems(['gram', 'kilogram', 'ton', 'pound'])
            self.ui.com_to.addItems(['gram', 'kilogram', 'ton', 'pound'])
        elif self.ui.com_kind.currentText() == 'Lenght':
            self.ui.com_from.addItems(['milimeter', 'centimeter', 'meter', 'kilometer', 'inch'])
            self.ui.com_to.addItems(['milimeter', 'centimeter', 'meter', 'kilometer', 'inch'])
        elif self.ui.com_kind.currentText() == 'Temperature':
            self.ui.com_from.addItems(['centigrade', 'fahrenheit', 'kelvin'])
            self.ui.com_to.addItems(['centigrade', 'fahrenheit', 'kelvin'])
        elif self.ui.com_kind.currentText() == 'Digital Mass':
            self.ui.com_from.addItems(['bit', 'byte', 'kilobyte', 'megabyte', 'gigabyte', 'terabyte'])
            self.ui.com_to.addItems(['bit', 'byte', 'kilobytes', 'megabyte', 'gigabyte', 'terabyte']) 

    def calculate(self):
        froms = self.ui.com_from.currentText()
        to = self.ui.com_to.currentText()
        input = float(self.ui.input.text())

        # Mass
        if froms == 'gram':
            if to == 'gram':
                res = input
            elif to == 'kilogram':
                res = input / 1000
            elif to == 'ton':
                res = input / 1000000
            elif to == 'pound':
                res = input * 0.002

        elif froms == 'kilogram':
            if to == 'gram':
                res = input * 1000
            elif to == 'kilogram':
                res = input 
            elif to == 'ton':
                res = input / 1000
            elif to == 'pound':
                res = input * 2.20

        elif froms == 'ton':
            if to == 'gram':
                res = input * 1000000
            elif to == 'kilogram':
                res = input * 1000
            elif to == 'ton':
                res = input 
            elif to == 'pound':
                res = input * 2679.2

        elif froms == 'pound':
            if to == 'gram':
                res = input * 453.59237
            elif to == 'kilogram':
                res = input * 0.45359237
            elif to == 'ton':
                res = input * 0.0004536
            elif to == 'pound':
                res = input 

        #Lenght
        if froms == 'milimeter':
            if to == 'milimeter':
                res = input 
            elif to == 'centimeter':
                res = input * 0.1
            elif to == 'meter':
                res = input * 0.001
            elif to == 'kilometer':
                res = input * 0.000001
            elif to == 'inch':
                res = input * 0.0394

        elif froms == 'centimeter':
            if to == 'milimeter':
                res = input * 10
            elif to == 'centimeter':
                res = input 
            elif to == 'meter':
                res = input * 0.01
            elif to == 'kilometer':
                res = input * 0.00001
            elif to == 'inch':
                res = input * 0.3937

        elif froms == 'meter':
            if to == 'milimeter':
                res = input * 1000
            elif to == 'centimeter':
                res = input * 100
            elif to == 'meter':
                res = input 
            elif to == 'kilometer':
                res = input * 0.001
            elif to == 'inch':
                res = input * 39.37007

        elif froms == 'kilometer':
            if to == 'milimeter':
                res = input * 1000000
            elif to == 'centimeter':
                res = input * 100000
            elif to == 'meter':
                res = input * 1000
            elif to == 'kilometer':
                res = input 
            elif to == 'inch':
                res = input * 39370.07

        elif froms == 'inch':
            if to == 'milimeter':
                res = input * 25.4
            elif to == 'centimeter':
                res = input * 2.54
            elif to == 'meter':
                res = input * 0.0254
            elif to == 'kilometer':
                res = input * 0.0000254
            elif to == 'inch':
                res = input

        #Temperature
        if froms == 'centigrade':
            if to == 'centigrade':
                res = input 
            elif to == 'fahrenheit':
                res = input * 9/5 + 32
            elif to == 'kelvin':
                res = input + 273

        elif froms == 'fahrenheit':
            if to == 'centigrade':
                res = 5/9 * (input - 32)
            elif to == 'fahrenheit':
                res = input 
            elif to == 'kelvin':
                res = (5/9 * (input - 32)) + 273

        elif froms == 'kelvin':
            if to == 'centigrade':
                res = input - 273
            elif to == 'fahrenheit':
                res = 1.8 * (input - 273) + 32
            elif to == 'kelvin':
                res = input        
          
        #Digital Mass
        if froms == 'bit':
            if to == 'bit':
                res = input 
            elif to == 'byte':
                res = input * 0.125
            elif to == 'kilobyte':
                res = input * (1/8) * 0.001
            elif to == 'megabyte':
                res = input * (1/8) * 10**-6
            elif to == 'gigabyte':
                res = input * (1/8) * 10**-9
            elif to == 'terabyte':
                res = input * (1/8) * 10**-12
        
        elif froms == 'byte':
            if to == 'bit':
                res = input * 8
            elif to == 'byte':
                res = input 
            elif to == 'kilobyte':
                res = input / 1024
            elif to == 'megabyte':
                res = input / (1024 ** 2)
            elif to == 'gigabyte':
                res = input / (1024 ** 3)
            elif to == 'terabyte':
                res = input / (1024 ** 4)

        elif froms == 'kilobyte':
            if to == 'bit':
                res = input * 8 * 1000
            elif to == 'byte':
                res = input * 1000
            elif to == 'kilobyte':
                res = input 
            elif to == 'megabyte':
                res = input / 1000
            elif to == 'gigabyte':
                res = input / (1000 ** 2)
            elif to == 'terabyte':
                res = input / (1000 ** 3)

        elif froms == 'megabyte':
            if to == 'bit':
                res = input * 8 * (1000 ** 2)
            elif to == 'byte':
                res = input * (1024 ** 2)
            elif to == 'kilobyte':
                res = input * 1000
            elif to == 'megabyte':
                res = input 
            elif to == 'gigabyte':
                res = input / 1000
            elif to == 'terabyte':
                res = input / (1000 ** 2)

        elif froms == 'gigabyte':
            if to == 'bit':
                res = input * 8 * (1000 ** 3)
            elif to == 'byte':
                res = input * (1024 ** 3)
            elif to == 'kilobyte':
                res = input * (1000 ** 2)
            elif to == 'megabyte':
                res = input * 1000
            elif to == 'gigabyte':
                res = input
            elif to == 'terabyte':
                res = input / 1000

        elif froms == 'terabyte':
            if to == 'bit':
                res = input * 8 * (1000 ** 4)
            elif to == 'byte':
                res = input * (1024 ** 4)
            elif to == 'kilobyte':
                res = input * (1000 ** 3)
            elif to == 'megabyte':
                res = input * (1000 ** 2)
            elif to == 'gigabyte':
                res = input / 1000
            elif to == 'terabyte':
                res = input
        
        self.ui.output.setText(str(res))


app = QApplication()
window = Converter()

app.exec()