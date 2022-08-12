# Guess the Hex... for Raspberry Pi Pico!

This is a circuitpython script that impliments a version of Guess the Hex to the Raspberry Pi Pico!

# Requirements

* A Raspberry Pi Pico
* A Pimoroni Pico Display Pack (note: other adafruit st7789 displays may work, although the pins used for the buttons may need to be modified.)

# Installation:

1: Install CircuitPython to the Pico
2: `git clone` this repo, or click `download code` on the github website
3: Copy everything to the pico
4: The code should start, if it doesnt, restart the pico by unplugging it and plugging it back in again

# How to unlock the filesystem

In order to read and write to files, the filesystem is set as read-only to the computer, to allow read/write access from the computer, please do the following:

Hold the `A` button (`GP12`) while plugging the pico into the computer