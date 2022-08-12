import time
import board
import busio
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7789 import ST7789
import digitalio
from board import *
import random

# Release any resources currently in use for the displays
displayio.release_displays()

# Init display
tft_cs = board.GP17
tft_dc = board.GP16
spi_mosi = board.GP19
spi_clk = board.GP18
spi = busio.SPI(spi_clk, spi_mosi)

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(
    display_bus, rotation=-270, width=240, height=135, rowstart=40, colstart=53)
splash = displayio.Group()
display.show(splash)

# Init buttons
A = digitalio.DigitalInOut(GP12)
B = digitalio.DigitalInOut(GP13)
X = digitalio.DigitalInOut(GP14)
Y = digitalio.DigitalInOut(GP15)
A.switch_to_input(pull=digitalio.Pull.UP)
B.switch_to_input(pull=digitalio.Pull.UP)
X.switch_to_input(pull=digitalio.Pull.UP)
Y.switch_to_input(pull=digitalio.Pull.UP)

streak = 1
score = 0
questions = 0

while True: # Main game loop
    if questions == 10:
        f = open("hi-score.txt", "r")
        highScore = int(f.read())
        f.close()
        winScreen = displayio.Group()
        display.show(winScreen)
        if score > highScore:
            text = f"You beat the\nHigh-Score!\nIt was {highScore}\nNow it's {score}!"
            f = open("hi-score.txt", "w")
            f.write(str(score))
            f.close()
        else:
            text = f"Congrats!\nYour score for this\nround is {score}! The \nHigh-Score is {highScore}"
        text_area = label.Label(terminalio.FONT, text=text, scale=2, color=0xFFFFFF, x=10, y=10)
        winScreen.append(text_area)
        time.sleep(2)
        while True:
            if not A.value or not B.value or not X.value or not Y.value:
                score = 0
                questions = 0
                break 
    questions += 1
    attempts = 0

        

    splash = displayio.Group()
    display.show(splash)
    color = hex(random.randint(0, 16777215))
    color_bitmap = displayio.Bitmap(240, 67, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = int(color)
    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.insert(0, bg_sprite)

    fakecolor1 = hex(random.randint(0, 16777215))
    fakecolor2 = hex(random.randint(0, 16777215))
    fakecolor3 = hex(random.randint(0, 16777215))
    colorlist = [fakecolor1, fakecolor2, fakecolor3, color]
    shuffledcolorlist = []
    for i in range(4):
        randomcolor = colorlist[random.randint(0, len(colorlist)-1)]
        shuffledcolorlist.append(randomcolor)
        colorlist.remove(randomcolor)
    
    text = f"Guess The Hex Q{questions}:\nY = {shuffledcolorlist[3]}, B = {shuffledcolorlist[1]}\nX = {shuffledcolorlist[2]}, A = {shuffledcolorlist[0]}\nStreak = {streak-1}, Score = {score}"
    text_area = label.Label(terminalio.FONT, text=text, scale=1, color=0xFFFFFF, y=77, x=45)
    splash.insert(1, text_area)
    time.sleep(0.5) # Give the user time to let go of the button from last question
    print(attempts)
    while True:
        if not A.value:
            attempts += 1
            if shuffledcolorlist[0] == color:
                break
            else:
                streak = 0
                time.sleep(0.2)
        if not B.value:
            attempts += 1
            if shuffledcolorlist[1] == color:
                break
            else:
                streak = 0
                time.sleep(0.2)
        if not X.value:
            attempts += 1
            if shuffledcolorlist[2] == color:
                break
            else:
                streak = 0
                time.sleep(0.2)
        if not Y.value:
            attempts += 1
            if shuffledcolorlist[3] == color:
                break
            else:
                streak = 0
                time.sleep(0.2)
    streak += 1
    if attempts == 1:
        score += 2
    elif attempts == 2:
        score += 1
    elif score == 3:
        score -= 2
    elif attempts >= 4:
        score -= 3