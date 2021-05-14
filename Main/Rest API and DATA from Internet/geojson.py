import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'                                #?
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:    continue                         #if we press enter instead of entering the location, it asks again

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key                           #adding a element key to parms, read the above if else block

    url = serviceurl + urllib.parse.urlencode(parms)       #making the url, urlencode does what i have a screenshot of in c:, +means space, 2%C means comma

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)             #just the handle of url
    data = uh.read().decode()                                 #actual string after decoding it from utf8 to unicode
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)                                   #creates a dictionary or nested combination of dicts and lists named js
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':           #if js is not true (if json is None then do ->), or the word status is not in the dict js, or status key does not have the value ok in it, do ->
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=2))                  #dumps is opp of loads, it'll print the dictionary with indent of 4

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
