# GOOGLE MAPS INTEGRATION


import json
import requests as r
import geopy.distance
from .models import Business


# GET API KEY FOR MAPS
api_key = "Ag8-hbsxZdHNXVz4vYDRoETbbv1sU85mLyKLmIOhB0f7GqSJQNtjriQeSbQk2tqU"

api_url = "http://dev.virtualearth.net/REST/v1/Locations?countryRegion={countryRegion}&adminDistrict={adminDistrict}&locality={locality}&postalCode={postalCode}&addressLine={addressLine}&userLocation={userLocation}&userIp={userIp}&usermapView={usermapView}&includeNeighborhood={includeNeighborhood}&maxResults={maxResults}&key={BingMapsKey}"

def get_coordinates(address, post_code):
    address = address
    pc = post_code
    query = "http://dev.virtualearth.net/REST/v1/Locations?addressLine=" + address + "&postalCode=" + pc + "&key=" + api_key

    # SENDS REQUEST FOR COORDINATES
    data = r.get(query);
    data = data.json()

    # PARSES JSON DATA AND RETURNS COORDINATES AS A LIST
    coordinates = data['resourceSets'][0]['resources'][0]['point']['coordinates']
    
    print(coordinates)
    return coordinates

def get_distance(place_one, place_two):
    # Temporary coord
    #place_two = [-27.84215, 153.28636]

    c1 = (place_one[0], place_one[1])
    c2 = (place_two[0], place_two[1])
    distance = geopy.distance.vincenty(c1, c2).km
    d = round(distance, ndigits=1)
    print(place_two)
    return d

# TESTING
# place_one = [-27.88845, 153.28103]
# place_two = [-27.84215, 153.28636]
# get_distance(place_one, place_two)

def set_coordinates(obj, lat, long):
    b = obj
    b.lat = lat;
    b.long = long;
    b.save()
    
def temp_set_coordinates():
    b = Business.objects.all()
    for i in b:
        if not i.lat and not i.long:
            adr = i.street_number + " " + i.street_name
            coords = get_coordinates(adr, i.postal_code)
            i.lat = coords[0]
            i.long = coords[1]
            i.save()