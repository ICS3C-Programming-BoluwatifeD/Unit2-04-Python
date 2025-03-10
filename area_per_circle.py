#!/usr/bin/env python3
# Created By: Boluwatife Dada
# Date: feb 26, 2025
# This program calculates the area and perimeter of a circle
import math


def main():
    # get the radius from the user
    radius = float(input("enter the radius of a circle(mm): "))
    circumference = float(input("enter the circumference of a circle(mm): "))
    # calculate the circumference
    circumference = TAU * radius

    # display the circumference
    # display the area
    print("")
    print("circumference = {}mm".format(circumference))

    main()


rad = 11
circ = math.pi * 2 * rad
area = math.pi * rad**2
print(circ, area)

math.sqrt(100)
10.0
math.sqrt(25)
5.0
