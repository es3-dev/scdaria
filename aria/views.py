from django.shortcuts import render, redirect
from .models import Reunion, Asistencia, Sede
from django.urls import reverse

# Create your views here.
def crearReunion(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        fecha = request.POST['fecha']
        sede = request.POST['sede']
        reunion = Reunion.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            fecha=fecha,
            sede=sede
        )
        return redirect(reverse('detalleReunion', args=[reunion.id]))
    return render(request, 'crear_reunion.html')

def detalleReunion(request, reunion_id):
    reunion = Reunion.objects.get(id=reunion_id)
    link_asistencia = request.build_absolute_uri(
        reverse('formulario_asistencia', args=[reunion_id])
    )
    return render(request, 'detalle_reunion.html', {
        'reunion': reunion,
        'link_asistencia': link_asistencia
    })

def crearFormulario(request, reunion_id):
    if request.method == 'POST':
        
