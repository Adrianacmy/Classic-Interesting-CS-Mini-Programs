#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  10 

@author: Adrianacmy

Given three points that fall on the circumference of a circle, find the center\ 
and radius of the circle.0

"""


class Point:
    def __init__(self, initx, inity):
        self.x = initx
        self.y = inity

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def distanceFromPoint(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

    def reflect_x(self):
        self.y = -self.gety()
        return self

    def compute_equation(self, p):
        try:
            slop = (self.y - p.gety()) / (self.x - p.getx())
        except ZeroDivisionError:
            reurn None, 0
        else:
            b = p.gety() - slop * p.getx()
            return slop, b

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)
        print
    
    def get_perpendicular(self, P):
        lst = compute_equation(self, p)
        p0 = self.halfway(p)
        if lst[0] == None:
            perpendicular_slop = 0
            perpendicular_intersection = p0.y
            oy = p0.y
            return [0,perpendicular_slop, oy]
        elif lst[0] == 0:
            perpendicular_interseciton = 0
            ox = p0.x
            return [1, perpendicular_interseciton, ox]
        else:
            perpendicular_slop = 1 / slop 
            perpendicular_interseciton = p0.y - perpenducular_slop * p0.x
            return [3, perpendicular_slop, perpendicular_interseciton]


    def form_circle(self, p0, p1):
        '''
        :param p0: a point 
        :param p1: another point
        :return: another point
        
        In order to get the center point and r , need to cacculate:
        1.halfway point of any two lines
        2.the slops of above two lines
            - the slop of two perpendicular lines is reciprocal to each other
             - compute_equation() will return slop of a line
        3. find the cross point of above two
        '''
        if self.x == p0.x == p1.x or self.y == p0.y == p1.y:
            return 'Three points can\'t be on the same line'
        else:
            p2 = self.halfway(p0)
            try:
                slop2, b2 = self.compute_equation(p0)
            except ZeroDivisionError:
                per_slop2 = 0
                per_b2 = p2.y
                oy = p2.y
            else:        
                try:
                    per_slop2 = 1 / slop2
                except ZeroDivisionError:
                    ox = p2.x
                else:
                    per_b2 = p2.y - per_slop2 * p2.x

            p3 = self.halfway(p1)
            try:
                slop3, b3 = self.compute_equation(p1)
            except ZeroDivisionError:
                per_slop3 = 0
                per_b3 = p3.y
                oy = p3.y
            else:        
                try:
                    per_slop3 = 1 / slop3
                except ZeroDivisionError:
                    ox = p3.x
                else:
                    per_b3 = p3.y - per_slop3 * p3.x

            
        
        return (r, (ox, oy))


p1 = Point(-1, 5)
p2 = Point(3, 5)
p3 = Point(3, -1)

print(p1.form_circle(p2, p3))


