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
        'content': 'La vision de la empresa',
        'mensaje_vision': 'Es algo bonito.'
    })


def vision(request):
    return render(request,'mainapp/vision.html',{
        'title':'vision',
        'content': 'La vision de la empresa',
        'mensaje_vision': 'Es una muy buena.'
    })