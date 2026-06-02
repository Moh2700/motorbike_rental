from django import forms
from .models import tblmotorbike

class MotorbikeForm(forms.ModelForm):
    class Meta:
        model = tblmotorbike
        fields = '__all__'