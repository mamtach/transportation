from rest_framework import generics
from .models import Polygon, Provider
from .serializers import PolygonSerializer, ProviderSerializer

#Get a list of entities, or create them. Allows GET and POST.
class PolygonList(generics.ListCreateAPIView):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer

#Retrieve an individual entity details, or delete the entity. Allows GET and DELETE.
class PolygonDetail(generics.RetrieveDestroyAPIView):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer

class ProviderList(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class ProviderDetail(generics.RetrieveDestroyAPIView):
    #can be further filtered, sliced or ordered by the view
    queryset = Provider.objects.all()

    #for validating and deserializing the input and for serializing the output
    serializer_class = ProviderSerializer

