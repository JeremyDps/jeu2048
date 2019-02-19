#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#


import sys
from application import Application
from windowJeuC import WindowJeuC
from windowJeuV import WindowJeuV
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class WindowMenu(QMainWindow):
	def __init__(self,app,jeuC,jeuV):
		super().__init__()
		self.initUI(app,jeuC,jeuV)

	def initUI(self,app,jeuC,jeuV):
		self.setWindowFlags(Qt.SplashScreen)
		self.app=app
		self.jeuC=jeuC
		self.jeuV=jeuV
		self.setGeometry(10, 10, 575, 470)
		self.setWindowTitle('2048 Mario')

		font=QFont("Arial",14,QFont.Bold)
        # bouton 1
		self.buttonV=QPushButton("Jeu 2048 variante",self)
		self.buttonV.setFont(font)
		self.buttonV.setGeometry(0,0,175,25)
		self.buttonV.move(15,60)
		self.buttonV.clicked.connect(self.buttonJeuV)
		# bouton 2
		self.buttonC=QPushButton("Jeu 2048 classique",self)
		self.buttonC.setFont(font)
		self.buttonC.setGeometry(0,0,190,25)
		self.buttonC.move(15,15)
		self.buttonC.clicked.connect(self.buttonJeuC)

		#Bouton Quitter
		self.quitter=QPushButton("Quitter",self)
		self.quitter.setFont(font)
		self.quitter.move(15,105)
		self.quitter.clicked.connect(QCoreApplication.instance().quit)

		self.setCenter()
		self.show()

	def setCenter(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def buttonJeuC(self):
		# slot du bouton
		self.app.initFont("img/fond.png")
		self.update()
		self.jeuC.show()
		self.hide()

	def buttonJeuV(self):
		# slot du bouton
		self.app.initFont("img/fond.png")
		self.update()
		self.jeuV.show()
		self.hide()



		

