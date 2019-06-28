from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Polygon

import json

##Ref : https://github.com/geopy/geopy
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='my_app')

# URL = "https://nominatim.openstreetmap.org/reverse?polygon_geojson=1&format=json&polygon_threshold=0.0"

def getPolygons(latitude, longitude):
    with open('input.geojson') as f:
        geojson = json.load(f)

    location = geolocator.reverse((latitude, longitude))

    with open('dump.geojson', 'w') as f:
        json.dump(geojson, f, indent=True)

# Create your views here.
def polygon_list(request):
    MAX_OBJECTS = 20
    polygon = Polygon.objects.all()[:MAX_OBJECTS]

    data = {"results": list(polygon.values("provider_id", "name", "price", "longitude", "latitude"))}

    return JsonResponse(data)

def polygon_detail(request, pk):
    polygon = get_object_or_404(Polygon, pk=pk)

    polys = getPolygons(polygon.latitude, polygon.longitude)

    data = {
       "results": {
         "provider_id": polygon.provider_id,
         "name": polygon.name,
         "price": polygon.price,
         "longitude": polygon.longitude,
         "latitude": polygon.latitude,
        }
    }
    return JsonResponse(data)


