# transportation
This REST api based on Django framework will help loading/retrieving geo data based on longitude/latitude of a location

https://nominatim.openstreetmap.org/reverse.php?lat=40.7127281&lon=-74.0060152&polygon_geojson=1&format=json
is being used to display all the polygons of a given longitude/latitude


Tools used:
  PyCharm
  sqlite3

Additional External APIs
  https://github.com/geopy/geopy

Example of data set:
  https://nominatim.openstreetmap.org/reverse?polygon_geojson=1&format=json&polygon_threshold=0.0

Steps to run:
  1.  checkout:https://github.com/mamtach/transportation
  2.  Run the command: python manage.py runserver

URLs Mapping:
  List of providers: http://localhost/providers/
  Detailed data for provider: http://localhost/providers/1/
  List of polygon: http://localhost/polygons/
  Detailed data for a polygon: http://localhost/polygons/1

PNG files (Django Rest api screens) are attached for Reference.
