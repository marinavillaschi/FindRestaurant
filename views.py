from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant
from findrestaurant import FindRestaurant

engine = create_engine('sqlite:///restaurant.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route("/restaurants", methods = ['GET', 'POST'])
def restaurantFunction():
  if request.method == 'GET':
    #Call the method to view all of the restaurants in the db
    return getAllRestaurants()
  
  elif request.method == 'POST':
    #Call the method to post a new restaurant into the db
    print ("Posting new restaurant into the db")
    mealType = request.args.get('mealType', '')
    location = request.args.get('location', '')
    restaurant_info = FindRestaurant(mealType, location)
    if restaurant_info != "No Restaurants Found":
      return postNewRestaurant(restaurant_info['name'], restaurant_info['address'], restaurant_info['image'])
    else:
      return jsonify({"error": "No restaurants found for %s in %s" %(mealType, location)})

#Make another app.route() decorator here that takes in an integer id in the URI
@app.route("/restaurant/<int:id>", methods = ['GET', 'PUT', 'DELETE'])
#Call the method to view a specific restaurant by its id
def restaurantFunctionId(id):
  if request.method == 'GET':
    return getRestaurant(id)
    
  #Call the method to edit a specific restaurant  
  elif request.method == 'PUT':
    name = request.args.get('name')
    address = request.args.get('address')
    image = request.args.get('image')
    return updateRestaurant(id, name, address, image)
    
 #Call the method to remove a specific restaurant 
  elif request.method == 'DELETE':
    return deleteRestaurant(id)

def getAllRestaurants():
  restaurant = session.query(Restaurant).all()
  return jsonify(restaurant=[i.serialize for i in restaurant])

def getRestaurant(id):
  restaurant = session.query(Restaurant).filter_by(restaurant_id = id).one()
  return jsonify(restaurant=restaurant.serialize) 
  
def postNewRestaurant(restaurant_name, restaurant_address, pic_url):
  restaurant = Restaurant(restaurant_name = restaurant_name, restaurant_address = restaurant_address, pic_url = pic_url)
  session.add(restaurant)
  session.commit()
  return jsonify(restaurant=restaurant.serialize)

def updateRestaurant(id, name, address, image):
  restaurant = session.query(Restaurant).filter_by(restaurant_id = id).one()
  if not name:
    restaurant.restaurant_name = name
  if not address:
    restaurant.restaurant_address = address
  if not image:
    restaurant.pic_url = image
  session.add(restaurant)
  session.commit()
  return jsonify(restaurant=restaurant.serialize)

def deleteRestaurant(id):
  restaurant = session.query(Restaurant).filter_by(restaurant_id = id).one()
  session.delete(restaurant)
  session.commit()
  return "Removed restaurant with id %s" % id


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	