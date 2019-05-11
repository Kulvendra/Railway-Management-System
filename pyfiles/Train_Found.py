# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Train_Found.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from UserDetails import Ui_Dialog as ui1
import datetime 
import calendar
import pymysql
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='pawaraman@123',
                             db='RMS')

print ("connect successful!!")
cursor = connection.cursor()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(846, 589)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(180, 80, 481, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(90, 110, 671, 371))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(310, 30, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(370, 520, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.det)



        b = datetime.datetime.strptime(str(sys.argv[3]), '%Y-%M-%d').weekday() 
        btf= (calendar.day_name[b]) 



        model = QtGui.QStandardItemModel()
        cursor.execute("SHOW Columns FROM Train")
        columnsData = cursor.fetchall()
        columnsName = []

        for item in columnsData:
            columnsName.append(item[0])

        cursor.execute("SELECT * FROM Train")
        rows = cursor.fetchall()

        model.setRowCount(0)
        model.setColumnCount(len(columnsName))
        model.setHorizontalHeaderLabels(columnsName)

        l=[str(sys.argv[1]),str(sys.argv[2])]
        
        if(btf=='Monday'):
            cursor.execute("SELECT * FROM Train where Frm=%s and Tu=%s and Mon=1",l)
            data = cursor.fetchall()
        elif(btf=='Tueday'):
            cursor.execute("SELECT * FROM Train where Frm=%s and Tu=%s and Tue=1",l)
            data = cursor.fetchall()
        elif(btf=='Wednesday'):
            cursor.execute("SELECT * FROM Train where Frm=%s and Tu=%s and Wed=1",l)
            data = cursor.fetchall()
        elif(btf=='Thursday'):
            cursor.execute("SELECT * FROM Train where Frm=%s and Tu=%s and Thurs=1",l)
            data = cursor.fetchall()
        elif(btf=='Friday'):
            cursor.execute("SELECT * FROM Train where Frm=%s and Tu=%s and Fri=1",l)
            data = cursor.fetchall()
        elif(btf=='Saturday'):
            cursor.execute("SELECT * FROM Train where Frm=%s and Tu=%s and Sat=1",l)
            data = cursor.fetchall()
        elif(btf=='Sunday'):
            cursor.execute("SELECT * FROM Train where Frm=%s and Tu=%s and Sun=1",l)
            data = cursor.fetchall()

        self.tableView.verticalHeader().hide()

        for d in data:
            row = []
            for id in d:
                print(id)
                item = QtGui.QStandardItem(str(id))
                item.setEditable(True)
                row.append(item)
            model.appendRow(row)
        self.tableView.setModel(model)

        # self.gridLayout.addWidget(self.tableView, 1, 0, 1, 3)





        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def det(self): 
        self.next=QtWidgets.QDialog()
        #self.ui=Ui_Dialog()
        self.ui=ui1()
        self.ui.setupUi(self.next)
        self.next.show()  
    

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Available Trains"))
        self.pushButton.setText(_translate("Dialog", "Book Ticket"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
