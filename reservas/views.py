from django.shortcuts import render, redirect
from .forms import ReservacionForm
from .models import Reservacion

# Create your views here.
def hacer_reservacion(request):
    if request.method == 'POST':
        form = ReservacionForm(request.POST)
        if form.is_valid():
            reservacion = form.save()
            return render(request,'main/templates/main/index.html',{'form': form, 'reservacion': reservacion})
    else:
        form = ReservacionForm()
    return render(request, 'main/templates/main/index.html', {'form': form})
        