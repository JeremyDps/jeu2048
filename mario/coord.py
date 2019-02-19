#! /usr/bin/python3
# -*- coding: utf-8 -*-
#

from random import randint


class Coord():
    def __init__(self):
        self.p=(randint(0,3),randint(0,3))
    def getX(self):
        return(self.p[0])
    def getY(self):
        return(self.p[1])
