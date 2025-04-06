import phonenumbers
from phonenumbers import geocoder #geocoder used to determine then loaction of the ph no
from test import number
import folium #folium used to create map 

key="cbe50fadc3334f0ca5b45b22e75e15e4"

number= input("Enter phone number with country code:  ")
check_number = phonenumbers.parse(number)
number_loc = geocoder.description_for_number(check_number,"en")
print(number_loc)

#service provider 
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(number_loc)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

#pointer on map 
map_loc = folium.Map(loc=[lat,lng],zoom_start = 9)
folium.Marker([lat,lng],popup = number_loc).add_to(map_loc)
map_loc.save("mylocation.html")  