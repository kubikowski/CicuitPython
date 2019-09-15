# Path Variables
from sys import path
path.insert(1, '/classes')
path.insert(2, '/scripts')
path.insert(3, '/services')

# Imports
import util
import motorShield as ms

# Setup
util.setup()
ms.setup()

# Main
while True:
    ms.strikeGong()
    util.getInput('Type any character to continue: ')
