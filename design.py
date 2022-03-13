import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
######
alphabet = []
for i in range(26):
    alphabet.append(chr(i + 65))

rotor1 = [[], []]
rotor2 = [[], []]
rotor3 = [[], []]
reflector = []
red = [8,1, 2, 8, 1]
blue = [3,0, 3, 4, 9]

for i in range(26):
    rotor1[0].append((random.randrange(26)))
    rotor1[1].append((random.randrange(26)))
    rotor2[0].append((random.randrange(26)))
    rotor2[1].append((random.randrange(26)))
    rotor3[0].append((random.randrange(26)))
    rotor3[1].append((random.randrange(26)))
    reflector.append((random.randrange(26)))

 
def boxDraw(data, numRows, r, b, type):

    a = "<html><head></head><body>"
    a += chr(0x250c)
    for i in range(25):
        a += 3*chr(0x2500)
        a += chr(0x252c)
    a += 3*chr(0x2500)
    a += chr(0x2510)
    a += "<br>"
    a += chr(0x2502)
    for i in range(numRows):
        for j in range(26):
            if (numRows == 1):

                if(type == "int" and data[j] >= 0):
                    value = "+" + str(data[j])
                elif(type == "int" and data[j] < 0):
                    value = str(data[j])
                elif (type == "str"):
                    value = data[j]
                if (j == r):
                    a += "<span style='color : red'>"
                elif (j == b):
                    a += "<span style='color : blue'>"
                else:
                    a += "<span>"
                if (len(value) == 1):
                    a= a + ' ' + "" + value +  ' ' + "</span>" + chr(0x2502)
                elif (len(value) == 2):
                    a= a + '' + value +  ' ' + "</span>" + chr(0x2502)
                elif (len(value) == 3):
                    a= a + '' + value +  '</span>' + chr(0x2502)
            else:
                if(data[i][j] >= 0):
                    value = "+" + str(data[i][j])
                else:
                    value = str(data[i][j])
                if (i == 0 and j == r):
                    a += "<span style='color : red'>"
                elif (i == 1 and j == b):
                    a += "<span style='color : blue'>"
                else:
                    a += "<span>"
                if (len(value) == 1):
                    a= a + ' ' + value +  ' </span>' + chr(0x2502)
                elif (len(value) == 2):
                    a= a + '' + value +  ' </span>' + chr(0x2502)
                elif (len(value) == 3):
                    a= a + '' + value +  '</span>' + chr(0x2502)
        if(numRows != 1 and i < numRows - 1):
            a += "<br>"
            a += chr(0x251C) # ├
            for j in range(25):
                a += 3*chr(0x2500)  # ─
                a += chr(0x253c) # ┼
            a += 3*chr(0x2500)
            a += chr(0x2524)
            a += "<br>"
            a += chr(0x2502)
            


    a += "<br>"
    a += chr(0x2514)
    for i in range(25):
        a += 3*chr(0x2500)
        a += chr(0x2534)
    a += 3*chr(0x2500)
    a += chr(0x2518)
    a += "</body></html>"
    return a
