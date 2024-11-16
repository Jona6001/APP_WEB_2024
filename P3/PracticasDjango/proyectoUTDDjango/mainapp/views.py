from django.shortcuts import render, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    mensaje= 'hola soy un mensaje'
    return render(request,'mainapp/index.html',{
    'title':'Inicio',
    'mensaje': mensaje ,
        'content': '.:: !Bienvenido! : ..'
})

def about(request):
    return render(request,'mainapp/about.html',{
        'title' : 'Acerca de nosostros',
        'content' : 'somos un equipo de Desarrollo de SW'
    })

def mision(request):
    return render(request,'mainapp/mision.html',{
        'title':'mision',
        'content': 'La Mision de la empresa',
        'mensaje_mision': 'La Misión de la Universidad Tecnológica de Durango (UTD)es una muy padre'
    })

def vision(request):
    return render(request,'mainapp/vision.html',{
        'title':'vision',
        'content': 'La vision de la empresa',
        'mensaje_vision': 'La visión de la Universidad Tecnológica de Durango (UTD) esta bonita'
    })

def page404(request,exception):
    return render(request,'mainapp/404.html',status=404)