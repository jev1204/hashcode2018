class RideObj:
    start_intersect = [0,0]
    end_intersect = [0, 0]
    start_step = 0
    finish_step = 0
    latest_step = 0
    needed_steps = 0
    id = 0

    def __init__(self, id, start_intersect, end_intersect, start_step, latest_step):
        self.id = id
        self.start_intersect = start_intersect
        self.end_intersect = end_intersect
        self.start_step = start_step
        self.latest_step = latest_step
        self.needed_steps = self.calcSteps()
        self.finish_step = self.start_step + self.needed_steps

    def calcSteps(self):
        row_steps = self.end_intersect[0] - self.start_intersect[0]
        col_steps = self.end_intersect[1] - self.start_intersect[1]

        if row_steps < 0:
            row_steps = row_steps * (-1)
        else:
            row_steps = row_steps

        if col_steps < 0:
            col_steps = col_steps * (-1)
        else:
            col_steps = col_steps

        return row_steps + col_steps