import adafruit_motorkit as am
from adafruit_motor import stepper

class MotorShield(object):
    # private methods
    def __init__(self):
        self.__kit = am.MotorKit()

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
            for i in range(steps):
                self.__kit.stepper1.onestep(**kwargs)
        elif Stepper == 2:
            for i in range(steps):
                self.__kit.stepper2.onestep(**kwargs)

    def __release(self, Stepper):
        if Stepper == 1:
            self.__kit.stepper2.release()
        elif Stepper == 2:
            self.__kit.stepper1.release()

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
        Stepper = args[0] if len(args) == 1 else 1

        self.__step(Stepper, steps, **kwargs)

    def release(self, *args):
        Stepper = args[0] if len(args) == 1 else 1

        self.__release(Stepper)
