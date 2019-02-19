#! /usr/bin/python3
# -*- coding: utf-8 -*-
#

from item import Item
from coord import Coord
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Grid(QWidget):
    def __init__(self):
        super(Grid,self).__init__()
        self.initUI()

    def initUI(self):
        self.brush=QBrush(Qt.transparent)
        self.pen=QPen(QColor.fromRgb(187,173,163))
        self.pen.setWidth(7)
        self.initRec()
        self.initRetour()
        

        #score
        self.score=0

    def win(self):
        for i in range(4):
            for j in range(4):
                if self.p[i][j].getType()==11:
                    return True
        return False

    def initRetour(self):
        self.ancienP=[]
        for i in self.p:
            l=[]
            for j in i:
                l.append(j)
            self.ancienP.append(l)

    def retour(self):
        self.p=[]
        for i in self.ancienP:
            l=[]
            for j in i:
                l.append(j)
            self.p.append(l)
        self.setFocus()
        self.update()

    def getScore(self):
        return self.score


    def retry(self):
        self.initUI()
        self.setFocus()
        self.update()


    def initRec(self):
        p1=Coord()
        p2=Coord()
        while(p1.getX()==p2.getX() and p1.getY()==p2.getY()):
            p1=Coord()
            p2=Coord()

        self.p=[]

        for i in range(4):
            l=[]
            for j in range(4):
                if (i==p1.getX() and j==p1.getY()) or(i==p2.getX() and j==p2.getY()):
                    l.append(Item(1,i,j))
                else:
                    l.append(Item(0,i,j))
            self.p.append(l)

    def newCase(self):
        p=Coord()
        while self.p[p.getX()][p.getY()].getType()!=0:
            p=Coord()
        self.p[p.getX()][p.getY()]=Item(1,p.getX(),p.getY())


    def type(self,argument):
        if argument==0:
            self.image=QImage("img/vide.jpg")
        elif argument==1:
            self.image=QImage("img/piece.jpg")
        elif argument==2:
            self.image=QImage("img/pieceEtoile.jpg")
        elif argument==3:
            self.image=QImage("img/champiB.jpg")
        elif argument==4:
            self.image=QImage("img/champiR.png")
        elif argument==5:
            self.image=QImage("img/vie.jpg")
        elif argument==6:
            self.image=QImage("img/grosChampi.jpg")
        elif argument==7:
            self.image=QImage("img/fleureB.jpg")
        elif argument==8:
            self.image=QImage("img/fleurR.jpg")
        elif argument==9:
            self.image=QImage("img/feuille.jpg")
        elif argument==10:
            self.image=QImage("img/pingouin.jpg")
        elif argument==11:
            self.image=QImage("img/etoile.jpg")



    def paintEvent(self,event):
        taille=self.height()/5
        painter = QPainter(self)

        painter.setPen(self.pen)
        width=self.width()/2-taille*2
        height=self.height()/2-taille*2
        painter.setBrush(self.brush)

        for i in range(4):
            for j in range(4):
                
                self.type(self.p[i][j].getType())
                painter.drawImage(QRect(width,height,taille,taille),self.image)
                painter.drawRect(QRect(width,height,taille,taille))
                width+=taille
            width=self.width()/2-taille*2
            height+=taille

        


    def decalUp(self):
        i=3
        while i>0:
            for j in range(4):
                caseSuppr=self.p[i-1][j]
                case=self.p[i][j]
                if caseSuppr.getType()==0 and case.getType()!=0:
                    self.p[i-1][j]=Item(case.getType(),i,j)
                    self.p[i][j]=Item(0,i,j)
            i-=1
    


    def fusionUp(self,i,j):
        self.p[i-1][j]=Item(self.p[i-1][j].getType()+1,i,j)
        self.p[i][j]=Item(0,i,j)
        self.score+=2**self.p[i-1][j].getType()
        self.decalUp()
        self.decalUp()


    def decalDown(self):
        for i in range(3):
            for j in range(4):

                caseSuppr=self.p[i+1][j]
                case=self.p[i][j]

                if caseSuppr.getType()==0 and case.getType()!=0:
                    self.p[i+1][j]=Item(case.getType(),i,j)
                    self.p[i][j]=Item(0,i,j)

    

    def fusionDown(self,i,j):
        caseSuppr=self.p[i+1][j]
        case=self.p[i][j]
        self.p[i+1][j]=Item(caseSuppr.getType()+1,i,j)
        self.p[i][j]=Item(0,i,j)
        self.score+=2**self.p[i+1][j].getType()
        self.decalDown()
        self.decalDown()


    def decalRight(self):
        for i in range(4):
            for j in range(3):

                caseSuppr=self.p[i][j+1]
                case=self.p[i][j]

                if caseSuppr.getType()==0 and case.getType()!=0:
                    self.p[i][j+1]=Item(case.getType(),i,j)
                    self.p[i][j]=Item(0,i,j)
       

    def decalLeft(self):
        for i in range(4):
            j=3
            while j>0:

                caseSuppr=self.p[i][j-1]
                case=self.p[i][j]

                if caseSuppr.getType()==0 and case.getType()!=0:
                    self.p[i][j-1]=Item(case.getType(),i,j)
                    self.p[i][j]=Item(0,i,j)
                j-=1

    def fusionRight(self,i,j):
        caseSuppr=self.p[i][j+1]
        case=self.p[i][j]
        self.p[i][j+1]=Item(case.getType()+1,i,j)
        self.p[i][j]=Item(0,i,j)
        self.score+=2**self.p[i][j+1].getType()
        self.decalRight()
        self.decalRight()

    def fusionLeft(self,i,j):
        caseSuppr=self.p[i][j-1]
        case=self.p[i][j]

        self.p[i][j-1]=Item(caseSuppr.getType()+1,i,j)
        self.p[i][j]=Item(0,i,j)

        self.score+=2**self.p[i][j-1].getType()
        self.decalLeft()
        self.decalLeft()
            



    def up(self):
        self.initRetour()
        for i in range(1,4):
            for j in range(4):
                if self.p[i-1][j].getType()==0 and self.p[i][j].getType()!=0:
                    self.decalUp()
        

        for i in range(1,4):
            for j in range(4):
                if self.p[i-1][j].getType()==self.p[i][j].getType() and self.p[i][j].getType()!=0 :
                    self.fusionUp(i,j)
                    



        self.newCase()
        self.update()


    def down(self):
        self.initRetour()
        i=2
        while i>=0:
            for j in range(4):

                caseSuppr=self.p[i+1][j]
                case=self.p[i][j]

                if caseSuppr.getType()==0 and case.getType()!=0:
                    self.decalDown()
                
            i-=1

        i=2
        while i>=0:
            for j in range(4):

                caseSuppr=self.p[i+1][j]
                case=self.p[i][j]
                if caseSuppr.getType()==case.getType() and caseSuppr.getType()!=0 :
                    self.fusionDown(i,j)
            i-=1
        

        self.newCase()

        self.update()


    def right(self):
        self.initRetour()
        for i in range(4):
            j=2
            while j>=0:

                caseSuppr=self.p[i][j+1]
                case=self.p[i][j]

                if caseSuppr.getType()==0 and case.getType()!=0:
                    self.decalRight()
                j-=1

        for i in range(4):
            j=2
            while j>=0:

                caseSuppr=self.p[i][j+1]
                case=self.p[i][j]
                if caseSuppr.getType()==case.getType() and caseSuppr.getType()!=0 :
                    self.fusionRight(i,j)
                    
                j-=1

        self.newCase()

        self.update()


    def left(self):
        self.initRetour()
        for i in range(4):
            for j in range(1,4):

                caseSuppr=self.p[i][j-1]
                case=self.p[i][j]

                if caseSuppr.getType()==0 and case.getType()!=0:
                    self.decalLeft()

        for i in range(4):
            for j in range(1,4):

                caseSuppr=self.p[i][j-1]
                case=self.p[i][j]
                if caseSuppr.getType()==case.getType() and caseSuppr.getType()!=0 :
                    self.fusionLeft(i,j)

        self.newCase()

        self.update()

    def mvUp(self):
        for i in range (1,4):
            for j in range(4):
                if (self.p[i-1][j].getType()==0 and self.p[i][j].getType()!=0) or (self.p[i][j].getType()==self.p[i-1][j].getType() and self.p[i][j].getType()!=0):
                    return True
        return False

    def mvDown(self):
        for i in range(3):
            for j in range(4):
                if (self.p[i+1][j].getType()==0 and self.p[i][j].getType()!=0) or (self.p[i][j].getType()==self.p[i+1][j].getType() and self.p[i][j].getType()!=0):
                    return True 

    def mvLeft(self):
        for i in range (4):
            for j in range(1,4):
                if (self.p[i][j-1].getType()==0 and self.p[i][j].getType()!=0) or (self.p[i][j].getType()==self.p[i][j-1].getType() and self.p[i][j].getType()!=0):
                    return True
        return False

    def mvRight(self):
        for i in range(4):
            for j in range(3):
                if (self.p[i][j+1].getType()==0 and self.p[i][j].getType()!=0) or (self.p[i][j].getType()==self.p[i][j+1].getType() and self.p[i][j].getType()!=0):
                    return True 

