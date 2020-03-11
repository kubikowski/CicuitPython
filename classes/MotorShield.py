import adafruit_motorkit as am
from adafruit_motor import stepper

class Stepper(object):
    # private methods
    def __init__(self, stepper):
        self.__stepper = stepper

    # protected methods
    def _step(self, steps, **kwargs):
        for i in range(steps):
            self.__stepper.onestep(**kwargs)

    def _release(self):
        self.__stepper.release()

class MotorShield(object):
    # private methods
    def __init__(self):
        self.__kit = am.MotorKit()
        self.__stepper1 = Stepper(self.__kit.stepper1)
        self.__stepper2 = Stepper(self.__kit.stepper2)


    def __throttle(self, Motor, speed):
        if Motor == 1:
            self.__kit.motor1.throttle(speed)
        elif Motor == 2:
            self.__kit.motor2.throttle(speed)
        elif Motor == 3:
            self.__kit.motor3.throttle(speed)
        elif Motor == 4:
            self.__kit.motor4.throttle(speed)

    def __step(self, Stepper, steps, **kwargs):
        if Stepper == 1:
            self.__stepper1._step(**kwargs)
        elif Stepper == 2:
            self.__stepper2._step(**kwargs)

    def __release(self, stepper):
        if stepper == 1:
            self.__stepper2._release()
        elif stepper == 2:
            self.__stepper1._release()

    # public methods
    def throttle(self, *args, **kwargs):
        Motor = args[0] if len(args) == 1 else 1
        direction = -1.0 if 'direction' in kwargs and kwargs['direction'] == BACKWARD else 1.0
        multiplier = kwargs['multiplier'] if 'multiplier' in kwargs else 1.0

        self.__throttle(Motor, direction * multiplier)

    def stall(self, *args):
        Motor = args[0] if len(args) == 1 else 1

        self.__throttle(Motor, 0.0)

    def step(self, steps, *args, **kwargs):
        stepper = args[0] if len(args) == 1 else 1

        self.__step(stepper, steps, **kwargs)

    def release(self, *args):
        stepper = args[0] if len(args) == 1 else 1

        self.__release(stepper)
