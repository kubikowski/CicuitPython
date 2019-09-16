import adafruit_motorkit as am
from adafruit_motor import stepper

class MotorShield(object):
    def __init__(self):
        self.kit = am.MotorKit()

    def steps(self, steps, **kwargs):
        direction = kwargs[direction] if 'direction' in kwargs.keys() else stepper.FORWARD
        style = kwargs[style] if 'style' in kwargs.keys() else style = stepper.SINGLE

        for i in range(steps):
            self.kit.stepper1.onestep(direction=direction, style=style)

    def release(self):
        self.kit.stepper1.release()
