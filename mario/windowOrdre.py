#! /usr/bin/python3
# -*- coding: utf-8 -*-
#

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *

class WindowOrdre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def closeEvent(self,event):
        QCoreApplication.instance().quit()

    def initUI(self):
    	self.setWindowFlags(Qt.SplashScreen)
    	self.setGeometry(0,0,250,188)
    	self.move(15,15)
    	p=self.palette()
    	p.setBrush(10,QBrush(QImage("img/ordre.jpg")))
    	self.setPalette(p)

    	font=QFont("Arial",5,Qt.transparent)
    	quitter=QPushButton("Quitter",self)
    	quitter.setFont(font)
    	quitter.setGeometry(0,0,30,15)
    	quitter.clicked.connect(self.hide)
    	quitter.move(15,45)
