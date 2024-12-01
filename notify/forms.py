from django import forms
from .models import Tablet
from .models import UserTablet

class TabletForm(forms.ModelForm):
    class Meta:
        model = Tablet
        fields = ['name', 'model_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tablet Name'}),
            'model_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Model Number'}),
        }

class UserTabletForm(forms.ModelForm):
    class Meta:
        model = UserTablet
        fields = ['tablet', 'alarm_time']
        widgets = {
            'tablet': forms.Select(attrs={'class': 'form-control'}),
            'alarm_time': forms.TimeInput(
                format='%H:%M',
                attrs={'class': 'form-control timepicker'}
            ),
        }
