import requests
import json
import base64

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

def volumeup():
    headers = getaheader()
    info = requests.get('https://api.spotify.com/v1/me/player', headers=headers)
    infostr = json.loads(info.content)
    volmeper = int(infostr['device']['volume_percent'])
    volup = requests.put('https://api.spotify.com/v1/me/player/volume?volume_percent=' + str(volmeper + 10), headers=headers)

def volumedown():
    headers = getaheader()
    info = requests.get('https://api.spotify.com/v1/me/player', headers=headers)
    infostr = json.loads(info.content)
    volmeper = int(infostr['device']['volume_percent'])
    voldw = requests.put('https://api.spotify.com/v1/me/player/volume?volume_percent=' + str(volmeper - 10), headers=headers)

def pausemusic():
    headers = getaheader()
    pause = requests.put('https://api.spotify.com/v1/me/player/pause', headers=headers)

def playmusic():
    headers = getaheader()
    play = requests.put('https://api.spotify.com/v1/me/player/play', headers=headers)

def previous():
    headers = getaheader()
    prev = requests.post('https://api.spotify.com/v1/me/player/previous', headers=headers)

def nextsong():
    headers = getaheader()
    next = requests.post('https://api.spotify.com/v1/me/player/next', headers=headers)
