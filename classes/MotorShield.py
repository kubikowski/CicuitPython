import adafruit_motorkit as am

class MotorShield(object):
    def __init__(self):
        self.kit = am.MotorKit()

    def steps(steps):
        for i in range(self, steps):
            self.kit.stepper1.onestep()

    def powerSteps(self, steps):
        for i in range(steps):
            self.kit.stepper1.onestep(style=am.stepper.DOUBLE)

    def smoothSteps(self, steps):
        for i in range(steps):
            self.kit.stepper1.onestep(style=am.stepper.MICROSTEP)

    def release(self):
        self.kit.stepper1.release()
