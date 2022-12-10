from django import forms
from . import models

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ('last_first_name','email','adress','phone_number','information')

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ('status','cart','last_first_name','email','adress','phone_number','information')

class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ('information',)