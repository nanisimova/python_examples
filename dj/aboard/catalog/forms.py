from django import forms

from catalog.models import Category

class CreateItemForm(forms.Form):
    name = forms.CharField(label='Title', max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Category.objects.all())

class UpdateItemForm(forms.Form):
    name = forms.CharField(label='Title', max_length=255)
    description = forms.CharField(widget=forms.Textarea)
