import requests
import json
import base64
import time
import board
import neopixel_spi as neopixel
#sets up neopixel
NUM_PIXELS = 11
PIXEL_ORDER = neopixel.RGB

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(
    spi, NUM_PIXELS, pixel_order=PIXEL_ORDER
)
#turns all lights off
def ledoff():
    pixels.deinit()
pixels.brightness = 0.3

#gets header used to access spotify api
def getaheader():
    #client username and password
    clientid = "b3186d148d7943298d295f09f6c264f8"
    clientsec = "919a4d95eada4419af540dfb5e53d82c"
    #allows api to accept id and password
    client = clientid + ":" + clientsec
    bytesid = client.encode('ascii')
    basicenc = base64.b64encode(bytesid)
    basic = basicenc.decode('ascii')
    #token needed to access
    rtoken = 'AQDFyYwEATPtg6Q2XuF_Q86Tx8LYWXuj-fkTyrMeJ_nb8VP8UwDpkAxEC1cJ6Yu4xYt5HoLOVANoVgalq366PvAtXZhfxWTp3g5VsTeoZ4B4rofKg3Wo8ZbJuK1gQB5GgdI'
    theaders = {'Authorization': 'basic ' + basic}
    #api request sent
    atoken = requests.post('https://accounts.spotify.com/api/token', headers=theaders, data={'grant_type': 'refresh_token', 'refresh_token': rtoken})
    atokenstr = json.loads(atoken.content)
    #seperates the access token from the rest
    accesstoken = atokenstr['access_token']
    headers = {'Accept': 'application/json', 'Content-Type':'application/json', 'Authorization': 'Bearer ' + accesstoken}
    return headers

headers = getaheader()
#api request for current volume
def getvolume():
    info = requests.get('https://api.spotify.com/v1/me/player', headers=headers)
    infostr = json.loads(info.content)
    volmeper = int(infostr['device']['volume_percent'])
    return volmeper


blue = (255,0,0)
blue1 = (0,255,0)
blue2 = (0,0,255)
#light control function
def vollight():
    #gets current volume
    volumper = getvolume()
    pvolumper = volumper
    if volumper == pvolumper:
        volumper = getvolume()
    #turns on certain amount of lights in accordance to current volume
    if volumper == 100:
        pixels[0] = blue2
        pixels[2] = blue
        pixels[3] = blue1
        pixels[4] = blue2
        pixels[6] = blue
        pixels[7] = blue1
        pixels[8] = blue2
        pixels[10] = blue
    if volumper == 88:
        ledoff()
        pixels[2] = blue
        pixels[3] = blue1
        pixels[4] = blue2
        pixels[6] = blue
        pixels[7] = blue1
        pixels[8] = blue2
        pixels[10] = blue
    if volumper == 76:
        ledoff()
        pixels[3] = blue1
        pixels[4] = blue2
        pixels[6] = blue
        pixels[7] = blue1
        pixels[8] = blue2
        pixels[10] = blue
    if volumper == 64:
        ledoff()
        pixels[4] = blue2
        pixels[6] = blue
        pixels[7] = blue1
        pixels[8] = blue2
        pixels[10] = blue
    if volumper == 52:
        ledoff()
        pixels[6] = blue
        pixels[7] = blue1
        pixels[8] = blue2
        pixels[10] = blue
    if volumper == 40:
        ledoff()
        pixels[7] = blue1
        pixels[8] = blue2
        pixels[10] = blue
    if volumper == 28:
        ledoff()
        pixels[8] = blue2
        pixels[10] = blue
    if volumper == 16:
        ledoff()
        pixels[10] = blue
    if volumper == 4:
        ledoff()
    print(volumper)
    pvolumper = volumper

vollight()

def volumeup():
    volumper = getvolume()
    requests.put('https://api.spotify.com/v1/me/player/volume?volume_percent=' + str(volumper + 12), headers=headers)

def volumedown():
    volumper = getvolume()
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

def previoussong():
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


