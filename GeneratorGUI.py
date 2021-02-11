from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from rueppel import Rueppel
import sys, os

class Okno(QMainWindow):
    def __init__(self,xorTable, lfsr, result,*args,**kwargs):
        super(Okno, self).__init__(*args,*kwargs)
        self.setWindowTitle("Self-decimation Generator")
        self.xorTable = xorTable
        self.lfsr = lfsr
        self.result = result
        self.r = Rueppel(xorTable, lfsr, result)
        
        titleText = QLabel()
        titleText.setText("RUEPPEL")
        titleText.setAlignment(Qt.AlignCenter)
        titleText.setFont(QFont('Comic Sans',50))
        titleText.setStyleSheet("QLabel {color : #cae8d5}")

        titleText2 = QLabel()
        titleText2.setText("GENERATOR")
        titleText2.setAlignment(Qt.AlignCenter)
        titleText2.setFont(QFont('Comic Sans',50))
        titleText2.setStyleSheet("QLabel {color : #cae8d5}")

        self.subtitleText = QLabel()
        self.subtitleText.setText(" ")
        self.subtitleText.setAlignment(Qt.AlignCenter)
        self.subtitleText.setFont(QFont('Comic Sans',20))
        self.subtitleText.setStyleSheet("QLabel {color : #84a9ac}")

        self.dparameterField = QLineEdit()
        self.dparameterField.setPlaceholderText("First parameter")
        self.dparameterField.setFont(QFont('Comic Sans',12))
        self.dparameterField.setStyleSheet("QLineEdit {color : #84a9ac}")

        self.kparameterField = QLineEdit()
        self.kparameterField.setPlaceholderText("Second parameter")
        self.kparameterField.setFont(QFont('Comic Sans',12))
        self.kparameterField.setStyleSheet("QLineEdit {color : #84a9ac}")

        self.amountField = QLineEdit()
        self.amountField.setPlaceholderText("Amount")
        self.amountField.setFont(QFont('Comic Sans',12))
        self.amountField.setStyleSheet("QLineEdit {color : #84a9ac}")

        textFielsLayout = QHBoxLayout()
        textFielsLayout.addWidget(self.dparameterField)
        textFielsLayout.addWidget(self.kparameterField)
        textFielsLayout.addWidget(self.amountField)
        textFielsLayoutW = QWidget()
        textFielsLayoutW.setLayout(textFielsLayout)

        self. dparameterFromFileButton = QFileDialog()
        self.kparameterFromFileButton = QFileDialog()

        dparameterFileButton = QPushButton()
        dparameterFileButton.setText("Get first parameter from file")
        dparameterFileButton.setFont(QFont('Comic Sans',12))
        dparameterFileButton.setStyleSheet("QPushButton {background : #3b6978}")
        dparameterFileButton.setStyleSheet("QPushButton {color : #cae8d5}")
        dparameterFileButton.clicked.connect(self.dparameterFileClicked)

        kparameterFileButton = QPushButton()
        kparameterFileButton.setText("Get second parameter from file")
        kparameterFileButton.setFont(QFont('Comic Sans',12))
        kparameterFileButton.setStyleSheet("QPushButton {background : #3b6978}")
        kparameterFileButton.setStyleSheet("QPushButton {color : #cae8d5}")
        kparameterFileButton.clicked.connect(self.kparameterFileClicked)

        self.saveButton = QPushButton()
        self.saveButton.setText("Save to file")
        self.saveButton.setFont(QFont('Comic Sans',12))
        self.saveButton.setStyleSheet("QPushButton {background : #3b6978}")
        self.saveButton.setStyleSheet("QPushButton {color : #cae8d5}")
        self.saveButton.clicked.connect(self.saveClicked)
        self.saveButton.setEnabled(False)

        self.infoButton = QPushButton()
        self.infoButton.setText("Info")
        self.infoButton.setFont(QFont('Comic Sans',12))
        self.infoButton.setStyleSheet("QPushButton {background : #3b6978}")
        self.infoButton.setStyleSheet("QPushButton {color : #cae8d5}")
        self.infoButton.clicked.connect(self.infoClicked)

        buttonsFileLayout = QHBoxLayout()
        buttonsFileLayout.addWidget(dparameterFileButton)
        buttonsFileLayout.addWidget(kparameterFileButton)
        buttonsFileLayoutW = QWidget()
        buttonsFileLayoutW.setLayout(buttonsFileLayout)

        generateButton = QPushButton()
        generateButton.setText("Generate")
        generateButton.setFont(QFont('Comic Sans',12))
        generateButton.setStyleSheet("QPushButton {background : #3b6978}")
        generateButton.setStyleSheet("QPushButton {color : #cae8d5}")
        generateButton.clicked.connect(self.generateClicked)

        amountFileButton = QPushButton()
        amountFileButton.setText("Get amount from file")
        amountFileButton.setFont(QFont('Comic Sans',12))
        amountFileButton.setStyleSheet("QPushButton {background : #3b6978}")
        amountFileButton.setStyleSheet("QPushButton {color : #cae8d5}")
        amountFileButton.clicked.connect(self.amountFileClicked)

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(generateButton)
        buttonsLayout.addWidget(amountFileButton)
        buttonsLayoutW = QWidget()
        buttonsLayoutW.setLayout(buttonsLayout)

        infoButtonsLayout = QHBoxLayout()
        infoButtonsLayout.addWidget(self.saveButton)
        infoButtonsLayout.addWidget(self.infoButton)
        infobuttonsLayoutW = QWidget()
        infobuttonsLayoutW.setLayout(infoButtonsLayout)

        #Main Layout
        mainMenu = QVBoxLayout()
        mainMenu.setAlignment(Qt.AlignCenter)
        mainMenu.addWidget(titleText)
        mainMenu.addWidget(titleText2)
        mainMenu.addWidget(self.subtitleText)
        mainMenu.addWidget(textFielsLayoutW)
        mainMenu.addWidget(buttonsLayoutW)
        mainMenu.addWidget(buttonsFileLayoutW)
        mainMenu.addWidget(infobuttonsLayoutW)

        mainMenuW = QWidget()
        mainMenuW.setLayout(mainMenu)

        self.setCentralWidget(mainMenuW)

    def generateClicked(self):
        self.r.lfsr = []
        self.r.result = []
        d = int(self.dparameterField.text())
        k = int(self.kparameterField.text())
        amount = int(self.amountField.text())
        self.r.genLFSR()
        self.r.saveLFSR()
        self.r.runGenerator(amount, d, k)
        self.subtitleText.setText("DONE")
        self.saveButton.setEnabled(True)
    
    def amountFileClicked(self):
        """
        key = self.genKey()
        amountFileed = self.amountFile(key)
        self.subtitleText.setText("amountFile MODE")
        self.amountFileedText.setText(amountFileed)
        self.saveButton.setEnabled(True)
        """
    
    def dparameterFileClicked(self):
        self.kparameterFromFileButton.hide()
        self.dparameterFromFileButton.show()

        if self. dparameterFromFileButton.exec():
            files = self. dparameterFromFileButton.selectedFiles()
            r = open(files[0],'r',encoding="utf-8")
            with r:
                data = r.read()
                self.dparameterField.setText(data)
    
    def kparameterFileClicked(self):
        self. dparameterFromFileButton.hide()
        self.kparameterFromFileButton.show()

        if self.kparameterFromFileButton.exec():
            files = self.kparameterFromFileButton.selectedFiles()
            r = open(files[0],'r',encoding="utf-8")
            with r:
                data = r.read()
                self.kparameterField.setText(data)
  
    def saveClicked(self):
        fileInput = self.r.binToString()
        if len(self.r.result) == 1000000:
            w = open("result1M.txt", "w")
            with w:
                w.write(fileInput)
        elif len(self.r.result) == 20000:
            w = open("result20.txt", "w")
            with w:
                w.write(fileInput)
        else:
            w = open("result.txt", "w")
            with w:
                w.write(fileInput)

    def infoClicked(self):
        info = QMessageBox()
        info.setWindowTitle("Info")
        info.setStyleSheet("QMessageBox {background-color : #cae8d5}")
        f = open("info.txt", "r", encoding="utf-8")
        data = f.read()
        info.setText(data)
        info.setFont(QFont('Courier',12))
        info.exec_()
                     
#MAIN
xorTable = {
    21 : [18,20],
    22 : [20,21],
    23 : [17,22],
    24 : [19,20,22,23],
    25 : [21,24],
    26 : [19,23,24,25],
    27 : [21,24,25,26],
    28 : [24,27],
    29 : [26,28],
    30 : [23,25,28,29],
    31 : [27,30],
}
lfsr = []
result = []
fileInput = ""
app = QApplication(sys.argv)
window = Okno(xorTable, lfsr, result)
window.setFixedSize(500,400)
window.setStyleSheet("background-color: #204051")
window.show()

app.exec_()