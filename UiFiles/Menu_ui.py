# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\datas_and_files\AAA_Dev\python\pyqt\Projects\Welcome_to_Site3408\UiFiles\Menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu_for_members(object):
    def setupUi(self, Menu_for_members):
        Menu_for_members.setObjectName("Menu_for_members")
        Menu_for_members.resize(528, 190)
        self.centralwidget = QtWidgets.QWidget(Menu_for_members)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.tasks = QtWidgets.QComboBox(self.centralwidget)
        self.tasks.setObjectName("tasks")
        self.tasks.addItem("")
        self.tasks.addItem("")
        self.tasks.addItem("")
        self.tasks.addItem("")
        self.tasks.addItem("")
        self.tasks.addItem("")
        self.tasks.addItem("")
        self.tasks.addItem("")
        self.tasks.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tasks)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_4)
        self.horizontalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.Goback = QtWidgets.QPushButton(self.centralwidget)
        self.Goback.setObjectName("Goback")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Goback)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        Menu_for_members.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Menu_for_members)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 22))
        self.menubar.setObjectName("menubar")
        self.menuSave_your_progress = QtWidgets.QMenu(self.menubar)
        self.menuSave_your_progress.setObjectName("menuSave_your_progress")
        Menu_for_members.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuSave_your_progress.menuAction())

        self.retranslateUi(Menu_for_members)
        QtCore.QMetaObject.connectSlotsByName(Menu_for_members)

    def retranslateUi(self, Menu_for_members):
        _translate = QtCore.QCoreApplication.translate
        Menu_for_members.setWindowTitle(_translate("Menu_for_members", "Menu"))
        self.label.setText(_translate("Menu_for_members", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Here you can check out the daily tasks and various services that</span></p><p><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">site-3408 offers you. Or... You can also simply rediscover yourself.</span></p></body></html>"))
        self.label_2.setText(_translate("Menu_for_members", "Tasks"))
        self.tasks.setItemText(0, _translate("Menu_for_members", "Select your task:"))
        self.tasks.setItemText(1, _translate("Menu_for_members", "I. Feed Scp-????"))
        self.tasks.setItemText(2, _translate("Menu_for_members", "II. Eat your lunch well"))
        self.tasks.setItemText(3, _translate("Menu_for_members", "III. Update your work log"))
        self.tasks.setItemText(4, _translate("Menu_for_members", "IV. Start your relaxation regimen!"))
        self.tasks.setItemText(5, _translate("Menu_for_members", "V. After that, take a nap."))
        self.tasks.setItemText(6, _translate("Menu_for_members", "VI. Enjoy the party of the night!"))
        self.tasks.setItemText(7, _translate("Menu_for_members", "VII. Drink a glass of ??!?, and fall asleep..."))
        self.tasks.setItemText(8, _translate("Menu_for_members", "VIII. #TODO"))
        self.label_3.setText(_translate("Menu_for_members", "Services"))
        self.label_4.setText(_translate("Menu_for_members", "about"))
        self.label_5.setText(_translate("Menu_for_members", "Diningroom"))
        self.comboBox_2.setItemText(0, _translate("Menu_for_members", "Monday"))
        self.comboBox_2.setItemText(1, _translate("Menu_for_members", "Tuesday"))
        self.comboBox_2.setItemText(2, _translate("Menu_for_members", "Wednesday"))
        self.comboBox_2.setItemText(3, _translate("Menu_for_members", "Thursday"))
        self.comboBox_2.setItemText(4, _translate("Menu_for_members", "Friday"))
        self.comboBox_2.setItemText(5, _translate("Menu_for_members", "Saturday"))
        self.comboBox_2.setItemText(6, _translate("Menu_for_members", "Sunday"))
        self.comboBox_2.setItemText(7, _translate("Menu_for_members", "?NULL?[Edited]day"))
        self.label_7.setText(_translate("Menu_for_members", "MyFile"))
        self.pushButton.setText(_translate("Menu_for_members", "View"))
        self.label_6.setText(_translate("Menu_for_members", "Goback"))
        self.Goback.setText(_translate("Menu_for_members", "Goback"))
        self.menuSave_your_progress.setTitle(_translate("Menu_for_members", "Save your progress"))
