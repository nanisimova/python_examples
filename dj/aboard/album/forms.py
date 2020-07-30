from django import forms

from catalog.models import Category

class CreatePhotoForm(forms.Form):
    image = forms.ImageField(required=False)
