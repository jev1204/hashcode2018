#!/usr/bin/python

import numpy as np
import sys
import rideObj

firstLine = []


def readMatrix(fileName):
    input = np.loadtxt(fileName)
    firstLine = input[0]
    print(firstLine)
    R = firstLine[0]
    C = firstLine[1]
    F = firstLine[2]
    rides = firstLine[3]
    bonus = firstLine[4]
    steps = firstLine[5]

    rideObjects = []

    for line in input:
        rideObject = rideObj.RideObj([line[0],line[1]], [line[2], line[3]], line[4], line[5])
        rideObjects.append(rideObject)
        print(rideObject.calcSteps())

readMatrix("dataSet/a_example.in")



