class RideObj:
    startIntersect = [0,0]
    endIntersect = [0, 0]
    startStep = 0
    finishStep = 0
    neededSteps = 0

    def __init__(self, startIntersect, endIntersect, startStep, finishStep):
        self.startIntersect = startIntersect
        self.endIntersect = endIntersect
        self.startIntersect = startStep
        self.finishStep = finishStep

        self.neededSteps = self.calcSteps()

    def calcSteps(self):
        rowSteps = self.endIntersect[0] - self.startIntersect[0]
        colSteps = self.endIntersect[1] - self.startIntersect[1]

        return rowSteps * colSteps