# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\datas_and_files\AAA_Dev\python\pyqt\Projects\Wiredo\UiFiles\Become_a_member.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Becomeamember(object):
    def setupUi(self, Becomeamember):
        Becomeamember.setObjectName("Becomeamember")
        Becomeamember.resize(281, 233)
        Becomeamember.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(Becomeamember)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 3)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 5, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 6, 1, 1, 2)
        self.Goback = QtWidgets.QPushButton(self.centralwidget)
        self.Goback.setObjectName("Goback")
        self.gridLayout.addWidget(self.Goback, 7, 0, 1, 2)
        self.Register = QtWidgets.QPushButton(self.centralwidget)
        self.Register.setObjectName("Register")
        self.gridLayout.addWidget(self.Register, 7, 2, 1, 1)
        Becomeamember.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Becomeamember)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 281, 22))
        self.menubar.setObjectName("menubar")
        self.menuSave_your_progress = QtWidgets.QMenu(self.menubar)
        self.menuSave_your_progress.setObjectName("menuSave_your_progress")
        Becomeamember.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuSave_your_progress.menuAction())

        self.retranslateUi(Becomeamember)
        QtCore.QMetaObject.connectSlotsByName(Becomeamember)

    def retranslateUi(self, Becomeamember):
        _translate = QtCore.QCoreApplication.translate
        Becomeamember.setWindowTitle(_translate("Becomeamember", "Become a member of Site-3408!"))
        self.label_3.setText(_translate("Becomeamember", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">Attention! </span></p></body></html>"))
        self.label_4.setText(_translate("Becomeamember", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Please keep your account in mind.</span></p></body></html>"))
        self.label_5.setText(_translate("Becomeamember", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">If you also forget yourself,</span></p></body></html>"))
        self.label_6.setText(_translate("Becomeamember", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">then no one in the world will</span></p></body></html>"))
        self.label_7.setText(_translate("Becomeamember", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">ever remember you again.</span></p></body></html>"))
        self.label.setText(_translate("Becomeamember", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Account</span></p></body></html>"))
        self.lineEdit.setText(_translate("Becomeamember", "Use your Email"))
        self.label_2.setText(_translate("Becomeamember", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Password</span></p></body></html>"))
        self.lineEdit_2.setText(_translate("Becomeamember", "Your password"))
        self.Goback.setText(_translate("Becomeamember", "Go back"))
        self.Register.setText(_translate("Becomeamember", "Register"))
        self.menuSave_your_progress.setTitle(_translate("Becomeamember", "Save your progress"))
