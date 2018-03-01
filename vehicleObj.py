import rideObj


class VehicleObj:
    current_ride = 0
    currentStep = 0
    vehicle_id = 0
    start_step = 0
    finish_step = 0
    finished_rides = []

    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def setCurrentRide(self, start_step, ride: rideObj):
        if (self.current_ride is not None):
            self.finished_rides.append(self.current_ride)
        self.current_ride = ride
        self.start_step = start_step
        self.finish_step = self.start_step + self.current_ride.needed_steps

    def didRideFinish(self, current_step):
        if self.start_step + self.current_ride.needed_steps <= current_step:
            return True
        else:
            return False
