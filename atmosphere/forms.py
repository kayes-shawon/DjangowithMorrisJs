from .models import Atmos
from django.forms import ModelForm

class AtmosForm(ModelForm):
    class Meta:
        model = Atmos
        fields = ['date', 'sensor1_temp', 'sensor2_temp', 'sensor3_temp', 'sensor4_temp']
