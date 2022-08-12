# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Storage logging boot.py file"""
import board
import digitalio
import storage
import time

A = digitalio.DigitalInOut(board.GP12)

A.switch_to_input(pull=digitalio.Pull.UP)

# If the switch pin is connected to ground CircuitPython can write to the drive
storage.remount("/", not A.value)