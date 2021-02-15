import time
import board
import neopixel_spi as neopixel

NUM_PIXELS = 10
PIXEL_ORDER = neopixel.RGB


spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(
    spi, NUM_PIXELS, pixel_order=PIXEL_ORDER
)
vol = 100
pixels[0] = (0,255,0)
pixels[1] = (0,0,255)
pixels[3] = (255,0,0)
pixels[4] = (0,255,0)
pixels[5] = (0,0,255)
pixels[7] = (255,0,0)
pixels[8] = (0,255,0)
pixels[9] = (0,0,255)
pixels.brightness = 0.1
time.sleep(5)
pixels.deinit()

""" while True:
    if vol == 100:
        print(5)
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
        pixels[3] = (255,0,0)
        pixels[4] = (0,255,0)
        pixels[5] = (0,0,255)
        pixels[7] = (255,0,0)
        pixels[8] = (0,255,0)
        pixels[9] = (0,0,255)
        pixels[11] = (255,0,0)
        pixels[12] = (0,255,0)
        pixels[13] = (0,0,255)
        pixels[15] = (255,0,0)
    if vol == 90:
        pixels.deinit()
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
        pixels[3] = (255,0,0)
        pixels[4] = (0,255,0)
        pixels[5] = (0,0,255)
        pixels[7] = (255,0,0)
        pixels[8] = (0,255,0)
        pixels[9] = (0,0,255)
        pixels[11] = (255,0,0)
        pixels[12] = (0,255,0)
        pixels[13] = (0,0,255)
    if vol == 80:
        pixels.deinit()
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
        pixels[3] = (255,0,0)
        pixels[4] = (0,255,0)
        pixels[5] = (0,0,255)
        pixels[7] = (255,0,0)
        pixels[8] = (0,255,0)
        pixels[9] = (0,0,255)
        pixels[11] = (255,0,0)
    if vol == 70:
        pixels.deinit()
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
        pixels[3] = (255,0,0)
        pixels[4] = (0,255,0)
        pixels[5] = (0,0,255)
        pixels[7] = (255,0,0)
        pixels[8] = (0,255,0)
        pixels[9] = (0,0,255)
    if vol == 60:
        pixels.deinit()
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
        pixels[3] = (255,0,0)
        pixels[4] = (0,255,0)
        pixels[5] = (0,0,255)
        pixels[7] = (255,0,0)
        pixels[8] = (0,255,0)
    if vol == 50:
        pixels.deinit()
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
        pixels[3] = (255,0,0)
        pixels[4] = (0,255,0)
        pixels[5] = (0,0,255)
        pixels[7] = (255,0,0)
    if vol == 40:
        pixels.deinit()
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
        pixels[3] = (255,0,0)
        pixels[4] = (0,255,0)
        pixels[5] = (0,0,255)
    if vol == 30:
        pixels.deinit()
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
        pixels[3] = (255,0,0)
        pixels[4] = (0,255,0)
    if vol == 20:
        pixels.deinit()
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
    if vol == 10:
        pixels.deinit()
        pixels[0] = (0,255,0)
    if vol == 0:
        pixels.deinit() """



