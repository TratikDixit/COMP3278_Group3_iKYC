# Form implementation generated from reading ui file 'accounts.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
import pandas as pd


class Ui_Dialog2(object):
    def __init__(self, user_name):
        self.user_name = user_name

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1142, 720)
        Dialog.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(10, 470, 811, 101))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        myconn = mysql.connector.connect(
            host="localhost", user="root", database="backend")
        cursor = myconn.cursor()
        select = "select A.account_number, B.account_type, A.branch_id, A.open_date from Account A, BankAccount B where A.account_number = B.account_number and A.username = '%s';" % (
            self.user_name)
        cursor.execute(select)
        data = cursor.fetchall()
        counterRows = 0
        for d in data:
            counterRows += 1

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(450, 130, 581, 451))
        # self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # self.tableWidget.verticalHeader().setStretchLastSection(True)
        # self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(counterRows)
        self.tableWidget.setColumnWidth(0, 152)
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(2, 130)
        self.tableWidget.setColumnWidth(3, 153)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item2 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item2)
        item3 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item3)
        item4 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item4)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 180, 400, 400))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./Images/user profile.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 281, 50))
        self.label_2.setObjectName("label_2")

        self.horizontalLayoutWidget_1 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_1.setGeometry(
            QtCore.QRect(550, 600, 400, 40))
        self.horizontalLayoutWidget_1.setObjectName("horizontalLayoutWidget_1")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_1)
        self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.pushButton_1 = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_1)

        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setStyleSheet(
            "font:bold;background-color: rgb(173, 216, 230);")

        self.horizontalLayout_1.addWidget(self.pushButton_1)
        self.pushButton_1.clicked.connect(self.saveCSV)

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Profile History"))
        self.pushButton_1.setText(_translate("Dialog", "Save to CSV"))

        self.label_2.setFont(QtGui.QFont('Times', 20))
        # print(self.user_name)
        self.label_2.setText(_translate(
            "Dialog", "Profile History of %s" % (self.user_name)))
        self.label_2.setStyleSheet('font:bold; color: purple;')
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Account Number"))

        item2 = self.tableWidget.horizontalHeaderItem(1)
        item2.setText(_translate("Dialog", "Account Type"))

        item3 = self.tableWidget.horizontalHeaderItem(2)
        item3.setText(_translate("Dialog", "Branch ID"))

        item4 = self.tableWidget.horizontalHeaderItem(3)
        item4.setText(_translate("Dialog", "Opening Date"))

        myconn = mysql.connector.connect(
            host="localhost", user="root", database="backend")
        cursor = myconn.cursor()
        select = "select A.account_number, B.account_type, A.branch_id, A.open_date from Account A, BankAccount B where A.account_number = B.account_number and A.username = '%s';" % (
            self.user_name)
        cursor.execute(select)
        data = cursor.fetchall()
        row = 0

        for d in data:
            account_number = d[0]
            self.tableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(account_number))
            account_type = d[1]
            self.tableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(account_type))
            branch_id = d[2]
            self.tableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(branch_id))
            opening_date = d[3].strftime("%m/%d/%Y")
            self.tableWidget.setItem(
                row, 3, QtWidgets.QTableWidgetItem(opening_date))
            row += 1

    def saveCSV(self):
        myconn = mysql.connector.connect(
            host="localhost", user="root",  database="backend")
        cursor = myconn.cursor()
        select = "select A.account_number, B.account_type, A.branch_id, A.open_date from Account A, BankAccount B where A.account_number = B.account_number and A.username = '%s';" % (
            self.user_name)
        cursor.execute(select)
        data = cursor.fetchall()
        if(data != []):
            data_df = pd.DataFrame(
                data, columns=["Account Number", "Account Type", "Branch ID", "Opening Date"])
            data_df.to_csv("accounts_details.csv")


'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

'''
