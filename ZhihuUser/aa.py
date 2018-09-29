#!/usr/anaconda3/python3
# -*- coding: utf-8 -*-
# @author:    Qingyunke
# @Time :     2018/9/28 15:15


students = [('zhang', 'A'), ('li', 'D'), ('wang', 'C')]
b = sorted(students, key=lambda x: x[1])
print(b)


class Student:
    def __init__(self, name, grade , age):
        self.name = name
        self.grade = grade
        self.age = age
        
    def __repr__(self):
        return repr((self.name, self.name, self.age))
    

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
        
    def __str__(self):
        return f'a {self.color} car'


my_car = Car('red', 235)
print(my_car)
