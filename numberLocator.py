import phonenumbers
import folium
from myNumber import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

# API key from Opencage
key = ""

# Locate the number
thisNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(thisNumber, "en")
print(yourLocation)


# get service provider

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

geocoder = OpenCageGeocode(key)
query = str(yourLocation)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng],zoom_start=9)

folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

myMap.save("myLocation.html")
