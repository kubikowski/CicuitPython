import ioService as io
import pinoutService as ps

# Globals
WAIT_TO_START = False

# Methods
def setup():
    io.init()
    if WAIT_TO_START:
        getInput('Type any character to begin: ')
    io.setPWM()
    io.setARef()

def getInput(message):
    ps.redLed.value = True
    result = input(message)
    ps.redLed.value = False
    return result
