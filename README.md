# Raspberry Pi Pin Test
Python program to test all the 40 pin I/O header pins. The PiPinTest program automatically checks that the inputs and outputs correctly drive static voltage levels. The PiSinglePinTest drives a single pin to allow more detailed tests to be done if any faults are identified. This is useful if you buy a secondhand Pi or think you might have damaged one or more of the I/O pins.

More complex testing is not included.

Requires:
- The [GPIO Library](https://sourceforge.net/projects/raspberry-gpio-python/) (Already on most Raspberry Pi OS builds)
- A [Raspberry Pi](http://www.raspberrypi.org/)

## Basic use

### PiPinTest

Ensure that no hardware is connected to the Raspberry Pi. 

Ensure that no other programs are running that interact with the IO pins.

Ensure that all interfaces are disabled in the Raspberry Pi Configuration. While the program tests for them, by the time it is run with the pairs of connections made, then the damage could have been done.

Connect pairs of pins together:
* 3 & 5
* 7 & 11
* 13 & 15
* 19 & 21
* 23 & 29
* 31 & 33
* 35 & 37
* 8 & 10
* 12 & 16
* 18 & 22
* 24 & 26
* 32 & 36
* 38 & 40

Run PiPinTest.py

All pairs of pins will be tested:
* Pull-up and Pull-down on one of each pair at a time is read correctly on both pins
* Pull-up on one pin and output drive low on the other pin correctly reads as low on both pins
* Pull-down on one pin and output drive high on the other pin correctly reads as high on both pins

### PiSinglePinTest

Ensure that no hardware is connected to the Raspberry Pi pin under test. Optionally connect an LED from with 3.3V (via a resistor) to test if the output can drive low or to ground (via a resistor) to test if the output can drive high.

Ensure that no other programs are running that interact with the IO pin under test.

Ensure that all interfaces are disabled for the pin under test in the Raspberry Pi Configuration.

Modify the code to change the value of checkPin to the pin you want to test

Run PiSinglePinTest.py



## Changelog

### V2.0

- Added second program to test a single pin

### V1.0

- Corrected error in I²C pin testing
- Fully tested and works

### V0.2

- Defined all pin pairs
- Added individual test of pull-up/down resistors within a pair of pins

### V0.1

- Initial code.
