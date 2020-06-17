# Raspberry Pi Pin Test
Python program to test all the 40 pin I/O header pins. This is useful if you buy a secondhand Pi or think you might have damaged one or more of the I/O pins.

Requires:
- The [GPIO Library](https://sourceforge.net/projects/raspberry-gpio-python/) (Already on most Raspberry Pi OS builds)
- A [Raspberry Pi](http://www.raspberrypi.org/)

## Basic use

Ensure that no hardware is connected to the Raspberry Pi. Connect pairs of pins together:
* TBD

Run PiPinTest.py

All pairs of pins will be tested:
* Pull-up and Pull-down on one of each pair at a time is read correctly on both pins
* Pull-up on one pin and output drive low on the other pin correctly reads as low
* Pull-down on one pin and output drive high on the other pin correctly reads as high

## Changelog



### V0.1

- Initial code.
