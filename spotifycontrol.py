import requests
import json
import base64
import time
import board
import neopixel_spi as neopixel

NUM_PIXELS = 16
PIXEL_ORDER = neopixel.RGB

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(
    spi, NUM_PIXELS, pixel_order=PIXEL_ORDER
)
def ledoff():
    pixels.deinit()
pixels.brightness = 0.5


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


def vollight():
    info = requests.get('https://api.spotify.com/v1/me/player', headers=headers)
    infostr = json.loads(info.content)
    volmeper = int(infostr['device']['volume_percent'])
    if volmeper == 100:
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
    if volmeper == 90:
        ledoff()
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
    if volmeper == 80:
        ledoff()
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
        pixels[3] = (255,0,0)
        pixels[4] = (0,255,0)
        pixels[5] = (0,0,255)
        pixels[7] = (255,0,0)
        pixels[8] = (0,255,0)
        pixels[9] = (0,0,255)
        pixels[11] = (255,0,0)
    if volmeper == 70:
        ledoff()
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
        pixels[3] = (255,0,0)
        pixels[4] = (0,255,0)
        pixels[5] = (0,0,255)
        pixels[7] = (255,0,0)
        pixels[8] = (0,255,0)
        pixels[9] = (0,0,255)
    if volmeper == 60:
        ledoff()
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
        pixels[3] = (255,0,0)
        pixels[4] = (0,255,0)
        pixels[5] = (0,0,255)
        pixels[7] = (255,0,0)
        pixels[8] = (0,255,0)
    if volmeper == 50:
        ledoff()
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
        pixels[3] = (255,0,0)
        pixels[4] = (0,255,0)
        pixels[5] = (0,0,255)
        pixels[7] = (255,0,0)
    if volmeper == 40:
        ledoff()
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
        pixels[3] = (255,0,0)
        pixels[4] = (0,255,0)
        pixels[5] = (0,0,255)
    if volmeper == 30:
        ledoff()
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
        pixels[3] = (255,0,0)
        pixels[4] = (0,255,0)
    if volmeper == 20:
        ledoff()
        pixels[0] = (0,255,0)
        pixels[1] = (0,0,255)
    if volmeper == 10:
        ledoff()
        pixels[0] = (0,255,0)
    if volmeper == 0:
        ledoff()
vollight()
def volumeup():
    info = requests.get('https://api.spotify.com/v1/me/player', headers=headers)
    infostr = json.loads(info.content)
    volmeper = int(infostr['device']['volume_percent'])
    requests.put('https://api.spotify.com/v1/me/player/volume?volume_percent=' + str(volmeper + 10), headers=headers)
    vollight()

def volumedown():
    info = requests.get('https://api.spotify.com/v1/me/player', headers=headers)
    infostr = json.loads(info.content)
    volmeper = int(infostr['device']['volume_percent'])
    requests.put('https://api.spotify.com/v1/me/player/volume?volume_percent=' + str(volmeper - 10), headers=headers)
    vollight()

def pausemusic():
    requests.put('https://api.spotify.com/v1/me/player/pause', headers=headers)

def playmusic():
    requests.put('https://api.spotify.com/v1/me/player/play', headers=headers)

def previous():
    requests.post('https://api.spotify.com/v1/me/player/previous', headers=headers)

def nextsong():
    requests.post('https://api.spotify.com/v1/me/player/next', headers=headers)

