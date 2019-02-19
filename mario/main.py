#! /usr/bin/python3
# -*- coding: utf-8 -*-
#

import sys
from windowOrdre import WindowOrdre
from application import Application
from menu import WindowMenu
from windowJeuC import WindowJeuC
from windowJeuV import WindowJeuV
from PyQt5.QtGui import *


class Main():
	def __init__(self):

		app = Application([QImage("img/accueil.jpg")])
		ordre=WindowOrdre()
		ordre.hide()
		jeuV=WindowJeuV(app,ordre)
		jeuV.hide()
		jeuC=WindowJeuC(app,ordre)
		jeuC.hide()
		win = WindowMenu(app,jeuC,jeuV)
		app.exec_()

Main()