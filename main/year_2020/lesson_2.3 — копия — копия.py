from geopy.geocoders import Nominatim
geolocator = Nominatim()
loc = geolocator.reverse("33.573256, -111.906344")
print(loc.address)