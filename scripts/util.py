# -----------------------------------------------------------------------------
# Imports

import io
import pinoutService as ps

# -----------------------------------------------------------------------------
# Globals
WAIT_TO_START = True

# -----------------------------------------------------------------------------
# Methods
def setup():
    io.init()

    if WAIT_TO_START:
        getInput('Type any character to begin: ')

    io.setPWM()
    io.setARef()

def getInput(message):
    ps.redLed.value = True
    result = imput(message)
    ps.redLed.value = False
    return result