######

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize
        MainWindow.setFixedSize(898, 680)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 110))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 170, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 110))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 170, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 110))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 110))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 170, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 110))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 110))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.reflector = QtWidgets.QLabel(self.centralwidget)
        self.reflector.setGeometry(QtCore.QRect(20, 10, 781, 60))
        self.reflector.setObjectName("reflector")
        self.reflector.setStyleSheet("font: 9pt \"DejaVu Sans Mono\";")
        self.rotor3 = QtWidgets.QLabel(self.centralwidget)
        self.rotor3.setGeometry(QtCore.QRect(20, 80, 781, 65))
        self.rotor3.setObjectName("rotor3")
        self.rotor3.setStyleSheet("font: 9pt \"DejaVu Sans Mono\";")
        self.rotor2 = QtWidgets.QLabel(self.centralwidget)
        self.rotor2.setGeometry(QtCore.QRect(20, 150, 781, 65))
        self.rotor2.setObjectName("rotor2")
        self.rotor2.setStyleSheet("font: 9pt \"DejaVu Sans Mono\";")
        self.rotor1 = QtWidgets.QLabel(self.centralwidget)
        self.rotor1.setGeometry(QtCore.QRect(20, 220, 781, 65))
        self.rotor1.setObjectName("rotor1")
        self.rotor1.setStyleSheet("font: 9pt \"DejaVu Sans Mono\";")
        self.alphabet = QtWidgets.QLabel(self.centralwidget)
        self.alphabet.setGeometry(QtCore.QRect(20, 290, 781, 60))
        self.alphabet.setObjectName("alphabet")
        self.alphabet.setStyleSheet("font: 9pt \"DejaVu Sans Mono\";")
        self.refLabel = QtWidgets.QLabel(self.centralwidget)
        self.refLabel.setGeometry(QtCore.QRect(800, 30, 61, 17))
        self.refLabel.setObjectName("refLabel")
        self.rotor1Label = QtWidgets.QLabel(self.centralwidget)
        self.rotor1Label.setGeometry(QtCore.QRect(800, 240, 54, 17))
        self.rotor1Label.setObjectName("rotor1Label")
        self.rotor3Label = QtWidgets.QLabel(self.centralwidget)
        self.rotor3Label.setGeometry(QtCore.QRect(800, 100, 54, 16))
        self.rotor3Label.setObjectName("rotor3Label")
        self.rotor2Label = QtWidgets.QLabel(self.centralwidget)
        self.rotor2Label.setGeometry(QtCore.QRect(800, 170, 54, 17))
        self.rotor2Label.setObjectName("rotor2Label")
        self.keyLabel = QtWidgets.QLabel(self.centralwidget)
        self.keyLabel.setGeometry(QtCore.QRect(270, 356, 31, 21))
        self.keyLabel.setObjectName("keyLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 350, 311, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.zoneOne = QtWidgets.QTextEdit(self.centralwidget)
        self.zoneOne.setGeometry(QtCore.QRect(50, 420, 769, 70))
        self.zoneOne.setObjectName("zoneOne")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(7, 390, 861, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.configBtn = QtWidgets.QPushButton(self.centralwidget)
        self.configBtn.setGeometry(QtCore.QRect(70, 510, 121, 31))
        self.configBtn.setObjectName("configBtn")
        self.encryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.encryptBtn.setGeometry(QtCore.QRect(270, 510, 121, 31))
        self.encryptBtn.setObjectName("encryptBtn")
        self.nextStepBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nextStepBtn.setGeometry(QtCore.QRect(470, 510, 121, 31))
        self.nextStepBtn.setObjectName("nextStepBtn")
        self.decryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.decryptBtn.setGeometry(QtCore.QRect(670, 510, 121, 31))
        self.decryptBtn.setObjectName("decryptBtn")
        self.zoneTwo = QtWidgets.QTextEdit(self.centralwidget)
        self.zoneTwo.setGeometry(QtCore.QRect(50, 560, 769, 70))
        self.zoneTwo.setObjectName("zoneTwo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionR_nitialiser = QtWidgets.QAction(MainWindow)
        self.actionR_nitialiser.setObjectName("actionR_nitialiser")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionQuitter.triggered.connect(QCoreApplication.instance().quit)
        self.menuMenu.addAction(self.actionR_nitialiser)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.reflector.setText(_translate("MainWindow", boxDraw(reflector, 1, red[4], blue[4], "int")))
        self.rotor3.setText(_translate("MainWindow", boxDraw(rotor3, 2, red[3], blue[3], "int")))
        self.rotor2.setText(_translate("MainWindow", boxDraw(rotor2, 2, red[2], blue[2], "int")))
        self.rotor1.setText(_translate("MainWindow", boxDraw(rotor1, 2, red[1], blue[1], "int")))
        self.alphabet.setText(_translate("MainWindow", boxDraw(alphabet, 1, red[0], blue[0], "str")))
        self.refLabel.setText(_translate("MainWindow", "Reflecteur"))
        self.rotor1Label.setText(_translate("MainWindow", "Rotor 1"))
        self.rotor3Label.setText(_translate("MainWindow", "Rotor 3"))
        self.rotor2Label.setText(_translate("MainWindow", "Rotor 2"))
        self.keyLabel.setText(_translate("MainWindow", "Clé : "))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Saisir votre clé (Ex : (R3, G, +7)(R2, D, -6)(R1, D, +5)"))
        self.zoneOne.setPlaceholderText(_translate("MainWindow", "Taper un message à encrypter ou affichage du résultat de décryption"))
        self.configBtn.setText(_translate("MainWindow", "Configurer Rotors"))
        self.encryptBtn.setText(_translate("MainWindow", "Encrypter"))
        self.nextStepBtn.setText(_translate("MainWindow", "Etape suivante"))
        self.decryptBtn.setText(_translate("MainWindow", "Décrypter"))
        self.zoneTwo.setPlaceholderText(_translate("MainWindow", "Taper un message à décrypter ou affichage du résultat d\'encryption"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionR_nitialiser.setText(_translate("MainWindow", "Rénitialiser"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
