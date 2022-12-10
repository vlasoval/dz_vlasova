from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from betterforms.multiform import MultiModelForm
from django.forms.widgets import HiddenInput
from .models import Profile

class SignUpForm(UserCreationForm):
    birthday_date = forms.DateField(help_text='Format: YYYY-MM-DD')
    phone_number = forms.CharField(max_length=30)
    country = forms.CharField(max_length=20)
    city = forms.CharField(max_length=20)
    zip_code = forms.CharField(max_length=20)
    address1 = forms.CharField(max_length=100)
    address2 = forms.CharField(max_length=100,required=False, help_text='*Необязательное поле')
    information = forms.CharField(max_length=20,required=False, help_text='*Необязательное поле')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



User = get_user_model()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password', 'groups')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'birthday_date', 'country', 'city', 'zip_code', 'address1', 'address2', 'information')

class UserEditMultiForm(MultiModelForm):
    form_classes = {
        'user': UserForm,
        'profile': ProfileForm,
    }
    def __init__(self, *args, **kwargs):
        active_user = kwargs.pop('active_user',None)
        super(UserEditMultiForm, self).__init__(*args, **kwargs)
        print(self.fields)
        if not active_user.is_superuser:
            self.forms['user'].fields['groups'].widget = HiddenInput()