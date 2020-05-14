# serializers.py
from rest_framework import serializers

from .models import Business

class BusinessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Business
        fields = ('name',
            'phone_number',
            'facebook_url',
            'opening_hours',
            'mondays_food',
            'mondays_entertainment',
            'b_image',
            'lat',
            'long',
            'postal_code')
