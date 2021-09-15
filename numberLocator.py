import phonenumbers
import folium
from myNumber import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

# API key from Opencage
key = "80f07637f41c4fea9051c83cff4216fe"

# Locate the number
thisNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(thisNumber, "en")
print(yourLocation)


# get service provider
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

# query the dictionary for latitude x longitude
geocoder = OpenCageGeocode(key)
query = str(yourLocation)
results = geocoder.geocode(query)

# assign lat x lng
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

# print lat x long in terminal
print(lat, lng)

# pass info onto the html file, open in browser
myMap = folium.Map(location=[lat, lng],zoom_start=9)
folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)
myMap.save("myLocation.html")
