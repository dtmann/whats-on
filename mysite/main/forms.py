from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import Event, DateModel
#from bootstrap_datepicker_plus import DatePickerInput
from django.forms import widgets, DateTimeField, DateField, DateInput
from django.forms import ModelForm
from . import models
from .models import Business

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class NewBusinessForm(forms.Form):
    name = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=50)
    facebook_url = forms.CharField(max_length=500)
    opening_hours = forms.CharField(max_length=500)
    #image =  forms.CharField(max_length=500)
    mondays_food = forms.CharField(max_length=500)
    mondays_entertainment = forms.CharField(max_length=500)
    mondays_other = forms.CharField(max_length=500)
    b_image = forms.ImageField(label="Image", required = False)
    street_number = forms.CharField(max_length=10)
    street_name = forms.CharField(max_length=500)
    locality = forms.CharField(max_length=500)
    state = forms.CharField(max_length=500)
    postal_code = forms.CharField(max_length=500)
    country = forms.CharField(max_length=500)

class BusinessForm(ModelForm):
    class Meta:
        model = models.Business
        fields = ['name', 'phone_number', 'facebook_url', 'opening_hours', 'mondays_food','mondays_entertainment','mondays_other', 'b_image', 'street_number', 'street_name', 'locality', 'state', 'postal_code', 'country']
# class NewEventForm(forms.Form):
#     event_name = forms.CharField(label = "Event Name:")
#     event_description = forms.CharField(label = "Event Description:")
#     date_of_event = DateTimeField(widget = DateInput(format='%Y-%m-%d'),
#                                    input_formats=('%Y-%m-%d',),
#                                    required=False)
#     event_host = forms.CharField(disabled=True)

#     class Meta:
#         model = DateModel
#         fields = ["date_of_event",]

# class NewEventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields =[            
#             "event_name", "event_description", "event_date", "event_hostname",
#         ]

#         widgets = {
#                 'event_date': forms.DateInput(attrs={'id': 'datetimepicker12'}),
#         }

class CordinatesForm(forms.Form):
    lat = forms.FloatField()
    long = forms.FloatField()