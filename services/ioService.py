import digitalio
import pulseio
import pinoutService as ps

# Globals
FREQUENCY = 1
DUTY_CYCLE = 0x7fff

# Methods
def init():
    ps.redLed.direction = digitalio.Direction.OUTPUT
    ps.greenLed.direction = digitalio.Direction.OUTPUT

def setPWM(pin):
    pulseio.PWMOut(pin, frequency=FREQUENCY, duty_cycle=DUTY_CYCLE)

def setARef(voltage):
    ps.dac.value = voltage
