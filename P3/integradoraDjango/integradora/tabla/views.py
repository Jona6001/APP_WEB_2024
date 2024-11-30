from django.shortcuts import render, redirect
from .models import Servicios

def index(request):
    if request.method == 'POST':
        # Inserción o actualización
        servicio_id = request.POST.get('Servicio_ID')
        nombre = request.POST['Nombre']
        descripcion = request.POST['Descripcion']
        costo = request.POST['Costo']
        activo = 'Activo' in request.POST

        if servicio_id:  # Si existe un ID, actualizamos
            servicio = Servicios.objects.get(pk=servicio_id)
            servicio.Nombre = nombre
            servicio.Descripcion = descripcion
            servicio.Costo = costo
            servicio.Activo = activo
            servicio.save()
        else:  # Si no hay ID, creamos un nuevo servicio
            Servicios.objects.create(
                Nombre=nombre,
                Descripcion=descripcion,
                Costo=costo,
                Activo=activo
            )
        return redirect('inicio')

    # Lectura de todos los datos
    servicios = Servicios.objects.all()
    return render(request, 'tabla/index.html', {
        'title': 'Gestión de Servicios',
        'servicios': servicios,
    })

def eliminar_servicio(request, servicio_id):
    servicio = Servicios.objects.get(pk=servicio_id)
    servicio.delete()
    return redirect('inicio')
