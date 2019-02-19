#! /usr/bin/python3
# -*- coding: utf-8 -*-
#

from math import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.initUI(argv)

    def initUI(self,argv):
        self.setFont(QFont("Arial",14))
        self.setStyle(QStyleFactory.create('fusion'))
        self.p = self.palette()
        self.p.setBrush(10,QBrush(argv[0]))
        self.p.setColor(QPalette.Button, QColor(53,53,53))
        self.p.setColor(QPalette.Highlight, QColor(142,45,197))
        self.p.setColor(QPalette.ButtonText, QColor(255,255,255))
        self.p.setColor(QPalette.WindowText, QColor(255,255,255))
        self.setPalette(self.p)

    def initFont(self,argv):
        self.p.setBrush(10,QBrush(QImage(argv)))
        self.setPalette(self.p)

    