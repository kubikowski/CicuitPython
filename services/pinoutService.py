# ------------------------------------------------------------------------------
# Imports
import board
import analogio
import digitalio

# ------------------------------------------------------------------------------
# Pins
RED_LED_PIN = board.D13
GREEN_LED_PIN = board.D3
DAC_PIN = board.A0

# ------------------------------------------------------------------------------
# Leds
redLed = digitalio.DigitalInOut(RED_LED_PIN)
greenLed = digitalio.DigitalInOut(GREEN_LED_PIN)

# ------------------------------------------------------------------------------
# AnalogOut
dac = analogio.AnalogOut(DAC_PIN)
