#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  14 

@author: Adrianacmy

In games, we often put a rectangular “bounding box” around our sprites in the 
game. We can then do collision detection between, say, bombs and spaceships, 
by comparing whether their rectangles overlap anywhere.
"""


class Point(object):
    def __init__(self, initx, inity):
        self.x = initx
        self.y = inity

    def __str__(self):
        print('x = ' + self.x + ' y = ' + self.y)


class Rectangle(object):

    def __init__(self, initP, width, height):
        '''
        initP is the left_bottom point
        '''
        self.location = initP
        self.width = width
        self.height = height

    def __str__(self):
        print(
            'location: ' + self.location + 'width: ' + self.width + 'height: ' 
            + self.height
             )

    def range_this(self):
        width_range = self.width + self.location.x
        height_range = self.height + self.location.y
        return width_range, height_range

    def is_overlap(self, other, width_range, width_range_other):
        for i in range(self.location.x, width_range):
            if i in range(other.location.x, width_range_other):
                return True
        return False

    def is_collided(self, other):
        width_range, height_range = self.range_this()
        width_range_other, height_range_other = other.range_this()

        width_overlap = self.is_overlap(other, width_range, width_range_other)
        height_overlap = self.is_overlap(other, height_range, height_range)

        return width_overlap or height_overlap
        
        



