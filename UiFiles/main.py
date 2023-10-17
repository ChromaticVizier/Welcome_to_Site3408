import sys
import time
import json
import typing
import requests
from Welcome_ui import Ui_Welcome
from Become_a_member_ui import Ui_Becomeamember
from congratulations_ui import Ui_congratulations
from Welcome_back_ui import Ui_welcomeback
from login_ui import Ui_login
from Stufflogin_ui import Ui_stufflogin
from requiredenied_ui import Ui_passwordincorrect
from Menu_ui import Ui_Menu_for_members

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QCoreApplication, pyqtSignal
from PyQt5 import QtCore, uic
from PyQt5.Qt import QApplication, QWidget, QThread
from PyQt5.uic import loadUi

class MyWindow(Ui_Welcome, QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.Imnew.clicked.connect(self.gobecomeamember)
        self.Imamember.clicked.connect(self.gologinwindow)
        self.Imastuff.clicked.connect(self.gostuffloginwindow)

    def gobecomeamember(self):
        self.ui_becomeamember = registerwindow()
        self.ui_becomeamember.show()
        self.close()

    def gologinwindow(self):
        self.ui_login = loginwindow()
        self.ui_login.show()
        self.close()

    def gostuffloginwindow(self):
        self.ui_stufflogin = stuffloginwindow()
        self.ui_stufflogin.show()
        self.close()
#This class is already done.

class stuffloginwindow(Ui_stufflogin, QMainWindow):
    def __init__(self):
        super(stuffloginwindow, self).__init__()
        self.setupUi(self)
        self.Goback.clicked.connect(self.gowelcome)
        self.Login.clicked.connect(self.stufflogin_next)

    def gowelcome(self):
        self.ui_welcome = MyWindow()
        self.ui_welcome.show()
        self.close()

    def stufflogin_next():
        #TODO
        pass

class loginwindow(Ui_login, QMainWindow):
    def __init__(self):
        super(loginwindow, self).__init__()
        self.setupUi(self)
        self.Goback.clicked.connect(self.gowelcome)
        self.Login.clicked.connect(self.login_next)

    def gowelcome(self):
        self.ui_welcome = MyWindow()
        self.ui_welcome.show()
        self.close()

    def login_next():
        #TODO
        pass

class congratulationswindow(Ui_congratulations, QMainWindow):
    def __init__(self):
        super(congratulationswindow, self).__init__()
        self.setupUi(self)
        self.iknow.clicked.connect(self.gowelcomeback)

    def gowelcomeback(self):
        self.ui_welcomeback = welcomebackwindow()
        self.ui_welcomeback.show()
        self.close()

class registerwindow(Ui_Becomeamember, QMainWindow):
    def __init__(self):
        super(registerwindow, self).__init__()
        self.setupUi(self)
        self.Goback.clicked.connect(self.gowelcome)
        self.Register.clicked.connect(self.register_next)

    def gowelcome(self):
        self.ui_welcome = MyWindow()
        self.ui_welcome.show()
        self.close()

    def register_next(self):
        #TODO
        self.gotocongratulations()

    def gotocongratulations(self):
        self.ui_congratulations = congratulationswindow()
        self.ui_congratulations.show()
        self.close()

class welcomebackwindow(Ui_welcomeback, QMainWindow):
    def __init__(self):
        super(welcomebackwindow, self).__init__()
        self.setupUi(self)
        self.next.clicked.connect(self.tomenu)

    def tomenu(self):
        self.ui_menu = menuformemberswindow()
        self.ui_menu.show()
        self.close()

class menuformemberswindow(Ui_Menu_for_members, QMainWindow):
    def __init__(self):
        super(menuformemberswindow, self).__init__()
        self.setupUi(self)
        self.Goback.clicked.connect(self.gowelcome)

    def gowelcome(self):
        self.ui_welcome = MyWindow()
        self.ui_welcome.show()
        self.close() 

#This class might be used later.Don't delete.
class denywindow(Ui_passwordincorrect, QMainWindow):
    def __init__(self):
        super(denywindow, self).__init__()
        self.setupUi(self)
        self.Goback.clicked.connect(self.gowelcome)

    def gowelcome(self):
        self.ui_welcome = MyWindow()
        self.ui_welcome.show()
        self.close()

if __name__ == '__main__':
    QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())