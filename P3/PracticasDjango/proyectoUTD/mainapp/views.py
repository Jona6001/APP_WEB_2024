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
        'mensaje_vision': 'La Misión de la Universidad Tecnológica de Durango (UTD) se enfoca en ser una institución de educación superior reconocida por su calidad académica, vinculación con el sector productivo y su capacidad para formar profesionales competentes y comprometidos con el desarrollo económico y social de su comunidad. Esta visión implica no solo un enfoque en la excelencia educativa, sino también en la innovación, la investigación aplicada y la responsabilidad social, con miras a contribuir al crecimiento sustentable y al bienestar de la región y el país. La UTD busca fortalecer continuamente sus programas académicos, apoyar el desarrollo integral de sus estudiantes, y trabajar de la mano con empresas y organizaciones para asegurar que los egresados puedan enfrentar los desafíos de un mundo laboral globalizado. Además, se enfoca en promover valores como el respeto, la responsabilidad y el compromiso, creando una comunidad educativa que impulse la transformación social a través de la educación.'
    })

def vision(request):
    return render(request,'mainapp/vision.html',{
        'title':'vision',
        'content': 'La vision de la empresa',
        'mensaje_vision': 'La visión de la Universidad Tecnológica de Durango (UTD) se enfoca en ser una institución de educación superior reconocida por su calidad académica, vinculación con el sector productivo y su capacidad para formar profesionales competentes y comprometidos con el desarrollo económico y social de su comunidad. Esta visión implica no solo un enfoque en la excelencia educativa, sino también en la innovación, la investigación aplicada y la responsabilidad social, con miras a contribuir al crecimiento sustentable y al bienestar de la región y el país. La UTD busca fortalecer continuamente sus programas académicos, apoyar el desarrollo integral de sus estudiantes, y trabajar de la mano con empresas y organizaciones para asegurar que los egresados puedan enfrentar los desafíos de un mundo laboral globalizado. Además, se enfoca en promover valores como el respeto, la responsabilidad y el compromiso, creando una comunidad educativa que impulse la transformación social a través de la educación.'
    })