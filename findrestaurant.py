import requests
from decouple import config
from geocode import getGeocodeLocation

def FindRestaurant(mealType, location):
    lat, long = getGeocodeLocation(location)
    AUTHORIZATION = config("AUTHORIZATION")
    url = ('https://api.foursquare.com/v3/places/nearby?ll=%s,%s&query=%s'% (lat, long, mealType))
    headers = {
    "Accept": "application/json",
    "Authorization": AUTHORIZATION
    }
    response = requests.get(url, headers=headers).json()

    if response:
        # select the first restaurant
        restaurant = response['results'][0]
        restaurant_id = restaurant['fsq_id']
        restaurant_name = restaurant['name']
        restaurant_address = restaurant['location']['address']

        # get 300x300 picture for each restaurant using the fsq_id
        url = ('https://api.foursquare.com/v3/places/%s/photos'% (restaurant_id))
        headers = {
            "Accept": "application/json",
            "Authorization": AUTHORIZATION
        }
        response = requests.get(url, headers=headers).json()
        # h = httplib2.Http()
        # result = json.loads(h.request(url,'GET')[1])


        if response:
            pic = response[0]
            pic_prefix = pic['prefix']
            pic_suffix = pic['suffix']
            pic_url = pic_prefix + "300x300" + pic_suffix
        else:
            pic_url = 'https://cdn.pixabay.com/photo/2020/04/11/22/59/restaurant-closed-5032259_960_720.jpg'

        restaurantInfo = {'name':restaurant_name, 'address':restaurant_address, 'image':pic_url}
        print("Restaurant Name: %s" % restaurantInfo['name'])
        print("Restaurant Address: %s" % restaurantInfo['address'])
        print("Image: %s \n" % restaurantInfo['image'])
        return restaurantInfo

    else:
        print("No Restaurants Found for %s" % location)
        return "No Restaurants Found"

if __name__ == '__main__':
    FindRestaurant("árabe", "Belo Horizonte, Minas Gerais")
    FindRestaurant("sushi", "Belo Horizonte, Minas Gerais")
    FindRestaurant("pizza", "Belo Horizonte, Minas Gerais")
    FindRestaurant("burger", "Belo Horizonte, Minas Gerais")
    FindRestaurant("café", "Belo Horizonte, Minas Gerais")