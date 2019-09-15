# -----------------------------------------------------------------------------
# Path Variables
from sys import path
path.insert(1, '/scripts')
path.insert(2, '/services')

# -----------------------------------------------------------------------------
# Imports
import util
import test

# -----------------------------------------------------------------------------
# Setup
util.setup()

# -----------------------------------------------------------------------------
# Main
while True:
    test.counting()
    util.getInput('Type any character to continue: ')