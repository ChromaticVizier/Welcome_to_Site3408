# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\datas_and_files\AAA_Dev\python\pyqt\Projects\Welcome_to_Site3408\UiFiles\Stufflogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_stufflogin(object):
    def setupUi(self, stufflogin):
        stufflogin.setObjectName("stufflogin")
        stufflogin.resize(489, 219)
        self.centralwidget = QtWidgets.QWidget(stufflogin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 1, 1, 2)
        self.Goback = QtWidgets.QPushButton(self.centralwidget)
        self.Goback.setObjectName("Goback")
        self.gridLayout.addWidget(self.Goback, 5, 0, 1, 2)
        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setObjectName("Login")
        self.gridLayout.addWidget(self.Login, 5, 2, 1, 1)
        stufflogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(stufflogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 25))
        self.menubar.setObjectName("menubar")
        self.menuSave_your_progress = QtWidgets.QMenu(self.menubar)
        self.menuSave_your_progress.setObjectName("menuSave_your_progress")
        stufflogin.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuSave_your_progress.menuAction())

        self.retranslateUi(stufflogin)
        QtCore.QMetaObject.connectSlotsByName(stufflogin)

    def retranslateUi(self, stufflogin):
        _translate = QtCore.QCoreApplication.translate
        stufflogin.setWindowTitle(_translate("stufflogin", "Site-3408 welcome you."))
        self.label.setText(_translate("stufflogin", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Hello, our loyal staff.</span></p></body></html>"))
        self.label_2.setText(_translate("stufflogin", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">No matter what position you\'re in,</span></p></body></html>"))
        self.label_3.setText(_translate("stufflogin", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">site3408 will always wish you success in your work.</span></p></body></html>"))
        self.label_4.setText(_translate("stufflogin", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Account</span></p></body></html>"))
        self.lineEdit.setText(_translate("stufflogin", "Your Email"))
        self.label_5.setText(_translate("stufflogin", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Password</span></p></body></html>"))
        self.lineEdit_2.setText(_translate("stufflogin", "Your password"))
        self.Goback.setText(_translate("stufflogin", "Go back"))
        self.Login.setText(_translate("stufflogin", "Login"))
        self.menuSave_your_progress.setTitle(_translate("stufflogin", "Save your progress"))
