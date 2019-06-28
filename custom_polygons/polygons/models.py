from django.db import models
from django.contrib.auth.models import User

##Ref: https://buildmedia.readthedocs.org/media/pdf/djangoapibook/latest/djangoapibook.pdf

# Create your models here.

class Provider(models.Model):
      first_name = models.CharField(max_length=100, null=True, blank=True)
      last_name  = models.CharField(max_length=100, null=True, blank=True)
      email      = models.CharField(max_length=100, null=True, blank=True)
      ##created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
      phone_number = models.CharField(validators=[], null=True, blank=True, max_length=15)
      language     = models.CharField(max_length=100, null=True, blank=True)
      currency     = models.CharField(max_length=100, null=True, blank=True)

      def __str__(self):
          return self.email

class Polygon(models.Model):
    provider_id = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name  = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    latitude   = models.FloatField(null=True, blank=True)
    longitude  = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

