from django import forms
from .models import bikeuser, tblmotorbike
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MotorbikeForm(forms.ModelForm):
    class Meta:
        model = tblmotorbike
        fields = '__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model = bikeuser
        fields = '__all__'

class CustomerRegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User

        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )