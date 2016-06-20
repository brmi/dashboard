from django import forms
from .models import Days

class DayForm(forms.ModelForm):

    class Meta:
        model = Days
        fields = ('days',)
