from django import forms
from .models import Reservacion,Servicio

class ReservacionForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ['nombre_cliente','telefono_cliente','servicio','fecha','hora']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type':'time'}),
        }