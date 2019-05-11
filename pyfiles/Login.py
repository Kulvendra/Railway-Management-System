# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Menu import Ui_Dialog as ui1
from Admin import Ui_Dialog as ui2
import pymysql
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='pawaraman@123',
                             db='RMS')

print ("connect successful!!")
cursor = connection.cursor()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(260, 220, 291, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(260, 290, 291, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 360, 94, 36))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 200, 16, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 270, 63, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 20, 611, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 130, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(280, 360, 61, 24))
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(350, 360, 71, 24))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(670, 440, 121, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 420, 94, 36))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton.clicked.connect(self.div)
           

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 430, 141, 21))
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(260, 400, 291, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 32))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def menu(self):
        print("hello")
        data=[]
        s="("
        d=self.textEdit.toPlainText()
        print(d)
        if(d=="NULL"):
            d=None
        s=s+"%s"+","    
        data.append(d)
        d=self.textEdit_2.toPlainText()
        print(d)
        if(d=="NULL"):
            d=None
        data.append(d)
        s=s+"%s"+")"
        cursor.execute("SELECT count(*) FROM Customer where Username=%s and Password=%s",data)
        val = cursor.fetchall()
        print(int(val[0][0]))
        if(int(val[0][0])==1):  
            self.next=QtWidgets.QDialog()
            #self.ui=Ui_Dialog()
            self.ui=ui1()
            self.ui.setupUi(self.next)
            self.next.show()

    def admin(self):

        data=[]
        s="("
        d=self.textEdit.toPlainText()
        print(d)
        if(d=="NULL"):
            d=None
        s=s+"%s"+","    
        data.append(d)
        d=self.textEdit_2.toPlainText()
        print(d)
        if(d=="NULL"):
            d=None
        data.append(d)
        s=s+"%s"+")"
        cursor.execute("SELECT count(*) FROM Admin where Username=%s and Password=%s",data)
        val = cursor.fetchall()
        print(int(val[0][0]))
        if(int(val[0][0])==1):  
            self.next=QtWidgets.QDialog()
            #self.ui=Ui_Dialog()
            self.ui=ui2()
            self.ui.setupUi(self.next)
            self.next.show() 

    def div(self): 
        if (self.radioButton_1.isChecked() == True):
            print("aman")
            (self.menu())
        elif (self.radioButton_2.isChecked() == True):
            print("pawar")
            (self.admin()) 
                              
                             

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "Railway Management System"))
        self.label_4.setText(_translate("MainWindow", "Login"))
        self.radioButton_1.setText(_translate("MainWindow", "&User"))
        self.radioButton_2.setText(_translate("MainWindow", "Admin"))
        self.label_5.setText(_translate("MainWindow", "IIT Jammu© 2019"))
        self.pushButton_2.setText(_translate("MainWindow", "Signup"))
        self.label_6.setText(_translate("MainWindow", "don\'t have account ? "))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
