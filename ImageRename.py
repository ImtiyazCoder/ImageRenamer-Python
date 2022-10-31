from datetime import datetime
from time import time
from tkinter import messagebox
import os,getpass
from PyQt5 import QtCore, QtGui, QtWidgets

tm=datetime.now().strftime("%H.%M")

us=getpass.getuser().replace('.'," ").title()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 406)
        MainWindow.setMinimumSize(QtCore.QSize(580, 406))
        MainWindow.setMaximumSize(QtCore.QSize(580, 406))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 561, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setLineWidth(1)
        self.label_2.setIndent(-1)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 350, 91, 21))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 180, 561, 121))
        self.textEdit.setToolTip("")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.rename())
        self.pushButton.setGeometry(QtCore.QRect(150, 320, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.exit())
        self.pushButton_2.setGeometry(QtCore.QRect(300, 320, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Rename"))
        
        if tm > str('05.01') and tm <= str(12.00):
            self.label_2.setText(_translate("MainWindow", "Good Morning! " + str(us)))
        if tm > str(12.01) and tm <= str(16.00):    
            self.label_2.setText(_translate("MainWindow", "Good Afternoon! " + str(us)))
        if tm >= str(16.01) and tm <= str(24.00):
            self.label_2.setText(_translate("MainWindow", "Good Evening! " + str(us)))
        if tm >= str('00.00') and tm <= str('05.00'):    
            self.label_2.setText(_translate("MainWindow", "Good Evening! " + str(us)))

        self.label.setText(_translate("MainWindow", "Image Rename by Folders"))
        self.label_3.setText(_translate("MainWindow", "© Imtiyaz Shaikh"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Paste folder path here"))
        self.pushButton.setText(_translate("MainWindow", "Rename"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))

    def rename(self):
        path=self.textEdit.toPlainText()
        final_path=path.replace('\\','//')

        file_name=os.listdir(final_path)

        for index, file in enumerate(file_name):
            folder_path=final_path + '//' + file +'//'
            
            
            img=os.listdir(folder_path)
            for index, list in enumerate(img):
                
                try:
                    os.rename(str(folder_path) + str(list),str(folder_path) + str(file)+'_'+str(index+1)+'.jpg' )
                except:
                    pass

        messagebox.showinfo("Image","Done")            

    def exit(self):
         sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
