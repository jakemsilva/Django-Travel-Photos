from django import forms
from django.contrib.auth.models import User
from trips.models import Trip, Experience, Picture
from django_countries.fields import CountryField

class TripForm(forms.ModelForm):
    title = forms.CharField(max_length=200, help_text="Please enter the title of your trip.")
    country = CountryField()
    
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Trip

        exclude = ('user','slug','lat_lng',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')
        
class ExperienceForm(forms.ModelForm):
    title = forms.CharField(max_length=200, help_text="Please enter the title of the page.")
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Experience

        exclude = ('trip',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views') 
        
class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = ('experience','picture_big','picture_small',)