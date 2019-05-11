# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PNR_Check.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

from PNR_Status import Ui_Dialog as ui3


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 433)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 20, 461, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 110, 411, 51))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(160, 80, 481, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(230, 240, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(380, 230, 151, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(540, 230, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pnrs)

        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(160, 290, 481, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        # Dialog.setCentralWidget(Dialog)
        # self.menubar = QtWidgets.QMenuBar(Dialog)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 32))
        # self.menubar.setObjectName("menubar")
        # Dialog.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(Dialog)
        # self.statusbar.setObjectName("statusbar")
        # Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def pnrs(self): 
        cmd='python3 PNR_Status.py '+self.textEdit.toPlainText()
        os.system(cmd)
        # self.next=QtWidgets.QDialog()
        # #self.ui=Ui_Dialog()
        # self.ui=ui3()
        # self.ui.setupUi(self.next)
        # self.next.show()   

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Passenger Current Status Enquiry"))
        self.label_2.setText(_translate("Dialog", "Enter the PNR for your booking below to get the current status.\n"
"               You will find it on the top left corner of the ticket."))
        self.label_3.setText(_translate("Dialog", "Enter PNR Number"))
        self.pushButton.setText(_translate("Dialog", "Submit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
