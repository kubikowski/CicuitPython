import digitalio
import pulseio
import pinoutService as ps

# Methods
def init():
    ps.redLed.direction = digitalio.Direction.OUTPUT
    ps.greenLed.direction = digitalio.Direction.OUTPUT

def setPWM(**kwargs):
    pin = kwargs['pin'] if 'pin' in kwargs else ps.PWM_PIN
    frequency = kwargs['frequency'] if 'frequency' in kwargs else 1
    dutyCycle = kwargs['dutyCycle'] if 'dutyCycle' in kwargs else 0x7fff

    pulseio.PWMOut(pin, frequency=frequency, duty_cycle=dutyCycle)

def setARef(**kwargs):
    dac = kwargs['dac'] if 'dac' in kwargs else ps.dac
    voltage = kwargs['voltage'] if 'voltage' in kwargs else 0x7fff

    dac.value = voltage
