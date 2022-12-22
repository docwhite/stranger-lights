# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

# FINAL_COL = (225, 60, 18)
FINAL_COL = (230, 70, 20)
RED = (255, 0, 0)

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 50

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False,
                           pixel_order=ORDER)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    r = int(r * 0.2)
    g = int(g * 0.2)
    b = int(b * 0.2)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


for x in range(2):
   rainbow_cycle(0.001)    # rainbow cycle with 1ms delay per step

pixels.fill(FINAL_COL)
pixels.show()

# time.sleep(180)

for x in range(100):
  pixels.fill(RED)
  pixels.show()
  time.sleep(0.05)
  pixels.fill(FINAL_COL)
  pixels.show()
  time.sleep(0.05)

pixels.fill((255, 0, 0))
pixels.show()
time.sleep(0.5)

for x in range(100):
  r = RED[0] + (FINAL_COL[0] - RED[0]) * (x / 100)
  g = RED[1] + (FINAL_COL[1] - RED[1]) * (x / 100)
  b = RED[2] + (FINAL_COL[2] - RED[2]) * (x / 100)
  pixels.fill((r, g, b))
  pixels.show()
  time.sleep(0.05)

# from subprocess import call
# call("sudo shutdown -h now", shell=True)
