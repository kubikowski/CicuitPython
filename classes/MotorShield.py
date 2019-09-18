import adafruit_motorkit as am
from adafruit_motor import stepper

class MotorShield(object):
    def __init__(self):
        self.kit = am.MotorKit()

    def step1(self, steps, **kwargs):
        for i in range(steps):
            self.kit.stepper1.onestep(**kwargs)

    def step2(self, steps, **kwargs):
        for i in range(steps):
            self.kit.stepper2.onestep(**kwargs)

    def steps(self, steps, *args, **kwargs):
        self.step2(steps, **kwargs) if len(args) == 1 and args[0] == 2 else self.step1(steps, **kwargs)

    def release(self):
        self.kit.stepper1.release()
