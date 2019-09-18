import adafruit_motorkit as am
from adafruit_motor import stepper

class MotorShield(object):
    # private methods
    def __init__(self):
        self.__kit = am.MotorKit()

    def __step1(self, steps, **kwargs):
        for i in range(steps):
            self.__kit.stepper1.onestep(**kwargs)

    def __step2(self, steps, **kwargs):
        for i in range(steps):
            self.__kit.stepper2.onestep(**kwargs)

    # public methods
    def steps(self, steps, *args, **kwargs):
        if len(args) == 1 and args[0] == 2:
            self.__step2(steps, **kwargs)
        else:
            self.__step1(steps, **kwargs)

    def release(self, *args):
        if len(args) == 1 and args[0] == 2:
            self.__kit.stepper2.release()
        else:
            self.__kit.stepper1.release()
