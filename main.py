#!/usr/bin/python

import numpy as np
import sys
import rideObj
import vehicleObj

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
    rideLines = input[1:len(input)]

    index = 0
    for line in rideLines:
        rideObject = rideObj.RideObj(index,[line[0],line[1]], [line[2], line[3]], line[4], line[5])
        rideObjects.append(rideObject)
        print(rideObject.calcSteps())
        index = index + 1


def stepsToStart(vehicle: vehicleObj, ride: rideObj):
    row_steps = vehicle.ride.start_intersect[0] - ride.start_intersect[0]
    col_steps = vehicle.ride.end_intersect[1] - ride.end_intersect[1]

    if row_steps < 0:
        row_steps = row_steps * (-1)
    else:
        row_steps = row_steps

    if col_steps < 0:
        col_steps = col_steps * (-1)
    else:
        col_steps = col_steps

    return row_steps + col_steps


readMatrix("dataSet/a_example.in")



