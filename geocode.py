import requests
from decouple import config

def getGeocodeLocation(inputString):
    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    GOOGLE_API_KEY = config("GOOGLE_API_KEY")
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, GOOGLE_API_KEY))
    result = requests.get(url).json()
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    # print(latitude, longitude)
    return latitude,longitude

if __name__ == '__main__':
    getGeocodeLocation("Dallas, Texas")