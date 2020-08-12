from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Business(models.Model):
    
    # GENERAL INFO
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    facebook_url = models.CharField(max_length=500)
    opening_hours = models.CharField(max_length=500)
    #image =  models.CharField(max_length=500)
    # WHATSON INFO
    mondays_food = models.CharField(max_length=500)
    mondays_entertainment = models.CharField(max_length=500)
    mondays_other = models.CharField(max_length=500)
    b_image = models.ImageField(upload_to='main/static') 
    image_url = ""
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    street_number = models.CharField(max_length=10, default ='')
    street_name = models.CharField(max_length=500, default ='')
    locality = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    postal_code = models.CharField(max_length=500, default ='')
    country = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    def set_attributes(self, name, phone_number, address, facebook_url):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.facebook_url = facebook_url

    def get_mondays(self):
        monday_data = {
            'food-drink':self.mondays_food,
            'entertainment':self.mondays_entertainment,
            'other':mondays_other
        }
        return monday_data

class UserData(models.Model):
    user = models.OneToOneField(User,related_name='UserData', on_delete=models.CASCADE)
    lat = models.FloatField()
    long = models.FloatField()

    def get_lat(self):
        return self.lat
    
    def get_long(self):
        return self.long