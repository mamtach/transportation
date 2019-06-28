from django.urls import path

from .apiviews import PolygonList,PolygonDetail,ProviderList, ProviderDetail

urlpatterns = [
    path("polygons/", PolygonList.as_view(), name="polygon_list"),
    path("polygons/<int:pk>/", PolygonDetail.as_view(), name="polygon_detail"),
    path("providers/", ProviderList.as_view(), name="provider_list"),
    path("providers/<int:pk>/", ProviderDetail.as_view(), name="provider_detail"),
]