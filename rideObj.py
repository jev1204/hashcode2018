class RideObj:
    startIntersect = [0,0]
    endIntersect = [0, 0]
    startStep = 0
    finishStep = 0
    neededSteps = 0
    id = 0

    def __init__(self, id, startIntersect, endIntersect, startStep, finishStep):
        self.id = id
        self.startIntersect = startIntersect
        self.endIntersect = endIntersect
        self.startStep = startStep
        self.finishStep = finishStep

        self.neededSteps = self.calcSteps()

    def calcSteps(self):
        rowSteps = self.endIntersect[0] - self.startIntersect[0]
        colSteps = self.endIntersect[1] - self.startIntersect[1]

        if rowSteps < 0:
            rowSteps = rowSteps * (-1)
        else:
            rowSteps = rowSteps

        if colSteps < 0:
            colSteps = colSteps * (-1)
        else:
            colSteps = colSteps

        return rowSteps + colSteps