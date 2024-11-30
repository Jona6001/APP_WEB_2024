from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio',
        'content': '.:: Bienvenido a la pagina principal ::.',
    })

@login_required(login_url='inicio')
def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'Acerca de nosotros',
        'content': 'Somos un equipo de desarrollo de SW'
    })
@login_required(login_url='inicio')
def mision(request):
    return render(request, 'mainapp/mision.html', {
        'title': 'Mision',
        'content': 'La mision de la empresa'
    })
@login_required(login_url='inicio')
def vision(request):
    return render(request, 'mainapp/vision.html', {
        'title': 'Vision',
        'content': 'La vision de la empresa'
    })
def page404(request,exception):
    return render(request,'mainapp/404.html', status=404)


def sesion(request):
    return render(request, 'mainapp/sesion.html', {'title': 'Inicio de Sesión'})

def registro(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        register_form=RegisterForm()

        if request.method== "POST":
            register_form=RegisterForm(request.POST)
            
            if register_form.is_valid():
                register_form.save()
                messages.success(request,"Registro Exitoso")
                return redirect('login')

        return render(request, 'users/registro.html', {
            'title': 'Registro de usuarios',
            'register_form':register_form,
            })

def login_user(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == "POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Bienvenido al inicio de sesion")
                return redirect('inicio')
            else:
                messages.warning(request,"NO FUE POSIBLE INICIAR SESION")
        return render(request,'users/login.html',{
            'title':'Inicio de sesion',
            'content':'iniciar sesion',

        })
def logout_user(request):
    logout(request)
    return redirect('inicio')

# def error_404_view(request, exception):
#     return redirect('inicio')