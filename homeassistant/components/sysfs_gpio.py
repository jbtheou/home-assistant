"""
Support for controlling GPIO pins through sysfs.

"""
# pylint: disable=import-error
import logging

from homeassistant.const import (
    EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP)

REQUIREMENTS = ['sysfs-gpio==0.2.1']

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'sysfs_gpio'

# pylint: disable=no-member
def setup(hass, config):
    """Setup the Raspberry PI GPIO component."""
    import sysfs.gpio as GPIO

    def cleanup_gpio(event):
        """Stuff to do before stopping."""

    def prepare_gpio(event):
        """Stuff to do when home assistant starts."""
        hass.bus.listen_once(EVENT_HOMEASSISTANT_STOP, cleanup_gpio)

    hass.bus.listen_once(EVENT_HOMEASSISTANT_START, prepare_gpio)
    return True


def setup_output(port):
    """Setup a GPIO as output."""
    import sysfs.gpio as GPIO
    GPIO.Controller.available_pins.append(port)
    pin = GPIO.Controller.allocate_pin(port, OUTPUT)
    pin.reset()


def write_output(port, value):
    """Write a value to a GPIO."""
    import sysfs.gpio as GPIO
    pin = GPIO.Controller.get_pin(port)
    if value is 0:
         pin.reset()
    if value is 1:
         pin.set()
