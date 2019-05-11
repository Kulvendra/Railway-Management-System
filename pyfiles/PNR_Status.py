# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Train_Found.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(851, 592)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(90, 270, 671, 261))
        self.tableView.setObjectName("tableView")
        self.horizontalScrollBar = QtWidgets.QScrollBar(Dialog)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(140, 510, 561, 20))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(520, 220, 121, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        # ite= QtGui.QStandardItem(str(sys.argv[1]))


        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 130, 411, 51))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(180, 100, 481, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalScrollBar = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar.setGeometry(QtCore.QRect(740, 290, 20, 211))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 40, 461, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(290, 220, 211, 21))
        self.label_3.setObjectName("label_3")


        # model = QtGui.QStandardItemModel()
        # cursor.execute("SHOW Columns FROM Passenger")
        # columnsData = cursor.fetchall()
        # columnsName = []

        # for item in columnsData:
        #     columnsName.append(item[0])

        # cursor.execute("SELECT * FROM Passenger")
        # rows = cursor.fetchall()

        # model.setRowCount(0)
        # model.setColumnCount(len(columnsName))
        # model.setHorizontalHeaderLabels(columnsName)
        
        # cursor.execute("SELECT * FROM Passenger where PNR=%s",sys.argv[1])
        # data = cursor.fetchall()
        # self.tableView.verticalHeader().hide()

        # for d in data:
        #     row = []
        #     for id in d:
        #         print(id)
        #         item = QtGui.QStandardItem(str(id))
        #         item.setEditable(True)
        #         row.append(item)
        #     model.appendRow(row)
        # self.tableView.setModel(model)

        # self.gridLayout.addWidget(self.tableView, 1, 0, 1, 3)




        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:10pt;\">2461650515</span></p></body></html>"))


        self.textEdit.setText(str(sys.argv[1]))



        self.label_2.setText(_translate("Dialog", "Enter the PNR for your booking below to get the current status.\n"
"               You will find it on the top left corner of the ticket."))
        self.label.setText(_translate("Dialog", "Passenger Current Status Enquiry"))
        self.label_3.setText(_translate("Dialog", "You Queried For : PNR Number: "))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
