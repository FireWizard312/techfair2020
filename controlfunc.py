import requests
import json
import base64
import time
import board
import neopixel_spi as neopixel
NUM_PIXELS = 11
PIXEL_ORDER = neopixel.RGB

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(
    spi, NUM_PIXELS, pixel_order=PIXEL_ORDER
)
def ledoff():
    pixels.deinit()
pixels.brightness = 0.3


def getaheader():
    clientid = "b3186d148d7943298d295f09f6c264f8"
    clientsec = "919a4d95eada4419af540dfb5e53d82c"
    client = clientid + ":" + clientsec
    bytesid = client.encode('ascii')
    basicenc = base64.b64encode(bytesid)
    basic = basicenc.decode('ascii')
    rtoken = 'AQDFyYwEATPtg6Q2XuF_Q86Tx8LYWXuj-fkTyrMeJ_nb8VP8UwDpkAxEC1cJ6Yu4xYt5HoLOVANoVgalq366PvAtXZhfxWTp3g5VsTeoZ4B4rofKg3Wo8ZbJuK1gQB5GgdI'
    theaders = {'Authorization': 'basic ' + basic}
    atoken = requests.post('https://accounts.spotify.com/api/token', headers=theaders, data={'grant_type': 'refresh_token', 'refresh_token': rtoken})
    atokenstr = json.loads(atoken.content)
    accesstoken = atokenstr['access_token']
    headers = {'Accept': 'application/json', 'Content-Type':'application/json', 'Authorization': 'Bearer ' + accesstoken}
    return headers

headers = getaheader()
def volper():
    info = requests.get('https://api.spotify.com/v1/me/player', headers=headers)
    infostr = json.loads(info.content)
    volmeper = int(infostr['device']['volume_percent'])
    return volmeper


b = (255,0,0)
b1 = (0,255,0)
b2 = (0,0,255)
def vollight():
    volumper = volper()
    pvolumper = volumper
    if volumper == pvolumper:
        volumper = volper()
    if volumper == 100:
        pixels[0] = b2
        pixels[2] = b
        pixels[3] = b1
        pixels[4] = b2
        pixels[6] = b
        pixels[7] = b1
        pixels[8] = b2
        pixels[10] = b
    if volumper == 88:
        ledoff()
        pixels[2] = b
        pixels[3] = b1
        pixels[4] = b2
        pixels[6] = b
        pixels[7] = b1
        pixels[8] = b2
        pixels[10] = b
    if volumper == 76:
        ledoff()
        pixels[3] = b1
        pixels[4] = b2
        pixels[6] = b
        pixels[7] = b1
        pixels[8] = b2
        pixels[10] = b
    if volumper == 64:
        ledoff()
        pixels[4] = b2
        pixels[6] = b
        pixels[7] = b1
        pixels[8] = b2
        pixels[10] = b
    if volumper == 52:
        ledoff()
        pixels[6] = b
        pixels[7] = b1
        pixels[8] = b2
        pixels[10] = b
    if volumper == 40:
        ledoff()
        pixels[7] = b1
        pixels[8] = b2
        pixels[10] = b
    if volumper == 28:
        ledoff()
        pixels[8] = b2
        pixels[10] = b
    if volumper == 16:
        ledoff()
        pixels[10] = b
    if volumper == 4:
        ledoff()
    print(volumper)
    pvolumper = volumper
#add constant
vollight()
def volumeup():
    volumper = volper()
    requests.put('https://api.spotify.com/v1/me/player/volume?volume_percent=' + str(volumper + 12), headers=headers)

def volumedown():
    volumper = volper()
    requests.put('https://api.spotify.com/v1/me/player/volume?volume_percent=' + str(volumper - 12), headers=headers)

def pausemusic():
    requests.put('https://api.spotify.com/v1/me/player/pause', headers=headers)
    pixels.deinit()
    time.sleep(0.1)
    vollight()

def playmusic():
    requests.put('https://api.spotify.com/v1/me/player/play', headers=headers)
    pixels.deinit()
    time.sleep(0.1)
    vollight()

def previous():
    requests.post('https://api.spotify.com/v1/me/player/previous', headers=headers)
    pt = 0
    if pt != 2:
        pixels.deinit()
        time.sleep(0.1)
        vollight()
        pt = pt + 1

def nextsong():
    requests.post('https://api.spotify.com/v1/me/player/next', headers=headers)
    pt = 0
    if pt != 2:
        pixels.deinit()
        time.sleep(0.1)
        vollight()
        pt = pt + 1


