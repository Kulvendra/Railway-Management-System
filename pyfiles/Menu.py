# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PNR_Check import Ui_Dialog as ui1
from Book_Ticket import Ui_Dialog as ui2
from PNR_Check import Ui_Dialog as ui3


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(906, 539)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(380, 40, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 260, 191, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pnr)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 260, 191, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.book)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 260, 191, 91))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.train)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(400, 460, 121, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 120, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(100, 90, 701, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        # Dialog.setCentralWidget(Dialog)
        # self.menubar = QtWidgets.QMenuBar(Dialog)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 906, 32))
        # self.menubar.setObjectName("menubar")
        # Dialog.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(Dialog)
        # self.statusbar.setObjectName("statusbar")
        # Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def pnr(self): 
        self.next=QtWidgets.QDialog()
        #self.ui=Ui_Dialog()
        self.ui=ui1()
        self.ui.setupUi(self.next)
        self.next.show()   

    def book(self): 
        self.next=QtWidgets.QDialog()
        #self.ui=Ui_Dialog()
        self.ui=ui2()
        self.ui.setupUi(self.next)
        self.next.show() 

    def train(self): 
        self.next=QtWidgets.QDialog()
        #self.ui=Ui_Dialog()
        self.ui=ui3()
        self.ui.setupUi(self.next)
        self.next.show()                         

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Welcome"))
        self.pushButton.setText(_translate("Dialog", "PNR Status Check"))
        self.pushButton_2.setText(_translate("Dialog", "Book Your Ticket"))
        self.pushButton_3.setText(_translate("Dialog", "Train Status"))
        self.label_2.setText(_translate("Dialog", "IIT Jammu© 2019"))
        self.label_3.setText(_translate("Dialog", " Have you not found the right one?\n"
"Find a service suitable for you here."))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
