from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Reunion, Asistencia, Sede

def listaReuniones(request):
    reuniones = Reunion.objects.all().order_by('-fecha')
    return render(request, 'aria/reuniones.html', {
        'reuniones': reuniones
    })

def crearReunion(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        fecha = request.POST['fecha']
        sede_id = request.POST['sede']
        sede = get_object_or_404(Sede, id=sede_id)
        
        reunion = Reunion.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            fecha=fecha,
            sede=sede
        )
        
        link_asistencia = request.build_absolute_uri(
            reverse('formulario_asistencia', args=[reunion.id])
        )
        
        asistentes = reunion.asistencia_set.all()
        
        return render(request, 'aria/reunion_creada.html', {
            'reunion': reunion,
            'link_asistencia': link_asistencia,
            'asistentes': asistentes
        })
    
    sedes = Sede.objects.all()
    return render(request, 'aria/crear_reunion.html', {
        'sedes': sedes
    })

def reunionCreada(request, reunion_id):
    reunion = get_object_or_404(Reunion, id=reunion_id)
    asistentes = reunion.asistencia_set.all()
    link_asistencia = request.build_absolute_uri(
        reverse('formulario_asistencia', args=[reunion_id])
    )
    
    return render(request, 'aria/reunion_creada.html', {
        'reunion': reunion,
        'asistentes': asistentes,
        'link_asistencia': link_asistencia
    })

def eliminarReunion(request, reunion_id):
    reunion = get_object_or_404(Reunion, id=reunion_id)
    if request.method == 'POST':
        reunion.delete()
        messages.success(request, 'La reunión ha sido eliminada exitosamente.')
        return redirect('lista_reuniones')
    return redirect('lista_reuniones')

def formularioAsistencia(request, reunion_id):
    reunion = get_object_or_404(Reunion, id=reunion_id)
    return render(request, 'aria/formulario_asistencia.html', {
        'reunion': reunion,
        'vinculacion_choices': Asistencia.VINCULACION_CHOICES
    })

def registrarAsistencia(request, reunion_id):
    if request.method == 'POST':
        reunion = get_object_or_404(Reunion, id=reunion_id)
        es_graduado = request.POST['es_graduado'] == 'true'
        
        # Crear el diccionario de datos base
        datos_asistencia = {
            'reunion': reunion,
            'nombre': request.POST['nombre'],
            'documento': request.POST['documento'],
            'correo': request.POST['correo'],
            'es_graduado': es_graduado
        }
        
        # Agregar vinculación solo si no es graduado
        if not es_graduado:
            vinculacion = request.POST.get('vinculacion')
            if vinculacion:
                datos_asistencia['vinculacion'] = vinculacion
        
        asistencia = Asistencia.objects.create(**datos_asistencia)
        messages.success(request, 'Tu asistencia ha sido registrada exitosamente.')
        return redirect('reunion_creada', reunion_id=reunion_id)
    
    return redirect('formulario_asistencia', reunion_id=reunion_id)

def editarReunion(request, reunion_id):
    reunion = get_object_or_404(Reunion, id=reunion_id)
    
    if request.method == 'POST':
        reunion.titulo = request.POST['titulo']
        reunion.descripcion = request.POST['descripcion']
        reunion.fecha = request.POST['fecha']
        sede = get_object_or_404(Sede, id=request.POST['sede'])
        reunion.sede = sede
        reunion.save()
        
        messages.success(request, 'La reunión ha sido actualizada exitosamente.')
        return redirect('reunion_creada', reunion_id=reunion.id)
    
    sedes = Sede.objects.all()
    return render(request, 'aria/editar_reunion.html', {
        'reunion': reunion,
        'sedes': sedes
    })

def editarAsistencia(request, reunion_id, asistencia_id):
    asistencia = get_object_or_404(Asistencia, id=asistencia_id, reunion_id=reunion_id)
    
    if request.method == 'POST':
        asistencia.nombre = request.POST['nombre']
        asistencia.documento = request.POST['documento']
        asistencia.correo = request.POST['correo']
        asistencia.es_graduado = request.POST['es_graduado'] == 'true'
        
        # Actualizar vinculación solo si no es graduado
        if not asistencia.es_graduado:
            vinculacion = request.POST.get('vinculacion')
            if vinculacion:
                asistencia.vinculacion = vinculacion
            else:
                asistencia.vinculacion = ''
        else:
            asistencia.vinculacion = ''
        
        asistencia.save()
        messages.success(request, 'La asistencia ha sido actualizada exitosamente.')
        return redirect('reunion_creada', reunion_id=reunion_id)
    
    return render(request, 'aria/editar_asistencia.html', {
        'asistencia': asistencia,
        'vinculacion_choices': Asistencia.VINCULACION_CHOICES,
        'reunion': asistencia.reunion
    })

