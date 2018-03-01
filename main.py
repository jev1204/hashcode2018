#!/usr/bin/python

import numpy as np
import sys
import rideObj

from rideObj import RideObj
from vehicleObj import VehicleObj

firstLine = []
rideObjects = []
vehicle_objects = []
current_step = 0
# TODO: set value
max_steps = 9999999
F = 0

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

    rideLines = input[1:len(input)]

    index = 0
    for line in rideLines:
        rideObject = rideObj.RideObj(index,[line[0],line[1]], [line[2], line[3]], line[4], line[5])
        rideObjects.append(rideObject)
        print(rideObject.calcSteps())
        index = index + 1


def __init__():
    current_step = 0
    readMatrix("dataSet/a_example.in")
    create_vehicles(F)

    while current_step <= max_steps:
        for vehicle in vehicle_objects:
            if vehicle.finish_step == current_step:
                add_step_to_vehicle(vehicle)
        current_step += 1


def create_vehicles(vehicle_count: int):
    for i in range(vehicle_count):
        vehicle_objects.append(VehicleObj(i))


def add_step_to_vehicle(vehicle: VehicleObj):
    vehicle.currentRideObj = get_shortest_ride()


def sort_rides_by_start_steps(rides: list[RideObj]):
    sorted_rides = sorted(rides, key=getattr('startSteps'))


def get_shortest_ride() -> rideObj:
    pass

