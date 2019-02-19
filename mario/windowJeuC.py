#! /usr/bin/python3
# -*- coding: utf-8 -*-
#

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from layout import Layout

class WindowJeuC(QMainWindow):
    def __init__(self,app,ordre):
        super().__init__()
        self.initUI(app,ordre)

    def closeEvent(self,event):
        QCoreApplication.instance().quit()

    def initUI(self,app,ordre):
        self.setWindowFlags(Qt.SplashScreen)
        self.setFocus()
        self.setWindow()
        self.setCenter()
        self.setLayout(app,ordre)
        self.update() 


    def setCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setLayout(self,app,ordre):
        self.layout = Layout(app,ordre)
        self.setCentralWidget(self.layout)

    def setWindow(self):
        width = QDesktopWidget().availableGeometry().width()/2
        height = QDesktopWidget().availableGeometry().height()/2
        self.setGeometry(10, 10, width, height)
        self.setWindowTitle("2048 Mario")

    def keyPressEvent(self, event):
        #while self.grid.perdu()==False:
        if event.key()==Qt.Key_Up and self.layout.getGrid().mvUp():
            self.layout.getGrid().up()
        elif event.key()==Qt.Key_Down and self.layout.getGrid().mvDown():
            self.layout.getGrid().down()
        elif event.key()==Qt.Key_Left and self.layout.getGrid().mvLeft():
            self.layout.getGrid().left()
        elif event.key()==Qt.Key_Right and self.layout.getGrid().mvRight():
            self.layout.getGrid().right()
        

        elif event.key()==Qt.Key_Backspace:
            self.layout.getGrid().retour()

        elif event.key()==Qt.Key_Space:
            self.layout.getGrid().retry()

            

        if not(self.layout.getGrid().mvUp()) and not(self.layout.getGrid().mvDown()) and not(self.layout.getGrid().mvLeft()) and not(self.layout.getGrid().mvRight()):
            son=QSound("sons/smb_mariodie.wav")
            son.play()
            perdu=QMessageBox(self)
            perdu.setText("Vous avez perdu!\n Voulez-vous reessayer?")
            perdu.setStandardButtons(QMessageBox.Close | QMessageBox.Ok)
            if perdu.exec_()==QMessageBox.Close:
                QCoreApplication.instance().quit()
            elif perdu.exec_()==QMessageBox.Ok:
                self.layout.getGrid().retry()
        elif (self.layout.getGrid().win()):
            son=QSound("sons/smb_stage_clear.wav")
            son.play()
            gagne=QMessageBox(self)
            gagne.setText("Vous avez gagné!\n Voulez-vous rejouer?")
            gagne.setStandardButtons(QMessageBox.Close | QMessageBox.Ok)
            if gagne.exec_()==QMessageBox.Close:
                QCoreApplication.instance().quit()
            elif gagne.exec_()==QMessageBox.Ok:
                self.layout.getGrid().retry()
        self.layout.afficheScore()