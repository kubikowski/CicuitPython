# ------------------------------------------------------------------------------
# Imports
import digitalio
import pulseio

import pinoutService as ps

# ------------------------------------------------------------------------------
# Globals
FREQUENCY = 1
DUTY_CYCLE = 0x7fff
VREF = 0x7fff           # 2.5V

# ------------------------------------------------------------------------------
# Methods
def init():
    ps.redLed.direction = digitalio.Direction.OUTPUT
    ps.greenLed.direction = digitalio.Direction.OUTPUT

def setPWM(pin=ps.RED_LED_PIN, frequency=FREQUENCY, dutyCycle=DUTY_CYCLE):
    pulseio.PWMOut(pin, frequency=frequency, duty_cycle=dutyCycle)

def setARef(voltage=VREF, dac=ps.dac):
    dac.value = voltage