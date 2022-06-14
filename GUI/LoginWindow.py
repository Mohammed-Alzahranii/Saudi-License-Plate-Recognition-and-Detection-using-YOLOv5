import mysql.connector
import pymysql
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLineEdit
from enum import Enum
import mysql.connector
import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path).replace('\\', '/')


def ExitProgram(self):
    exit()


class Privilege(Enum):
    admin = 1
    user = 2
    none = 3


connection = pymysql.connect(host="sql6.freesqldatabase.com", user="sql6497447", password="LRhX1AvV6Y",
                             database="sql6497447")
cursor = connection.cursor()

privilege = Privilege.none


class UI_QueryModPage(object):
    def __init__(self):
        self.Window = None
        self.PrevWindow = None
        self.PrevUI = None

    def setupUi(self, Form, PrevWindow, PrevUI):
        Form.setObjectName("Form")
        Form.resize(759, 911)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(759, 837))
        Form.setMaximumSize(QtCore.QSize(759, 911))
        Form.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 741, 311))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.MsgBox = QtWidgets.QLabel(Form)
        self.MsgBox.setGeometry(QtCore.QRect(160, 320, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.MsgBox.setFont(font)
        self.MsgBox.setStyleSheet("background-color: rgba(0,0,0,0);\n" "color: rgb(85, 170, 0);")
        self.MsgBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MsgBox.setObjectName("MsgBox")
        self.Confirm = QtWidgets.QPushButton(Form)
        self.Confirm.setGeometry(QtCore.QRect(110, 850, 229, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Confirm.sizePolicy().hasHeightForWidth())
        self.Confirm.setSizePolicy(sizePolicy)
        self.Confirm.setStyleSheet(
            ".QPushButton{\n" "font: 13pt bold \"Arial\";\n" "border: 2px solid black;\n" "padding: 14px 28px;\n" "background-color: rgba(0,0,0,0);\n" "border-radius: 8px;\n" "color: white;\n" "}\n" "\n" ".pushButton {\n" "border-color: #2196F3;\n" "}\n" "\n" ".QPushButton::hover{\n" "color:black;\n" "border-color: white;\n" "}")
        self.Confirm.setObjectName("Confirm")
        self.Cancel = QtWidgets.QPushButton(Form)
        self.Cancel.setGeometry(QtCore.QRect(410, 850, 229, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cancel.sizePolicy().hasHeightForWidth())
        self.Cancel.setSizePolicy(sizePolicy)
        self.Cancel.setStyleSheet(
            ".QPushButton{\n" "font: 13pt bold \"Arial\";\n" "border: 2px solid black;\n" "padding: 14px 28px;\n" "background-color: rgba(0,0,0,0);\n" "border-radius: 8px;\n" "color: white;\n" "}\n" "\n" ".pushButton {\n" "border-color: #2196F3;\n" "}\n" "\n" ".QPushButton::hover{\n" "color:black;\n" "border-color: white;\n" "}")
        self.Cancel.setObjectName("Cancel")
        self.Licenseplate = QtWidgets.QLineEdit(Form)
        self.Licenseplate.setGeometry(QtCore.QRect(380, 400, 219, 43))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.Licenseplate.sizePolicy().hasHeightForWidth())
        self.Licenseplate.setSizePolicy(sizePolicy)
        self.Licenseplate.setBaseSize(QtCore.QSize(0, 0))
        self.Licenseplate.setAutoFillBackground(False)
        self.Licenseplate.setStyleSheet("background-color: rgba(0,0,0,0);\n" "font: 12pt \"Arial\";")
        self.Licenseplate.setText("")
        self.Licenseplate.setFrame(True)
        self.Licenseplate.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Licenseplate.setObjectName("Licenseplate")
        self.LicensePlateLable = QtWidgets.QLabel(Form)
        self.LicensePlateLable.setGeometry(QtCore.QRect(170, 400, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LicensePlateLable.setFont(font)
        self.LicensePlateLable.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.LicensePlateLable.setStyleSheet(
            "background-color: rgba(0,0,0,0);\n" "\n" "border: 2px solid rgba(0,0,0,0);\n" "border-bottom-color:white;")
        self.LicensePlateLable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LicensePlateLable.setObjectName("LicensePlateLable")
        self.CarColorLable = QtWidgets.QLabel(Form)
        self.CarColorLable.setGeometry(QtCore.QRect(170, 710, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CarColorLable.setFont(font)
        self.CarColorLable.setStyleSheet(
            "background-color: rgba(0,0,0,0);\n" "border: 2px solid rgba(0,0,0,0);\n" "border-bottom-color:white;")
        self.CarColorLable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.CarColorLable.setObjectName("CarColorLable")
        self.CarTypeLable = QtWidgets.QLabel(Form)
        self.CarTypeLable.setGeometry(QtCore.QRect(170, 650, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CarTypeLable.setFont(font)
        self.CarTypeLable.setStyleSheet(
            "background-color: rgba(0,0,0,0);\n" "border: 2px solid rgba(0,0,0,0);\n" "border-bottom-color:white;")
        self.CarTypeLable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.CarTypeLable.setObjectName("CarTypeLable")
        self.PhoneLable = QtWidgets.QLabel(Form)
        self.PhoneLable.setGeometry(QtCore.QRect(170, 590, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PhoneLable.setFont(font)
        self.PhoneLable.setStyleSheet(
            "background-color: rgba(0,0,0,0);\n" "border: 2px solid rgba(0,0,0,0);\n" "border-bottom-color:white;")
        self.PhoneLable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PhoneLable.setObjectName("PhoneLable")
        self.NameLable = QtWidgets.QLabel(Form)
        self.NameLable.setGeometry(QtCore.QRect(170, 530, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NameLable.setFont(font)
        self.NameLable.setStyleSheet(
            "background-color: rgba(0,0,0,0);\n" "border: 2px solid rgba(0,0,0,0);\n" "border-bottom-color:white;")
        self.NameLable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.NameLable.setObjectName("NameLable")
        self.IDLable = QtWidgets.QLabel(Form)
        self.IDLable.setGeometry(QtCore.QRect(170, 460, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.IDLable.setFont(font)
        self.IDLable.setStyleSheet(
            "background-color: rgba(0,0,0,0);\n" "border: 2px solid rgba(0,0,0,0);\n" "border-bottom-color:white;")
        self.IDLable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.IDLable.setObjectName("IDLable")
        self.IDLineEdit = QtWidgets.QLineEdit(Form)
        self.IDLineEdit.setGeometry(QtCore.QRect(380, 460, 219, 43))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.IDLineEdit.sizePolicy().hasHeightForWidth())
        self.IDLineEdit.setSizePolicy(sizePolicy)
        self.IDLineEdit.setBaseSize(QtCore.QSize(0, 0))
        self.IDLineEdit.setAutoFillBackground(False)
        self.IDLineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n" "font: 12pt \"Arial\";")
        self.IDLineEdit.setText("")
        self.IDLineEdit.setFrame(True)
        self.IDLineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.IDLineEdit.setObjectName("IDLineEdit")
        self.NameLineEdit = QtWidgets.QLineEdit(Form)
        self.NameLineEdit.setGeometry(QtCore.QRect(380, 520, 219, 43))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.NameLineEdit.sizePolicy().hasHeightForWidth())
        self.NameLineEdit.setSizePolicy(sizePolicy)
        self.NameLineEdit.setBaseSize(QtCore.QSize(0, 0))
        self.NameLineEdit.setAutoFillBackground(False)
        self.NameLineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n" "font: 12pt \"Arial\";")
        self.NameLineEdit.setText("")
        self.NameLineEdit.setFrame(True)
        self.NameLineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.PhoneLineEdit = QtWidgets.QLineEdit(Form)
        self.PhoneLineEdit.setGeometry(QtCore.QRect(380, 580, 219, 43))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.PhoneLineEdit.sizePolicy().hasHeightForWidth())
        self.PhoneLineEdit.setSizePolicy(sizePolicy)
        self.PhoneLineEdit.setBaseSize(QtCore.QSize(0, 0))
        self.PhoneLineEdit.setAutoFillBackground(False)
        self.PhoneLineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n" "font: 12pt \"Arial\";")
        self.PhoneLineEdit.setText("")
        self.PhoneLineEdit.setFrame(True)
        self.PhoneLineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PhoneLineEdit.setObjectName("PhoneLineEdit")
        self.CarTypeLineEdit = QtWidgets.QLineEdit(Form)
        self.CarTypeLineEdit.setGeometry(QtCore.QRect(380, 640, 219, 43))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.CarTypeLineEdit.sizePolicy().hasHeightForWidth())
        self.CarTypeLineEdit.setSizePolicy(sizePolicy)
        self.CarTypeLineEdit.setBaseSize(QtCore.QSize(0, 0))
        self.CarTypeLineEdit.setAutoFillBackground(False)
        self.CarTypeLineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n" "font: 12pt \"Arial\";")
        self.CarTypeLineEdit.setText("")
        self.CarTypeLineEdit.setFrame(True)
        self.CarTypeLineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.CarTypeLineEdit.setObjectName("CarTypeLineEdit")
        self.CarColorLineEdit = QtWidgets.QLineEdit(Form)
        self.CarColorLineEdit.setGeometry(QtCore.QRect(380, 700, 219, 43))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.CarColorLineEdit.sizePolicy().hasHeightForWidth())
        self.CarColorLineEdit.setSizePolicy(sizePolicy)
        self.CarColorLineEdit.setBaseSize(QtCore.QSize(0, 0))
        self.CarColorLineEdit.setAutoFillBackground(False)
        self.CarColorLineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n" "font: 12pt \"Arial\";")
        self.CarColorLineEdit.setText("")
        self.CarColorLineEdit.setFrame(True)
        self.CarColorLineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.CarColorLineEdit.setObjectName("CarColorLineEdit")
        self.GenderLineEdit = QtWidgets.QLineEdit(Form)
        self.GenderLineEdit.setGeometry(QtCore.QRect(380, 760, 219, 43))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.GenderLineEdit.sizePolicy().hasHeightForWidth())
        self.GenderLineEdit.setSizePolicy(sizePolicy)
        self.GenderLineEdit.setBaseSize(QtCore.QSize(0, 0))
        self.GenderLineEdit.setAutoFillBackground(False)
        self.GenderLineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n" "font: 12pt \"Arial\";")
        self.GenderLineEdit.setText("")
        self.GenderLineEdit.setFrame(True)
        self.GenderLineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.GenderLineEdit.setObjectName("GenderLineEdit")
        self.GenderLable = QtWidgets.QLabel(Form)
        self.GenderLable.setGeometry(QtCore.QRect(170, 770, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)

        self.GenderLable.setFont(font)
        self.GenderLable.setStyleSheet(
            "background-color: rgba(0,0,0,0);\n""border: 2px solid rgba(0,0,0,0);\n""border-bottom-color:white;")
        self.GenderLable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.GenderLable.setObjectName("GenderLable")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Window = Form
        self.PrevWindow = PrevWindow
        self.PrevUI = PrevUI

        self.Cancel.clicked.connect(self.Clicked_GoBack)
        self.Confirm.clicked.connect(self.Clicked_AddToDB)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "License plate"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Car type"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Color"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Gender"))
        self.MsgBox.setText(_translate("Form", ""))
        self.Confirm.setText(_translate("Form", "Confirm"))
        self.Cancel.setText(_translate("Form", "Cancel"))
        self.LicensePlateLable.setText(_translate("Form", "License Plate"))
        self.CarColorLable.setText(_translate("Form", "Car color"))
        self.CarTypeLable.setText(_translate("Form", "Car type"))
        self.PhoneLable.setText(_translate("Form", "Phone"))
        self.NameLable.setText(_translate("Form", "Name"))
        self.IDLable.setText(_translate("Form", "ID"))
        self.GenderLable.setText(_translate("Form", "Gender"))

    def Clicked_AddToDB(self):
        global cursor
        global connection
        try:
            cursor.execute(
                'SELECT * FROM information WHERE (plate = "{}" OR ID = "{}");'.format(self.Licenseplate.text(),
                                                                                      self.IDLineEdit.text()))

            Info = cursor.fetchall()
            if len(Info) > 0 or self.Licenseplate.text() == '' or self.IDLineEdit.text() == '' or self.NameLineEdit.text() == '' or self.PhoneLineEdit.text() == '' or self.CarTypeLineEdit.text() == '' or self.CarColorLineEdit.text() == '' or self.GenderLineEdit.text() == '':
                self.MsgBox.setStyleSheet('color: white;' 'background-color: rgba(0,0,0,0);')
                self.MsgBox.setText("Invalid Data.")
                return

            cursor.execute(
                'INSERT INTO information VALUES ("{}","{}","{}","{}","{}","{}","{}");'.format(self.Licenseplate.text(),
                                                                                              self.IDLineEdit.text(),
                                                                                              self.NameLineEdit.text(),
                                                                                              self.PhoneLineEdit.text(),
                                                                                              self.CarTypeLineEdit.text(),
                                                                                              self.CarColorLineEdit.text(),
                                                                                              self.GenderLineEdit.text()))
            self.MsgBox.setStyleSheet('color: white;' 'background-color: rgba(0,0,0,0);')
            self.MsgBox.setText("Successfully Added.")
            connection.commit()
            self.Update_DB()

        except Exception as e:
            print(e)

    def Update_DB(self):
        try:
            global cursor
            cursor.execute("SELECT * FROM information")
            Info = cursor.fetchall()
            for Row, ColData in enumerate(Info):
                for Col, Data in enumerate(ColData):
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(Data))
                    self.tableWidget.setItem(Row, Col, item)

        except Exception as e:
            print(e)

    def Clicked_GoBack(self):
        self.Window.hide()


class UI_QueryDelPage(object):
    def __init__(self):
        self.Window = None
        self.PrevWindow = None
        self.PrevUI = None

    def setupUi(self, Form, PrevWindow, PrevUI):
        Form.setObjectName("Form")
        Form.resize(759, 658)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(759, 658))
        Form.setMaximumSize(QtCore.QSize(759, 658))
        font = QtGui.QFont()
        font.setUnderline(False)
        Form.setFont(font)
        Form.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));")
        self.MsgBox = QtWidgets.QLabel(Form)
        self.MsgBox.setGeometry(QtCore.QRect(150, 340, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.MsgBox.setFont(font)
        self.MsgBox.setStyleSheet("background-color: rgba(0,0,0,0);\n" "color: rgb(85, 170, 0);")
        self.MsgBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MsgBox.setObjectName("MsgBox")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 751, 301))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.EnterTheIDLable = QtWidgets.QLabel(Form)
        self.EnterTheIDLable.setGeometry(QtCore.QRect(230, 420, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.EnterTheIDLable.setFont(font)
        self.EnterTheIDLable.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.EnterTheIDLable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.EnterTheIDLable.setWordWrap(False)
        self.EnterTheIDLable.setObjectName("EnterTheIDLable")
        self.Confirm = QtWidgets.QPushButton(Form)
        self.Confirm.setGeometry(QtCore.QRect(270, 520, 229, 53))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Confirm.sizePolicy().hasHeightForWidth())
        self.Confirm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("13 Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Confirm.setFont(font)
        self.Confirm.setStyleSheet(
            ".QPushButton{\n" "font: 13pt bold \"Arial\";\n" "border: 2px solid black;\n" "padding: 14px 28px;\n" "background-color: rgba(0,0,0,0);\n" "border-radius: 8px;\n" "color: white;\n" "}\n" "\n" ".pushButton {\n" "border-color: #2196F3;\n" "}\n" "\n" ".QPushButton::hover{\n" "color:black;\n" "border-color: white;\n" "}")
        self.Confirm.setObjectName("Confirm")
        self.CancelButton = QtWidgets.QPushButton(Form)
        self.CancelButton.setGeometry(QtCore.QRect(270, 590, 229, 53))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CancelButton.sizePolicy().hasHeightForWidth())
        self.CancelButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("13 Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.CancelButton.setFont(font)
        self.CancelButton.setStyleSheet(
            ".QPushButton{\n" "font: 13pt bold \"Arial\";\n" "border: 2px solid black;\n" "padding: 14px 28px;\n" "background-color: rgba(0,0,0,0);\n" "border-radius: 8px;\n" "color: white;\n" "}\n" "\n" ".pushButton {\n" "border-color: #2196F3;\n" "}\n" "\n" ".QPushButton::hover{\n" "color:black;\n" "border-color: white;\n" "}")
        self.CancelButton.setObjectName("CancelButton")
        self.ID = QtWidgets.QLineEdit(Form)
        self.ID.setGeometry(QtCore.QRect(320, 470, 133, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.ID.sizePolicy().hasHeightForWidth())
        self.ID.setSizePolicy(sizePolicy)
        self.ID.setBaseSize(QtCore.QSize(0, 0))
        self.ID.setAutoFillBackground(False)
        self.ID.setStyleSheet("background-color: rgba(0,0,0,0);\n" "font: 12pt \"Arial\";")
        self.ID.setText("")
        self.ID.setFrame(True)
        self.ID.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ID.setObjectName("ID")
        self.IDLable = QtWidgets.QLabel(Form)
        self.IDLable.setGeometry(QtCore.QRect(290, 470, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.IDLable.setFont(font)
        self.IDLable.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.IDLable.setObjectName("IDLable")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Window = Form
        self.PrevWindow = PrevWindow
        self.PrevUI = PrevUI

        self.Confirm.clicked.connect(self.Clicked_DeleteRecord)
        self.CancelButton.clicked.connect(self.Clicked_GoBack)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.MsgBox.setText(_translate("Form", ""))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "License plate"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Car type"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Color"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Gender"))
        self.EnterTheIDLable.setText(_translate("Form", "Enter the ID of the query you want to delete."))
        self.Confirm.setText(_translate("Form", "Confirm"))
        self.CancelButton.setText(_translate("Form", "Cancel"))
        self.IDLable.setText(_translate("Form", "ID"))

    def Clicked_DeleteRecord(self):
        global cursor
        global connection
        try:
            cursor.execute('SELECT * FROM information WHERE ID = "{}"'.format(self.ID.text()))
            Info = cursor.fetchall()
            if len(Info) <= 0:
                self.MsgBox.setStyleSheet('color: white;' 'background-color: rgba(0,0,0,0);')
                self.MsgBox.setText("Record not found.")
                return

            cursor.execute('DELETE FROM information WHERE ID = "{}"'.format(self.ID.text()))
            self.MsgBox.setStyleSheet('color: white;' 'background-color: rgba(0,0,0,0);')
            self.MsgBox.setText("Successfully deleted.")

            connection.commit()
            self.Update_DB()

        except Exception as e:
            print(e)

    def Update_DB(self):
        try:
            global cursor
            self.tableWidget.clearContents()
            cursor.execute("SELECT * FROM information")
            Info = cursor.fetchall()
            for Row, ColData in enumerate(Info):
                for Col, Data in enumerate(ColData):
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(Data))
                    self.tableWidget.setItem(Row, Col, item)
        except Exception as e:
            print(e)

    def Clicked_GoBack(self):
        self.Window.hide()


class UI_Admin(object):
    def __init__(self):
        self.Window = None

        self.FrontUI = None
        self.FrontWindow = None

        self.QueryModPage = None
        self.QueryDelPage = None

        self.QueryDelUI = None
        self.QueryModUI = None

    def setupUi(self, LicensePlateProject, FrontPage, FrontUI):
        LicensePlateProject.setObjectName("LicensePlateProject")
        LicensePlateProject.resize(1029, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LicensePlateProject.sizePolicy().hasHeightForWidth())
        LicensePlateProject.setSizePolicy(sizePolicy)
        LicensePlateProject.setMinimumSize(QtCore.QSize(1029, 909))
        LicensePlateProject.setMaximumSize(QtCore.QSize(1029, 1000))

        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)

        LicensePlateProject.setFont(font)
        LicensePlateProject.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        LicensePlateProject.setStyleSheet(
            "font: 75 8pt \"System\";\n" "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));")
        LicensePlateProject.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        LicensePlateProject.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.centralwidget = QtWidgets.QWidget(LicensePlateProject)
        self.centralwidget.setObjectName("centralwidget")
        self.Frame = QtWidgets.QLabel(self.centralwidget)
        self.Frame.setGeometry(QtCore.QRect(10, 90, 600, 460))
        self.Frame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.Frame.setStyleSheet(
            "border:2px solid black;\n" "padding: 10px;\n" "border-radius: 25px;\n" "background-color:rgba(0,0,0,0);\n" "color: white;")
        self.Frame.setMidLineWidth(0)
        self.Frame.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Frame.setObjectName("Frame")
        self.StartDetection = QtWidgets.QPushButton(self.centralwidget)
        self.StartDetection.setGeometry(QtCore.QRect(20, 570, 241, 51))
        self.StartDetection.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.StartDetection.setStyleSheet(
            ".QPushButton{\n" "font: 13pt bold \"Arial\";\n" "border: 2px solid black;\n" "padding: 14px 28px;\n" "background-color: rgba(0,0,0,0);\n" "border-radius: 8px;\n" "color: white;\n" "}\n" "\n" ".pushButton {\n" "border-color: #2196F3;\n" "}\n" "\n" ".QPushButton::hover{\n" "color:black;\n" "border-color: white;\n" "}")
        self.StartDetection.setObjectName("StartDetection")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(340, 570, 241, 51))
        self.Exit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Exit.setStyleSheet(
            ".QPushButton{\n" "font: 13pt bold \"Arial\";\n" "border: 2px solid black;\n" "padding: 14px 28px;\n" "background-color: rgba(0,0,0,0);\n" "border-radius: 8px;\n" "color: white;\n" "}\n" "\n" ".pushButton {\n" "border-color: #2196F3;\n" "}\n" "\n" ".QPushButton::hover{\n" "color:black;\n" "border-color: white;\n" "}")
        self.Exit.setObjectName("Exit")
        self.LicensePlateImage = QtWidgets.QLabel(self.centralwidget)
        self.LicensePlateImage.setGeometry(QtCore.QRect(90, 760, 441, 171))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.LicensePlateImage.setFont(font)
        self.LicensePlateImage.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.LicensePlateImage.setText("")
        self.LicensePlateImage.setPixmap(QtGui.QPixmap(resource_path('GUI/Photos/Sc1.png')))
        self.LicensePlateImage.setScaledContents(True)
        self.LicensePlateImage.setObjectName("LicensePlateImage")

        self.ArabicNumb = QtWidgets.QLabel(self.centralwidget)
        self.ArabicNumb.setGeometry(QtCore.QRect(100, 770, 221, 71))
        self.ArabicNumb.setStyleSheet(
            "content-justify:center;\n""background: #ffffff;\n""color:#000000;\n""font: 75 30pt \"Arial\";")
        self.ArabicNumb.setText("")
        self.ArabicNumb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ArabicNumb.setObjectName("ArabicNumb")

        self.EnglishNumb = QtWidgets.QLabel(self.centralwidget)
        self.EnglishNumb.setGeometry(QtCore.QRect(100, 850, 221, 71))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.EnglishNumb.setFont(font)
        self.EnglishNumb.setStyleSheet(
            "content-justify:center;\n" "background: #ffffff;\n" "color:#000000;\n" "font: 75 30pt \"Arial\";")
        self.EnglishNumb.setText("")
        self.EnglishNumb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.EnglishNumb.setObjectName("EnglishNumb")

        self.ArabicLetter = QtWidgets.QLabel(self.centralwidget)
        self.ArabicLetter.setGeometry(QtCore.QRect(330, 770, 151, 71))
        self.ArabicLetter.setStyleSheet(
            "content-justify:center;\n" "background: #ffffff;\n" "color:#000000;\n" "font: 75 30pt \"Arial\";")
        self.ArabicLetter.setText("")
        self.ArabicLetter.setScaledContents(False)
        self.ArabicLetter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ArabicLetter.setObjectName("ArabicLetter")

        self.EnglishLetter = QtWidgets.QLabel(self.centralwidget)
        self.EnglishLetter.setGeometry(QtCore.QRect(330, 850, 151, 71))
        self.EnglishLetter.setStyleSheet(
            "content-justify:center;\n""background: #ffffff;\n""color:#000000;\n""font: 75 30pt \"Arial\";")
        self.EnglishLetter.setText("")
        self.EnglishLetter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.EnglishLetter.setObjectName("EnglishLetter")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(670, 90, 351, 651))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet(
            "background-color:rgb(179, 235, 255);\n" "border-radius: 25px;\n" "padding: 20px;\n" "background: #ffffff;\n" "color:#000000;")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableWidget.setLineWidth(25)
        self.tableWidget.setMidLineWidth(25)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setTextElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(147)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(82)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.GoBack = QtWidgets.QPushButton(self.centralwidget)
        self.GoBack.setGeometry(QtCore.QRect(170, 640, 241, 51))
        self.GoBack.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.GoBack.setStyleSheet(
            ".QPushButton{\n" "font: 13pt bold \"Arial\";\n" "border: 2px solid black;\n" "padding: 14px 28px;\n" "background-color: rgba(0,0,0,0);\n" "border-radius: 8px;\n" "color: white;\n" "}\n" "\n" ".pushButton {\n" "border-color: #2196F3;\n" "}\n" "\n" ".QPushButton::hover{\n" "color:black;\n" "border-color: white;\n" "}")
        self.GoBack.setObjectName("GoBack")
        self.name_msg = QtWidgets.QLabel(self.centralwidget)
        self.name_msg.setGeometry(QtCore.QRect(120, 10, 121, 29))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.name_msg.setFont(font)
        self.name_msg.setAutoFillBackground(False)
        self.name_msg.setStyleSheet(
            "color: rgb(85, 170, 0);\n" "background-color:rgba(0,0,0,0);\n" "border: 2px solid rgba(0,0,0,0);\n" "border-bottom-color:white;")
        self.name_msg.setLineWidth(5)
        self.name_msg.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.name_msg.setObjectName("name_msg")
        self.Logged_in_msg = QtWidgets.QLabel(self.centralwidget)
        self.Logged_in_msg.setGeometry(QtCore.QRect(20, 10, 101, 29))
        self.Logged_in_msg.setStyleSheet(
            "color:white;\n" "background-color:rgba(0,0,0,0);\n" "border: 2px solid rgba(0,0,0,0);\n" "border-bottom-color:white;")
        self.Logged_in_msg.setObjectName("Logged_in_msg")
        self.LableTableoflicenseplateholderinformation = QtWidgets.QLabel(self.centralwidget)
        self.LableTableoflicenseplateholderinformation.setGeometry(QtCore.QRect(710, 50, 271, 31))
        self.LableTableoflicenseplateholderinformation.setStyleSheet(
            "background-color:rgba(0,0,0,0);\n" "color: white;\n" "border: 2px solid black;\n" "border-radius: 8px;")
        self.LableTableoflicenseplateholderinformation.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LableTableoflicenseplateholderinformation.setObjectName("LableTableoflicenseplateholderinformation")
        self.StartDetection.raise_()
        self.Exit.raise_()
        self.LicensePlateImage.raise_()
        self.EnglishNumb.raise_()
        self.ArabicNumb.raise_()
        self.Frame.raise_()
        self.ArabicLetter.raise_()
        self.EnglishLetter.raise_()
        self.tableWidget.raise_()
        self.GoBack.raise_()
        self.name_msg.raise_()
        self.Logged_in_msg.raise_()
        self.LableTableoflicenseplateholderinformation.raise_()
        LicensePlateProject.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(LicensePlateProject)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1029, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuOptions = QtWidgets.QMenu(self.menuBar)
        self.menuOptions.setObjectName("menuOptions")
        LicensePlateProject.setMenuBar(self.menuBar)
        self.actionAdd_database_information = QtGui.QAction(LicensePlateProject)
        self.actionAdd_database_information.setObjectName("actionAdd_database_information")
        self.actionDelete_database_data = QtGui.QAction(LicensePlateProject)
        self.actionDelete_database_data.setObjectName("actionDelete_database_data")
        self.menuOptions.addAction(self.actionAdd_database_information)
        self.menuOptions.addAction(self.actionDelete_database_data)
        self.menuBar.addAction(self.menuOptions.menuAction())

        item = QtWidgets.QTableWidgetItem()
        item.setText('License plate')
        self.tableWidget.setItem(0, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('ID')
        self.tableWidget.setItem(1, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Name')
        self.tableWidget.setItem(2, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Phone')
        self.tableWidget.setItem(3, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Car type')
        self.tableWidget.setItem(4, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Color')
        self.tableWidget.setItem(5, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Gender')
        self.tableWidget.setItem(6, 0, item)

        self.StartDetection.clicked.connect(self.OnButtonPressed_DetectActivation)
        self.Exit.clicked.connect(ExitProgram)
        self.GoBack.clicked.connect(self.Clicked_SignOut)

        ### Creating sub widgets
        self.Window = LicensePlateProject
        self.FrontWindow = FrontPage
        self.FrontUI = FrontUI

        self.QueryModPage = QtWidgets.QMainWindow()
        self.QueryModUI = UI_QueryModPage()
        self.QueryModUI.setupUi(self.QueryModPage, LicensePlateProject, self)

        self.QueryDelPage = QtWidgets.QMainWindow()
        self.QueryDelUI = UI_QueryDelPage()
        self.QueryDelUI.setupUi(self.QueryDelPage, LicensePlateProject, self)

        self.actionAdd_database_information.triggered.connect(self.Clicked_OpenAddMenu)
        self.actionDelete_database_data.triggered.connect(self.Clicked_OpenDelMenu)

        self.retranslateUi(LicensePlateProject)
        QtCore.QMetaObject.connectSlotsByName(LicensePlateProject)

    def retranslateUi(self, LicensePlateProject):
        _translate = QtCore.QCoreApplication.translate
        LicensePlateProject.setWindowTitle(_translate("LicensePlateProject", "License Plate Detection and Recognition"))
        self.Frame.setText(_translate("LicensePlateProject", "Frame"))
        self.StartDetection.setText(_translate("LicensePlateProject", "Start Detection"))
        self.Exit.setText(_translate("LicensePlateProject", "Exit"))
        self.tableWidget.setSortingEnabled(False)
        self.GoBack.setText(_translate("LicensePlateProject", "Back"))
        self.name_msg.setText(_translate("LicensePlateProject", "Admin"))
        self.Logged_in_msg.setText(_translate("LicensePlateProject", "Logged in as:"))
        self.LableTableoflicenseplateholderinformation.setText(
            _translate("LicensePlateProject", "Table of license plate holder information"))
        self.menuOptions.setTitle(_translate("LicensePlateProject", "Options"))
        self.actionAdd_database_information.setText(_translate("LicensePlateProject", "Add database information"))
        self.actionDelete_database_data.setText(_translate("LicensePlateProject", "Delete database informaion"))

    def Clicked_OpenAddMenu(self):
        print("xx")
        self.QueryModPage.show()
        self.FrontUI.setDetect(False)
        self.QueryModUI.Update_DB()

    def Clicked_OpenDelMenu(self):
        self.QueryDelPage.show()
        self.FrontUI.setDetect(False)
        self.QueryDelUI.Update_DB()

    def Clicked_SignOut(self):
        self.FrontWindow.show()
        self.Window.hide()

    def Change_LoggedAs(self, username):
        self.name_msg.setText(username)

    def ShowResults(self, En_Letters, En_Numbers, Ar_Letters, Ar_Numbers):
        Search = En_Numbers + En_Letters
        cursor.execute('SELECT * FROM information WHERE plate like "{}"'.format(Search))
        Info = cursor.fetchall()

        for Idx, Row in enumerate(Info):
            for Col, value in enumerate(Row):
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(value))
                self.tableWidget.setItem(Col, 1, item)

        for Idx, Row in enumerate(Info):
            for Col, value in enumerate(Row):
                if Search == value:
                    self.EnglishLetter.setText(En_Letters)
                    self.EnglishNumb.setText(En_Numbers)
                    self.ArabicLetter.setText(Ar_Letters)
                    self.ArabicNumb.setText(Ar_Numbers)
                    break

    def OnButtonPressed_DetectActivation(self):
        try:
            if self.FrontUI.getDetect() is False:
                self.StartDetection.setText("Stop Detection")
                self.Frame.setPixmap(QPixmap('Out/Frame.png'))
                self.FrontUI.setDetect(True)
            else:
                self.StartDetection.setText("Start Detection")

                self.EnglishNumb.setText("")
                self.EnglishLetter.setText("")
                self.ArabicNumb.setText("")
                self.ArabicLetter.setText("")

                for x in range(self.tableWidget.rowCount()):
                    self.tableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem(''))

                self.Frame.setPixmap(QPixmap())

                self.FrontUI.setDetect(False)

        except Exception as e:
            print(e)


class UI_User(object):
    def __init__(self):
        self.Window = None
        self.FrontWindow = None
        self.FrontUI = None

    def setupUi(self, LicensePlateProject, FrontPage, FrontUI):
        LicensePlateProject.setObjectName("LicensePlateProject")
        LicensePlateProject.resize(1029, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LicensePlateProject.sizePolicy().hasHeightForWidth())
        LicensePlateProject.setSizePolicy(sizePolicy)
        LicensePlateProject.setMinimumSize(QtCore.QSize(1029, 909))
        LicensePlateProject.setMaximumSize(QtCore.QSize(1029, 1000))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        LicensePlateProject.setFont(font)
        LicensePlateProject.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        LicensePlateProject.setStyleSheet("font: 75 8pt \"System\";\n"
                                          "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));")
        LicensePlateProject.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        LicensePlateProject.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(LicensePlateProject)
        self.centralwidget.setObjectName("centralwidget")
        self.Frame = QtWidgets.QLabel(self.centralwidget)
        self.Frame.setGeometry(QtCore.QRect(10, 90, 600, 460))
        self.Frame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.Frame.setStyleSheet("border:2px solid black;\n"
                                 "padding: 10px;\n"
                                 "border-radius: 25px;\n"
                                 "background-color:rgba(0,0,0,0);\n"
                                 "color: white;")
        self.Frame.setMidLineWidth(0)
        self.Frame.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Frame.setObjectName("Frame")
        self.StartDetection = QtWidgets.QPushButton(self.centralwidget)
        self.StartDetection.setGeometry(QtCore.QRect(20, 570, 241, 51))
        self.StartDetection.setStyleSheet(".QPushButton{\n"
                                          "font: 13pt bold \"Arial\";\n"
                                          "border: 2px solid black;\n"
                                          "padding: 14px 28px;\n"
                                          "background-color: rgba(0,0,0,0);\n"
                                          "border-radius: 8px;\n"
                                          "color: white;\n"
                                          "}\n"
                                          "\n"
                                          ".pushButton {\n"
                                          "border-color: #2196F3;\n"
                                          "}\n"
                                          "\n"
                                          ".QPushButton::hover{\n"
                                          "color:black;\n"
                                          "border-color: white;\n"
                                          "}")
        self.StartDetection.setObjectName("StartDetection")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(360, 570, 241, 51))
        self.Exit.setStyleSheet(".QPushButton{\n"
                                "font: 13pt bold \"Arial\";\n"
                                "border: 2px solid black;\n"
                                "padding: 14px 28px;\n"
                                "background-color: rgba(0,0,0,0);\n"
                                "border-radius: 8px;\n"
                                "color: white;\n"
                                "}\n"
                                "\n"
                                ".pushButton {\n"
                                "border-color: #2196F3;\n"
                                "}\n"
                                "\n"
                                ".QPushButton::hover{\n"
                                "color:black;\n"
                                "border-color: white;\n"
                                "}")
        self.Exit.setObjectName("Exit")
        self.LicensePlateImage = QtWidgets.QLabel(self.centralwidget)
        self.LicensePlateImage.setGeometry(QtCore.QRect(140, 730, 441, 171))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(20)
        self.LicensePlateImage.setFont(font)
        self.LicensePlateImage.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.LicensePlateImage.setText("")
        self.LicensePlateImage.setPixmap(QtGui.QPixmap(resource_path('GUI/Photos/Sc1.png')))
        self.LicensePlateImage.setScaledContents(True)
        self.LicensePlateImage.setObjectName("LicensePlateImage")

        self.ArabicNumb = QtWidgets.QLabel(self.centralwidget)
        self.ArabicNumb.setGeometry(QtCore.QRect(150, 740, 221, 71))
        self.ArabicNumb.setStyleSheet(
            "content-justify:center;\n""background: #ffffff;\n""color:#000000;\n""font: 75 30pt \"Arial\";")
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.ArabicNumb.setText("")
        self.ArabicNumb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ArabicNumb.setObjectName("ArabicNumb")

        self.EnglishNumb = QtWidgets.QLabel(self.centralwidget)
        self.EnglishNumb.setGeometry(QtCore.QRect(150, 820, 221, 71))
        self.EnglishNumb.setFont(font)
        self.EnglishNumb.setStyleSheet(
            "content-justify:center;\n""background: #ffffff;\n""color:#000000;\n""font: 75 30pt \"Arial\";")
        self.EnglishNumb.setText("")
        self.EnglishNumb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.EnglishNumb.setObjectName("EnglishNumb")

        self.ArabicLetter = QtWidgets.QLabel(self.centralwidget)
        self.ArabicLetter.setGeometry(QtCore.QRect(380, 740, 151, 71))
        self.ArabicLetter.setStyleSheet(
            "content-justify:center;\n""background: #ffffff;\n""color:#000000;\n""font: 75 30pt \"Arial\";")
        self.ArabicLetter.setText("")
        self.ArabicLetter.setScaledContents(False)
        self.ArabicLetter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ArabicLetter.setObjectName("ArabicLetter")

        self.EnglishLetter = QtWidgets.QLabel(self.centralwidget)
        self.EnglishLetter.setGeometry(QtCore.QRect(380, 820, 151, 71))
        self.EnglishLetter.setStyleSheet(
            "content-justify:center;\n""background: #ffffff;\n""color:#000000;\n""font: 75 30pt \"Arial\";")
        self.EnglishLetter.setText("")
        self.EnglishLetter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.EnglishLetter.setObjectName("EnglishLetter")

        self.GoBack = QtWidgets.QPushButton(self.centralwidget)
        self.GoBack.setGeometry(QtCore.QRect(190, 640, 241, 51))
        self.GoBack.setStyleSheet(".QPushButton{\n"
                                  "font: 13pt bold \"Arial\";\n"
                                  "border: 2px solid black;\n"
                                  "padding: 14px 28px;\n"
                                  "background-color: rgba(0,0,0,0);\n"
                                  "border-radius: 8px;\n"
                                  "color: white;\n"
                                  "}\n"
                                  "\n"
                                  ".pushButton {\n"
                                  "border-color: #2196F3;\n"
                                  "}\n"
                                  "\n"
                                  ".QPushButton::hover{\n"
                                  "color:black;\n"
                                  "border-color: white;\n"
                                  "}")
        self.GoBack.setObjectName("GoBack")

        self.name_msg = QtWidgets.QLabel(self.centralwidget)
        self.name_msg.setGeometry(QtCore.QRect(120, 10, 121, 29))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.name_msg.setFont(font)
        self.name_msg.setAutoFillBackground(False)
        self.name_msg.setStyleSheet("color: rgb(85, 170, 0);\n"
                                    "background-color:rgba(0,0,0,0);\n"
                                    "border: 2px solid rgba(0,0,0,0);\n"
                                    "border-bottom-color:white;")
        self.name_msg.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.name_msg.setObjectName("name_msg")
        self.Logged_in_msg = QtWidgets.QLabel(self.centralwidget)
        self.Logged_in_msg.setGeometry(QtCore.QRect(20, 10, 101, 29))
        self.Logged_in_msg.setStyleSheet("color:white;\n"
                                         "background-color:rgba(0,0,0,0);\n"
                                         "border: 2px solid rgba(0,0,0,0);\n"
                                         "border-bottom-color:white;")
        self.Logged_in_msg.setObjectName("Logged_in_msg")
        self.StartDetection.raise_()
        self.Exit.raise_()
        self.LicensePlateImage.raise_()
        self.EnglishNumb.raise_()
        self.ArabicNumb.raise_()
        self.Frame.raise_()
        self.ArabicLetter.raise_()
        self.EnglishLetter.raise_()
        self.GoBack.raise_()
        self.name_msg.raise_()
        self.Logged_in_msg.raise_()

        LicensePlateProject.setCentralWidget(self.centralwidget)

        self.actionAdd_License_plate = QtGui.QAction(LicensePlateProject)
        self.actionAdd_License_plate.setObjectName("actionAdd_License_plate")
        self.actionModify_License_plates = QtGui.QAction(LicensePlateProject)
        self.actionModify_License_plates.setObjectName("actionModify_License_plates")
        self.actionDelete_License_plate = QtGui.QAction(LicensePlateProject)
        self.actionDelete_License_plate.setObjectName("actionDelete_License_plate")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(670, 90, 351, 651))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet(
            "background-color:rgb(179, 235, 255);\n" "border-radius: 25px;\n" "padding: 20px;\n" "background: #ffffff;\n" "color:#000000;")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableWidget.setLineWidth(25)
        self.tableWidget.setMidLineWidth(25)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setTextElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(147)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(82)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.LableTableoflicenseplateholderinformation = QtWidgets.QLabel(self.centralwidget)
        self.LableTableoflicenseplateholderinformation.setGeometry(QtCore.QRect(710, 50, 271, 31))
        self.LableTableoflicenseplateholderinformation.setStyleSheet(
            "background-color:rgba(0,0,0,0);\n" "color: white;\n" "border: 2px solid black;\n" "border-radius: 8px;")
        self.LableTableoflicenseplateholderinformation.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LableTableoflicenseplateholderinformation.setObjectName("LableTableoflicenseplateholderinformation")
        self.StartDetection.raise_()

        self.LableTableoflicenseplateholderinformation.raise_()
        LicensePlateProject.setCentralWidget(self.centralwidget)

        item = QtWidgets.QTableWidgetItem()
        item.setText('License plate')
        self.tableWidget.setItem(0, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('ID')
        self.tableWidget.setItem(1, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Name')
        self.tableWidget.setItem(2, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Phone')
        self.tableWidget.setItem(3, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Car type')
        self.tableWidget.setItem(4, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Color')
        self.tableWidget.setItem(5, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText('Gender')
        self.tableWidget.setItem(6, 0, item)

        self.retranslateUi(LicensePlateProject)
        QtCore.QMetaObject.connectSlotsByName(LicensePlateProject)

        self.Window = LicensePlateProject
        self.FrontWindow = FrontPage
        self.FrontUI = FrontUI

        self.StartDetection.clicked.connect(self.OnButtonPressed_DetectActivation)
        self.GoBack.clicked.connect(self.Clicked_SignOut)
        self.Exit.clicked.connect(ExitProgram)

    def retranslateUi(self, LicensePlateProject):
        _translate = QtCore.QCoreApplication.translate
        LicensePlateProject.setWindowTitle(_translate("LicensePlateProject", "License Plate Detection and Recognition"))
        self.Frame.setText(_translate("LicensePlateProject", "Frame"))
        self.StartDetection.setText(_translate("LicensePlateProject", "Start Detection"))
        self.LableTableoflicenseplateholderinformation.setText(
            _translate("LicensePlateProject", "Table of license plate holder information"))
        self.Exit.setText(_translate("LicensePlateProject", "Exit"))
        self.GoBack.setText(_translate("LicensePlateProject", "Back"))
        self.name_msg.setText(_translate("LicensePlateProject", "Admin"))
        self.Logged_in_msg.setText(_translate("LicensePlateProject", "Logged in as:"))

    def Clicked_SignOut(self):
        self.Window.hide()
        self.FrontWindow.show()
        self.FrontUI.setDetect(False)

    def Change_LoggedAs(self, username):
        self.name_msg.setText(username)

    def ShowResults(self, En_Letters, En_Numbers, Ar_Letters, Ar_Numbers):
        Search = En_Numbers + En_Letters
        cursor.execute('SELECT * FROM information WHERE plate like "{}"'.format(Search))
        Info = cursor.fetchall()

        for Idx, Row in enumerate(Info):
            for Col, value in enumerate(Row):
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(value))
                self.tableWidget.setItem(Col, 1, item)

        for Idx, Row in enumerate(Info):
            for Col, value in enumerate(Row):
                if Search == value:
                    self.EnglishLetter.setText(En_Letters)
                    self.EnglishNumb.setText(En_Numbers)
                    self.ArabicLetter.setText(Ar_Letters)
                    self.ArabicNumb.setText(Ar_Numbers)
                    break

    def OnButtonPressed_DetectActivation(self):
        try:
            if self.FrontUI.getDetect() is False:
                self.StartDetection.setText("Stop Detection")
                self.Frame.setPixmap(QPixmap('Out/Frame.png'))
                self.FrontUI.setDetect(True)
            else:
                self.StartDetection.setText("Start Detection")
                self.EnglishNumb.setText("")
                self.EnglishLetter.setText("")
                self.ArabicNumb.setText("")
                self.ArabicLetter.setText("")

                self.Frame.setPixmap(QPixmap())
                self.FrontUI.setDetect(False)

                for x in range(self.tableWidget.rowCount()):
                    self.tableWidget.setItem(x, 1, QtWidgets.QTableWidgetItem(''))

                self.Frame.setPixmap(QPixmap())
                self.FrontUI.setDetect(False)

        except Exception as e:
            print(e)


class UI_LoginPage(object):

    def __init__(self):
        self.Window = None

        self.FrontWindow = None

        self.RegisterWindow = None

        self.AdminWindow = None
        self.UserWindow = None

        self.Admin_UI = None
        self.User_UI = None

        self.ForgotPass_UI = None
        self.ForgotPass_Window = None

        self.LoginAttempt = 0
        self.LoginNoneAttempt = 0
        self.LastUsername = ''

    def setupGUI(self, Admin_UI, User_UI):
        self.Admin_UI = Admin_UI
        self.User_UI = User_UI

    def setupUi(self, MainWindow, FrontWindow, RegisterWindow, AdminWindow, UserWindow, ForgotPassWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 547)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(425, 547))
        MainWindow.setMaximumSize(QtCore.QSize(425, 547))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SingintoLable = QtWidgets.QLabel(self.centralwidget)
        self.SingintoLable.setGeometry(QtCore.QRect(80, 100, 271, 31))
        self.SingintoLable.setStyleSheet(
            "font: 75 15pt \"Arial\";\n""background-color: rgba(0,0,0,0);\n""color: white;")
        self.SingintoLable.setObjectName("SingintoLable")
        self.welcome_2Lable = QtWidgets.QLabel(self.centralwidget)
        self.welcome_2Lable.setGeometry(QtCore.QRect(150, 40, 121, 51))
        self.welcome_2Lable.setStyleSheet(
            "font: 75 35pt \"Arial\";\n""background-color: rgba(0,0,0,0);\n""color: white;")
        self.welcome_2Lable.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.welcome_2Lable.setScaledContents(False)
        self.welcome_2Lable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.welcome_2Lable.setObjectName("welcome_2Lable")
        self.LoginButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton_2.setGeometry(QtCore.QRect(110, 380, 211, 51))
        self.LoginButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.LoginButton_2.setStyleSheet(
            ".QPushButton{\n" "font: 12pt bold \"Arial\";\n" "border: 2px solid black;\n" "padding: 14px 28px;\n" "background-color: rgba(0,0,0,0);\n" "color: white;\n" "}\n" "\n" ".pushButton {\n" "border-color: #2196F3;\n" "color: dodgerblue;\n" "}\n" "\n" ".QPushButton::hover{\n" "color:black;\n" "border-color: white;\n" "}")
        self.LoginButton_2.setObjectName("LoginButton_2")

        self.UsernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.UsernameInput.setGeometry(QtCore.QRect(80, 220, 271, 31))
        self.UsernameInput.setStyleSheet(
            "border: 2px solid rgba(0,0,0,0);\n" "font: 12pt \"Arial\";\n" "background-color: rgba(0,0,0,0);\n" "color:white;\n" "padding-bottom: 7px;\n" "border-bottom-color:white;")
        self.UsernameInput.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.VisualMoveStyle)
        self.UsernameInput.setObjectName("UsernameInput")

        self.PasswordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.PasswordInput.setGeometry(QtCore.QRect(80, 310, 271, 31))
        self.PasswordInput.setStyleSheet(
            "border: 2px solid rgba(0,0,0,0);\n" "font: 12pt \"Arial\";\n" "background-color: rgba(0,0,0,0);\n" "color:white;\n" "padding-bottom: 7px;\n" "border-bottom-color:white;")
        self.PasswordInput.setObjectName("PasswordInput")

        self.LableDontHaveAnAccount = QtWidgets.QLabel(self.centralwidget)
        self.LableDontHaveAnAccount.setGeometry(QtCore.QRect(80, 520, 181, 21))
        self.LableDontHaveAnAccount.setStyleSheet(
            "font: 75  bold 12pt \"Arial\";\n""background-color: rgba(0,0,0,0);\n""color: white;")
        self.LableDontHaveAnAccount.setObjectName("LableDontHaveAnAccount")

        self.MoveToSignUpPage = QtWidgets.QPushButton(self.centralwidget)
        self.MoveToSignUpPage.setGeometry(QtCore.QRect(260, 520, 101, 23))
        self.MoveToSignUpPage.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.MoveToSignUpPage.setStyleSheet(
            "font: 75  bold 12pt \"Arial\";\n" "background-color: rgba(0,0,0,0);\n" "color: rgb(3, 215, 252);")
        self.MoveToSignUpPage.setObjectName("MoveToSignUpPage")

        self.MoveToForgotPage = QtWidgets.QPushButton(self.centralwidget)
        self.MoveToForgotPage.setGeometry(QtCore.QRect(120, 480, 181, 21))
        self.MoveToForgotPage.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.MoveToForgotPage.setStyleSheet(
            "font: 75  bold 12pt \"Arial\";\n" "background-color: rgba(0,0,0,0);\n" "color: white;")
        self.MoveToForgotPage.setObjectName("MoveToSignUpPage1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.welcome_2Lable.setBuddy(MainWindow)

        self.MsgBox = QtWidgets.QLabel(self.centralwidget)
        self.MsgBox.setGeometry(QtCore.QRect(70, 140, 290, 41))
        self.MsgBox.setAutoFillBackground(False)
        self.MsgBox.setStyleSheet("background-color: rgba(0,0,0,0);\n" "color: rgb(85, 170, 0);")
        self.MsgBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MsgBox.setObjectName("MsgBox")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Window = MainWindow
        self.FrontWindow = FrontWindow
        self.RegisterWindow = RegisterWindow
        self.AdminWindow = AdminWindow
        self.UserWindow = UserWindow

        self.MoveToSignUpPage.clicked.connect(self.Clicked_Register)
        self.MoveToForgotPage.clicked.connect(self.Clicked_ForgotPass)
        self.LoginButton_2.clicked.connect(self.Clicked_CheckLogin)
        self.ForgotPass_Window = ForgotPassWindow


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SingintoLable.setText(_translate("MainWindow", "Sign into your existing account"))
        self.welcome_2Lable.setText(_translate("MainWindow", "Login"))
        self.LoginButton_2.setText(_translate("MainWindow", "Login"))
        self.UsernameInput.setPlaceholderText(_translate("MainWindow", "Username"))
        self.PasswordInput.setPlaceholderText(_translate("MainWindow", "Password"))
        self.LableDontHaveAnAccount.setText(_translate("MainWindow", "Don\'t have an account?"))
        self.MoveToSignUpPage.setText(_translate("MainWindow", "SignUp now"))
        self.MoveToForgotPage.setText(_translate("MainWindow", "Forgot your Pass"))

    def Admin_Window(self):
        self.Window.hide()
        self.AdminWindow.show()

    def User_Window(self):
        self.Window.hide()
        self.UserWindow.show()

    def Clicked_ForgotPass(self):
        try:
            self.ForgotPass_Window.show()
        except Exception as e:
            print(e)

    def Clicked_CheckLogin(self):
        try:
            global cursor
            cursor.execute('SELECT username FROM users WHERE username = "{}" AND password = "{}"'.format(
                str(self.UsernameInput.text()), self.PasswordInput.text()))
            Info = cursor.fetchall()

            U_Name = 'none'
            for Row, Col in enumerate(Info):
                for idx, n in enumerate(Col):
                    U_Name = n

            if len(Info) > 0:
                global privilege
                if U_Name == 'admin':
                    self.Admin_Window()
                    self.Admin_UI.Change_LoggedAs(U_Name)
                    privilege = Privilege.admin

                else:
                    self.User_Window()
                    self.User_UI.Change_LoggedAs(U_Name)
                    privilege = Privilege.user

                self.MsgBox.setText("")
                self.Window.hide()
                print(("{}".format(privilege.name)))

            else:
                self.MsgBox.setStyleSheet("color:white;\n" "font: 12pt \"Arial\";" 'background-color: rgba(0,0,0,0);')

                cursor.execute('SELECT username FROM users WHERE username = "{}"'.format(self.UsernameInput.text()))
                Info2 = cursor.fetchall()
                U_Name = 'none'
                for Row, Col in enumerate(Info2):
                    for idx, n in enumerate(Col):
                        U_Name = n

                print(U_Name)
                self.LoginNoneAttempt = self.LoginNoneAttempt + 1
                self.LoginAttempt = self.LoginAttempt + 1

                if self.LoginAttempt >= 3 and U_Name != 'none':
                    self.LoginNoneAttempt = 0
                    cursor.execute('SELECT hint FROM users WHERE username = "{}"'.format(self.UsernameInput.text()))
                    Info3 = cursor.fetchall()

                    for Row, Col in enumerate(Info3):
                        for idx, n in enumerate(Col):
                            self.MsgBox.setText('Wrong attempt {}'.format(self.LoginAttempt)+'\n'+"your hint is: " + n)
                elif U_Name == 'none' and self.LoginAttempt >= 3:
                    self.LoginNoneAttempt = 0
                else:
                    self.MsgBox.setText('Wrong attempt {}'.format(self.LoginNoneAttempt))



        except mysql.connector.Error as Error:
            print(Error)
            # self.MsgBox.setText('Something wrong')
            # self.MsgBox.setStyleSheet("color:#FF0000;\n")

    def Clicked_Register(self):
        self.Window.hide()
        self.RegisterWindow.show()

class UI_ForgotPassword(object):

    def __init__(self):
        self.RegisterWindow = None
        self.Window = None

    def setupUi(self, MainWindow):
        self.Window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(465, 600))
        MainWindow.setMaximumSize(QtCore.QSize(465, 600))
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));")


        self.headerlable = QtWidgets.QLabel(self.centralwidget)
        self.headerlable.setGeometry(QtCore.QRect(50, 30, 361, 41))


        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)

        self.headerlable.setFont(font)
        self.headerlable.setObjectName("headerlable")
        self.headerlable.setStyleSheet("background-color: rgba(0,0,0,0);\n" "color: Black;")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 280, 300, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("What high school did you attend?")
        self.comboBox.addItem("In what city were you born?")
        self.comboBox.addItem("What was your favorite food as a child?")
        self.comboBox.addItem("What is your first car?")
        self.comboBox.setStyleSheet("color:white;\n" "font: 12pt \"Arial\";")

        self.answerquestion = QtWidgets.QLineEdit(self.centralwidget)
        self.answerquestion.setGeometry(QtCore.QRect(100, 370, 261, 31))
        self.answerquestion.setObjectName("answerquestion")
        self.answerquestion.setStyleSheet("background-color:rgba(0,0,0,0);\n" "font: 14pt \"Arial\";" "color: white;")

        self.chooselable = QtWidgets.QLabel(self.centralwidget)
        self.chooselable.setGeometry(QtCore.QRect(100, 240, 261, 31))
        self.chooselable.setStyleSheet("background-color:rgba(0,0,0,0);\n" "font: 14pt \"Arial\";")
        self.chooselable.setObjectName("chooselable")

        self.forgotpassbutton = QtWidgets.QPushButton(self.centralwidget)
        self.forgotpassbutton.setGeometry(QtCore.QRect(130, 440, 211, 51))
        self.forgotpassbutton.setStyleSheet(
            ".QPushButton{\n" "font: 12pt bold \"Arial\";\n" "border: 2px solid black;\n" "padding: 14px 28px;\n" "background-color: rgba(0,0,0,0);\n" "color: white;\n" "}\n" "\n" ".pushButton {\n" "border-color: #2196F3;\n" "color: dodgerblue;\n" "}\n" "\n" ".QPushButton::hover{\n" "color:black;\n" "border-color: white;\n" "}")
        self.forgotpassbutton.setObjectName("forgotpassbutton")
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(100, 170, 271, 31))
        self.Username.setObjectName("Username")
        self.Username.setStyleSheet("background-color:rgba(0,0,0,0);\n" "font: 14pt \"Arial\";" "color: white;")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 110, 220, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-color: rgba(0,0,0,0);\n" "color: rgb(85, 170, 0);")

        self.Backbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Backbutton.setGeometry(QtCore.QRect(130, 500, 211, 51))
        self.Backbutton.setObjectName("Backbutton")
        self.Backbutton.setStyleSheet(
            ".QPushButton{\n" "font: 12pt bold \"Arial\";\n" "border: 2px solid black;\n" "padding: 14px 28px;\n" "background-color: rgba(0,0,0,0);\n" "color: white;\n" "}\n" "\n" ".pushButton {\n" "border-color: #2196F3;\n" "color: dodgerblue;\n" "}\n" "\n" ".QPushButton::hover{\n" "color:black;\n" "border-color: white;\n" "}")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("background-color: rgba(0,0,0,0);")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Backbutton.clicked.connect(self.Clicked_CloseWindow)
        self.forgotpassbutton.clicked.connect(self.Clicked_ForgotPass)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headerlable.setText(_translate("MainWindow", "Forgot Your Password"))
        self.answerquestion.setPlaceholderText(_translate("MainWindow", "Answer"))
        self.chooselable.setText(_translate("MainWindow", "Choose your security question"))
        self.forgotpassbutton.setText(_translate("MainWindow", "Forgot Password"))
        self.Username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.Backbutton.setText(_translate("MainWindow", "Back"))

    def Clicked_CloseWindow(self):
        try:
            self.Window.hide()
            self.headerlable.setText("Forgot Your Password")
            self.answerquestion.setPlaceholderText("Answer")
            self.chooselable.setText("Choose your security question")
            self.forgotpassbutton.setText("Forgot Password")
            self.Username.setText("")
            self.Username.setPlaceholderText("Username")
            self.Backbutton.setText("Back")
            self.label_2.setText("")
            self.answerquestion.setText("")
        except Exception as e:
            print(e)

    def Clicked_ForgotPass(self):
        self.label_2.setStyleSheet("color:white;\n" "font: 12pt \"Arial\";" 'background-color: rgba(0,0,0,0);')
        self.label_2.setText("")

        try:
            global cursor
            cursor.execute('SELECT username FROM questions WHERE username = "{}"'.format(self.Username.text()))
            Info = cursor.fetchall()
            if len(Info) > 0:
                cursor.execute('SELECT * FROM questions WHERE username = "{}" AND questionID = "{}" AND answer = "{}"'.format(self.Username.text(),self.comboBox.currentIndex(),self.answerquestion.text()))
                Info2 = cursor.fetchall()
                if len(Info2) > 0:
                    cursor.execute('SELECT password FROM users WHERE username = "{}"'.format(self.Username.text()))
                    Info3 = cursor.fetchall()
                    P_Name = 'none'
                    for Row, Col in enumerate(Info3):
                        for idx, n in enumerate(Col):
                            self.label_2.setText("The password is: "+n)
                else:
                    if self.answerquestion.text() == '' or self.answerquestion.text().isspace():
                        self.label_2.setText("you must answer the question")
                    else:
                        self.label_2.setText("Wrong Question or answer")
            else:
                if self.Username.text() == '' or self.Username.text().isspace():
                    self.label_2.setText("you have to enter the username")
                else:
                    self.label_2.setText("Wrong Username")
        except Exception as e:
            print(e)

class UI_RegisterPage(object):
    def __init__(self):
        self.Window = None
        self.FrontWindow = None
        self.LoginWindow = None

    def setupUi(self, MainWindow, FrontWindow, LoginWindow):
        MainWindow.resize(425, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(425, 768))
        MainWindow.setMaximumSize(QtCore.QSize(425, 768))

        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RegisterLable = QtWidgets.QLabel(self.centralwidget)
        self.RegisterLable.setGeometry(QtCore.QRect(110, 100, 201, 31))
        self.RegisterLable.setStyleSheet(
            "font: 75 15pt \"Arial\";\n" "background-color: rgba(0,0,0,0);\n" "color: white;")
        self.RegisterLable.setObjectName("RegisterLable")

        self.RegisterLable_2 = QtWidgets.QLabel(self.centralwidget)
        self.RegisterLable_2.setGeometry(QtCore.QRect(110, 40, 191, 51))
        self.RegisterLable_2.setStyleSheet(
            "font: 75 35pt \"Arial\";\n" "background-color: rgba(0,0,0,0);\n" "color: white;")
        self.RegisterLable_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.RegisterLable_2.setScaledContents(False)
        self.RegisterLable_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.RegisterLable_2.setObjectName("RegisterLable_2")

        self.RegisterButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterButton.setGeometry(QtCore.QRect(110, 680, 211, 51))
        self.RegisterButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.RegisterButton.setStyleSheet(
            ".QPushButton{\n" "font: 12pt bold \"Arial\";\n" "border: 2px solid black;\n" "padding: 14px 28px;\n" "background-color: rgba(0,0,0,0);\n" "color: white;\n" "}\n" "\n" ".pushButton {\n" "border-color: #2196F3;\n" "color: dodgerblue;\n" "}\n" "\n" ".QPushButton::hover{\n" "color:black;\n" "border-color: white;\n" "}")
        self.RegisterButton.setObjectName("RegisterButton")

        self.UsernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.UsernameInput.setGeometry(QtCore.QRect(80, 210, 271, 31))
        self.UsernameInput.setStyleSheet(
            "border: 2px solid rgba(0,0,0,0);\n" "font: 12pt \"Arial\";\n" "background-color: rgba(0,0,0,0);\n" "color:white;\n" "padding-bottom: 7px;\n" "border-bottom-color:white;")
        self.UsernameInput.setObjectName("UsernameInput")

        self.PasswordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.PasswordInput.setGeometry(QtCore.QRect(80, 390, 271, 31))
        self.PasswordInput.setStyleSheet(
            "border: 2px solid rgba(0,0,0,0);\n" "font: 12pt \"Arial\";\n" "background-color: rgba(0,0,0,0);\n" "color:white;\n" "padding-bottom: 7px;\n" "border-bottom-color:white;")
        self.PasswordInput.setObjectName("PasswordInput")

        self.Hint = QtWidgets.QLineEdit(self.centralwidget)
        self.Hint.setGeometry(QtCore.QRect(80, 480, 271, 31))
        self.Hint.setStyleSheet(
            "border: 2px solid rgba(0,0,0,0);\n" "font: 12pt \"Arial\";\n" "background-color: rgba(0,0,0,0);\n" "color:white;\n" "padding-bottom: 7px;\n" "border-bottom-color:white;")
        self.Hint.setObjectName("HintMsg")

        self.combobox1 = QtWidgets.QComboBox(self.centralwidget)
        self.combobox1.addItem("What high school did you attend?")
        self.combobox1.addItem("In what city were you born?")
        self.combobox1.addItem("What was your favorite food as a child?")
        self.combobox1.addItem("What is your first car?")
        self.combobox1.setGeometry(QtCore.QRect(80, 560, 271, 31))

        self.QuestionAnswer = QtWidgets.QLineEdit(self.centralwidget)
        self.QuestionAnswer.setGeometry(QtCore.QRect(80, 570 + 50, 271, 31))
        self.QuestionAnswer.setStyleSheet(
            "border: 2px solid rgba(0,0,0,0);\n" "font: 12pt \"Arial\";\n" "background-color: rgba(0,0,0,0);\n" "color:white;\n" "padding-bottom: 7px;\n" "border-bottom-color:white;")
        self.QuestionAnswer.setObjectName("QuestionAnswer")

        self.EmailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.EmailInput.setGeometry(QtCore.QRect(80, 300, 271, 31))
        self.EmailInput.setStyleSheet(
            "font: 12pt \"Arial\";\n" "background-color: rgba(0,0,0,0);\n" "color:white;\n" "padding-bottom: 7px;\n" "border: 2px solid rgba(0,0,0,0);\n" "border-bottom-color:white;")
        self.EmailInput.setObjectName("EmailInput")

        self.Haveanaccount = QtWidgets.QLabel(self.centralwidget)
        self.Haveanaccount.setGeometry(QtCore.QRect(120, 740, 141, 21))
        self.Haveanaccount.setStyleSheet(
            "font: 75  bold 12pt \"Arial\";\n" "background-color: rgba(0,0,0,0);\n" "color: white;")
        self.Haveanaccount.setObjectName("Haveanaccount")

        self.MoveToLoginPage = QtWidgets.QPushButton(self.centralwidget)
        self.MoveToLoginPage.setGeometry(QtCore.QRect(260, 740, 51, 23))
        self.MoveToLoginPage.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.MoveToLoginPage.setStyleSheet(
            "font: 75  bold 12pt \"Arial\";\n" "background-color: rgba(0,0,0,0);\n" "color: rgb(3, 215, 252);")
        self.MoveToLoginPage.setObjectName("MoveToLoginPage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.RegisterLable_2.setBuddy(MainWindow)

        self.MsgBox = QtWidgets.QLabel(self.centralwidget)
        self.MsgBox.setGeometry(QtCore.QRect(80, 152, 250, 31))
        self.MsgBox.setStyleSheet("background-color: rgba(0,0,0,0);\n" "color: rgb(0, 170, 0);")
        self.MsgBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MsgBox.setObjectName("MsgBox")
        self.MsgBox.setAutoFillBackground(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Window = MainWindow
        self.FrontWindow = FrontWindow
        self.LoginWindow = LoginWindow
        self.MoveToLoginPage.clicked.connect(self.Clicked_GoBack)
        self.RegisterButton.clicked.connect(self.Clicked_AddToDatabase)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RegisterLable.setText(_translate("MainWindow", "Create a new account"))
        self.RegisterLable_2.setText(_translate("MainWindow", "Register"))
        self.RegisterButton.setText(_translate("MainWindow", "Register"))
        self.UsernameInput.setPlaceholderText(_translate("MainWindow", "Username"))
        self.PasswordInput.setPlaceholderText(_translate("MainWindow", "Password"))
        self.EmailInput.setPlaceholderText(_translate("MainWindow", "Email"))
        self.Haveanaccount.setText(_translate("MainWindow", "Have an account?"))
        self.MoveToLoginPage.setText(_translate("MainWindow", "Login"))
        self.QuestionAnswer.setPlaceholderText(_translate("MainWindow", "Question Answer"))
        self.Hint.setPlaceholderText(_translate("MainWindow", "Hint"))

    def LoginWindow(self):
        self.LoginWindow.show()
        self.Window.hide()

    def CheckForReg(self):
        global cursor
        cursor.execute('SELECT username FROM users WHERE username = "{}"'.format(self.UsernameInput.text()))
        Info1 = cursor.fetchall()
        cursor.execute('SELECT email FROM users WHERE email = "{}"'.format(self.EmailInput.text()))
        self.MsgBox.setStyleSheet("color:white;""font: 12pt \"Arial\";" 'background-color: rgba(0,0,0,0);')
        Info2 = cursor.fetchall()

        if len(Info1) > 0:
            self.MsgBox.setText('Username is already exist.')
            return False
        elif self.UsernameInput.text() == '':
            self.MsgBox.setText('invalid username.')
            return False
        elif len(Info2) > 0:
            self.MsgBox.setText('Email is already exist.')
            return False
        elif self.PasswordInput.text() == '':
            self.MsgBox.setText('invalid password.')
            return False
        elif self.EmailInput.text() == '':
            self.MsgBox.setText('Invalid Email.')
            return False
        elif self.QuestionAnswer.text() == '':
            self.MsgBox.setText('Invalid Question answer.')
            return False
        else:
            return True

    def Clicked_GoBack(self):
        self.Window.hide()
        self.LoginWindow.show()

    def Clicked_AddToDatabase(self):
        # TODO: Check for emptiness in mail
        if self.CheckForReg() is True:
            try:
                global cursor
                global connection
                cursor.execute('INSERT INTO users VALUES ("{}","{}","{}","{}");'.format(self.UsernameInput.text(),
                                                                                         self.EmailInput.text(),
                                                                                         self.PasswordInput.text(),
                                                                                         self.Hint.text()))
                connection.commit()

                cursor.execute('INSERT INTO questions VALUES ("{}","{}","{}")'.format(self.UsernameInput.text(),
                                                                                      self.combobox1.currentIndex(),
                                                                                      self.QuestionAnswer.text()))
                connection.commit()
                # self.MsgBox.setStyleSheet("color:green;""font: 14pt \"Arial\";")
                # self.MsgBox.setText("Successfully registered")
            except Exception as e:
                print(e)



class UI_WelcomingPage(object):
    def __init__(self):
        self.Window = None
        self.StartDet = False

    def setupUi(self, FirstPage):
        FirstPage.setObjectName("FirstPage")
        FirstPage.resize(425, 547)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FirstPage.sizePolicy().hasHeightForWidth())
        FirstPage.setSizePolicy(sizePolicy)
        FirstPage.setMinimumSize(QtCore.QSize(425, 547))
        FirstPage.setMaximumSize(QtCore.QSize(425, 547))
        FirstPage.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));")
        self.welcome = QtWidgets.QLabel(FirstPage)
        self.welcome.setGeometry(QtCore.QRect(100, 50, 221, 41))
        self.welcome.setStyleSheet("font: 75 35pt \"Arial\";\n" "background-color: rgba(0,0,0,0);\n" "color: white;")
        self.welcome.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.welcome.setScaledContents(False)
        self.welcome.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.welcome.setObjectName("welcome")
        self.textunderwelcome = QtWidgets.QLabel(FirstPage)
        self.textunderwelcome.setGeometry(QtCore.QRect(70, 100, 281, 31))
        self.textunderwelcome.setStyleSheet(
            "font: 75 15pt \"Arial\";\n" "background-color: rgba(0,0,0,0);\n" "color: white;")
        self.textunderwelcome.setObjectName("textunderwelcome")
        self.LoginButton = QtWidgets.QPushButton(FirstPage)
        self.LoginButton.setGeometry(QtCore.QRect(110, 244, 211, 51))
        font = QtGui.QFont()
        font.setFamily("13 Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LoginButton.setFont(font)
        self.LoginButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.LoginButton.setStyleSheet(
            ".QPushButton{\n" "font: 13pt bold \"Arial\";\n" "border: 2px solid black;\n" "padding: 14px 28px;\n" "background-color: rgba(0,0,0,0);\n" "color: white;\n" "}\n" "\n" ".pushButton {\n" "border-color: #2196F3;\n" "}\n" "\n" ".QPushButton::hover{\n" "color:whitek;\n" "border-color: white;\n" "}")
        self.LoginButton.setObjectName("LoginButton")
        self.createanewaccountButton = QtWidgets.QPushButton(FirstPage)
        self.createanewaccountButton.setGeometry(QtCore.QRect(110, 340, 211, 51))
        self.createanewaccountButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.createanewaccountButton.setStyleSheet(
            ".QPushButton{\n""font: 12pt bold \"Arial\";\n""border: 2px solid black;\n""padding: 14px 28px;\n""background-color: rgba(0,0,0,0);\n""color: white;\n""}\n""\n"".pushButton {\n""border-color: #2196F3;\n""color: dodgerblue;\n""}\n""\n"".QPushButton::hover{\n""color:black;\n""border-color: white;\n""}")
        self.createanewaccountButton.setObjectName("createanewaccountButton")
        self.ExitButton = QtWidgets.QPushButton(FirstPage)
        self.ExitButton.setGeometry(QtCore.QRect(110, 460, 211, 51))
        self.ExitButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExitButton.setStyleSheet(
            ".QPushButton{\n" "font: 12pt bold \"Arial\";\n" "border: 2px solid black;\n" "padding: 14px 28px;\n" "background-color: rgba(0,0,0,0);\n" "color: white;\n" "}\n" "\n" ".pushButton {\n" "border-color: #2196F3;\n" "color: dodgerblue;\n" "}\n" "\n" ".QPushButton::hover{\n" "color:black;\n" "border-color: white;\n" "}")
        self.ExitButton.setObjectName("ExitButton")
        self.textunderwelcome.raise_()
        self.welcome.raise_()
        self.LoginButton.raise_()
        self.createanewaccountButton.raise_()
        self.ExitButton.raise_()
        self.welcome.setBuddy(FirstPage)

        self.retranslateUi(FirstPage)
        QtCore.QMetaObject.connectSlotsByName(FirstPage)

        self.Window = FirstPage

        ## Admin Window
        self.A_Window = QtWidgets.QMainWindow()
        self.A_UI = UI_Admin()
        self.A_UI.setupUi(self.A_Window, FirstPage, self)

        ## User Window
        self.U_Window = QtWidgets.QMainWindow()
        self.U_UI = UI_User()
        self.U_UI.setupUi(self.U_Window, FirstPage, self)

        self.PassWindow = QtWidgets.QMainWindow()
        self.PassUI = UI_ForgotPassword()
        self.PassUI.setupUi(self.PassWindow)

        ## Register Window
        self.RegisterWindow = QtWidgets.QMainWindow()
        self.Register_UI = UI_RegisterPage()

        ## Login Window
        self.LoginWindow = QtWidgets.QMainWindow()
        self.Login_UI = UI_LoginPage()
        self.Login_UI.setupUi(self.LoginWindow, FirstPage, self.RegisterWindow, self.A_Window, self.U_Window,self.PassWindow)
        self.Login_UI.setupGUI(self.A_UI, self.U_UI)

        self.Register_UI.setupUi(self.RegisterWindow, FirstPage, self.LoginWindow)

        self.LoginButton.clicked.connect(self.Clicked_LoginWindow)
        self.createanewaccountButton.clicked.connect(self.Clicked_RegisterPage)
        self.ExitButton.clicked.connect(ExitProgram)

    def retranslateUi(self, FirstPage):
        _translate = QtCore.QCoreApplication.translate
        FirstPage.setWindowTitle(_translate("FirstPage", "Form"))
        self.welcome.setText(_translate("FirstPage", "Welcome"))
        self.textunderwelcome.setText(_translate("FirstPage", "Sign in or create a new account"))
        self.LoginButton.setText(_translate("FirstPage", "Login"))
        self.createanewaccountButton.setText(_translate("FirstPage", "Create a new account"))
        self.ExitButton.setText(_translate("FirstPage", "Exit"))

    def get_UI(self):
        global privilege
        if privilege.name == 'admin':
            return self.A_UI
        elif privilege.name == 'user':
            return self.U_UI
        else:
            return None

    def setDetect(self, NewValue):
        self.StartDet = NewValue

    def getDetect(self):
        return self.StartDet

    def Clicked_RegisterPage(self):
        try:
            self.RegisterWindow.show()
            self.Window.hide()
        except Exception as e:
            print(e)

    def Clicked_LoginWindow(self):
        try:
            self.LoginWindow.show()
            self.Window.hide()
        except Exception as e:
            print(e)
