from django.shortcuts import render, redirect
from reservas.forms import ReservacionForm
from reservas.models import Reservacion, Servicio

def index(request):
    servicios = Servicio.objects.all()
    if request.method == 'POST':
        form = ReservacionForm(request.POST)
        if form.is_valid():
            reservacion = form.save()
            return render(request, 'main/index.html', {'form': form, 'reservacion': reservacion, 'servicios': servicios})
    else:
        form = ReservacionForm()
    return render(request, 'main/index.html', {'form': form, 'servicios': servicios})
