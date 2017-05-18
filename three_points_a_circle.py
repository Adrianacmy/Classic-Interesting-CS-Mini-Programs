#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  16 

@author: Adrianacmy


Given three points that fall on the circumference of a circle, find the center
and radius of the circle

I started with the solution try to handle all slop doesn't exist exception, end
up horrible and lost in the control flow, lunkily a great fellow remanded me 
to ignore the slop unexist one,since there is always only one side may don't have slop
in a triangle. Yeah, it is a great clue and thanks dude :) 
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

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def perpendicular_slop(self, p):
        '''caculate two points' perpendicular_slop when exist'''
        
        per_slop = (self.x - p.x)/(self.y - p.y)
        return per_slop

    def get_two_groups_points(self, p0, p1):
        '''find the two right points and skip the ones whose perpendicular_slop
        dosen't exist'''

        if self.y == p0.y:
            p = [(self, p1), (p0, p1)]
        elif self.y == p1.y:
            p = [(self, p0), (p0, p1)]
        else:
            p = [(self, p0), (self, p1)]
        return p

    def form_circle(self, p0, p1):
        '''compute center point by caculating the two perpendicular's 
        cross points, use distanceFromPoint() to caculate the radius.
        
        self, p0, p1 are three points
        per_slop: perpendicular line slop 
        per_inter: perpendicular line intersection
        return  r and center point

        '''

        if self.x == p0.x == p1.x or self.y == p0.y == p1.y:
            return 'Wrong inputs, three points can\'t be on the same line'
        else:
            points_group = self.get_two_groups_points(p0, p1)
            per_slop1 = points_group[0][0].perpendicular_slop(points_group[0][1])
            per_slop2 = points_group[1][0].perpendicular_slop(points_group[1][1])
            pm1 = points_group[0][0].halfway(points_group[0][1])
            pm2 = points_group[1][0].halfway(points_group[1][1])
            per_inter1 = pm1.y - per_slop1 * pm1.x
            per_inter2 = pm2.y - per_slop2 * pm2.x 

            ox = (per_inter2 - per_inter1) / (per_slop1 - per_slop2)
            oy = per_slop1 * ox + per_inter1

            r = points_group[0][0].distanceFromPoint(Point(ox, oy))

            return (round(r, 2), (round(ox, 2), round(oy, 2)))


def main():        
    p1 = Point(-1, 5)
    p2 = Point(3, 5)
    p3 = Point(3, -1)
    tp = p3.form_circle(p2, p1)
    print('center point:', tp[1], ' r:', tp[0])


if __name__ == '__main__':
    main()