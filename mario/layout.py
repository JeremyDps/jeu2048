#! /usr/bin/python3
# -*- coding: utf-8 -*-
#


from grid import Grid
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Layout(QWidget):
    def __init__(self,app,ordre):
        super(Layout,self).__init__()
        self.initUI(app,ordre)

    def initUI(self,app,ordre):
        self.fenOrdre=ordre
        self.app=app
        self.setFocus()
        self.layout=QGridLayout()

        self.layout.setColumnMinimumWidth(1,4*(self.width()/5))
        self.layout.setColumnMinimumWidth(0,(self.width()-4*(self.height()/4))/2)
        self.layout.setColumnMinimumWidth(2,(self.width()-4*(self.height()/4))/2)

        self.layout.setRowMinimumHeight(1,4*(self.height()/5))
        self.layout.setRowMinimumHeight(0,(self.height()-4*(self.height()/4))/2)
        self.layout.setRowMinimumHeight(2,(self.height()-4*(self.height()/4))/2)

        self.browser = QTextBrowser()
        self.layout.addWidget(self.browser,0,0)


        self.grid=Grid()
        self.layout.addWidget(self.grid,1,1)


        #Bouton reessayer
        font=QFont("Arial",14,QFont.Bold)
        self.retry=QPushButton("Reessayer",self)
        self.retry.setFont(font)
        self.retry.clicked.connect(self.grid.retry)


        #bouton retour
        self.retour=QPushButton("Retour",self)
        self.retour.setFont(font)
        self.retour.clicked.connect(self.grid.retour)

        #Bouton Quitter
        self.quitter=QPushButton("Quitter",self)
        self.quitter.setFont(font)
        self.quitter.clicked.connect(QCoreApplication.instance().quit)

        #bouton ordre bonus
        self.ordre=QPushButton("Ordre Bonus",self)
        self.ordre.setFont(font)
        self.ordre.clicked.connect(self.fOrdre)

        self.layout.addWidget(self.ordre,1,0)


        self.layout.addWidget(self.retour,2,2)


        self.layout.addWidget(self.retry,0,2)


        self.layout.addWidget(self.quitter,2,0)

        self.browser.append("Score : %d"%(self.grid.getScore()))


        self.setLayout(self.layout)
        



    def fOrdre(self):
        self.fenOrdre.show()
        self.setFocus()

    def afficheScore(self):
        self.browser=QTextBrowser()
        self.layout.addWidget(self.browser,0,0)
        self.browser.append("Score : %d"%(self.grid.getScore()))
        self.update()

    def getGrid(self):
        return self.grid