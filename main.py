#!/usr/bin/python

import numpy as np
import sys

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
    



readMatrix("dataSet/a_example.in")



