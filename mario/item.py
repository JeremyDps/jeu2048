#! /usr/bin/python3
# -*- coding: utf-8 -*-
#



class Item():
    def __init__(self,typ,i,j):
        self.type=typ
        self.i=i
        self.j=j
    def getType(self):
        return self.type

    def getI(self):
        return self.i

    def getJ(self):
        return self.j