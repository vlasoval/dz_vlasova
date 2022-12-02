from django import forms
from . import models

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ('last_first_name','email','adress','phone_number',)
