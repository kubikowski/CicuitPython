# Path Variables
from sys import path
path.insert(1, '/classes')
path.insert(2, '/controllers')
path.insert(3, '/services')

# Imports
import utilityService as util
import motorShieldController as motors

# Setup
util.setup()

# Main
while True:
    steps = util.getInput('Type any character to continue: ')
    motors.strikeGong(steps)
