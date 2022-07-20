from cgitb import html
from email.mime import image
from re import I
from urllib import request
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse


from .models import *
from WebApp.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def defInicio(request):
    if request.user.is_authenticated:

        check = buscarAvatar(request.user)
        return render(request, "WebApp/index.html", {"url":buscarAvatar(request.user.id), 'check':check})

    return render(request, "WebApp/index.html")#, {"url":avatares[0].imagen.url})

def buscarAvatar(user):
    avatar = Avatar.objects.filter(user=user)
    if avatar:
        avatarimagen = (avatar[0].imagen.url)
        return avatarimagen
     
    return None

def defNosotros(request):
    about = clsAcercade.objects.all()
    if request.user.is_authenticated:

        return render(request, "WebApp/about.html", {'about1':about, "url":buscarAvatar(request.user.id)})
    return render(request, "WebApp/about.html", {'about1':about})

def defProducts(request):
    paquetes = clsPaquetes.objects.all()
    if request.user.is_authenticated:
        return render(request, "WebApp/products.html", {'paqueteshtml':paquetes, "url":buscarAvatar(request.user.id)})
    return render(request, "WebApp/products.html", {'paqueteshtml':paquetes})

def defContact(request):
    if request.user.is_authenticated:

        return render(request, "WebApp/contact.html", {"url":buscarAvatar(request.user.id)})
    return render(request, "WebApp/contact.html")

def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username =form.cleaned_data['username']
            
            form.save()

            return render(request, "WebApp/login.html", {"mensaje":"Usuario Creado"})
    
    else:
        form = UserRegisterForm()
        return render(request, "WebApp/singup.html", {"form":form})

def login_request(request):

    if request.method == "POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get('username')
            
            contraseña = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contraseña)
            
            if user is not None:
                
                login(request, user)

                return render(request,"WebApp/user.html", {"mensaje":usuario})
            
            else:

                return render(request, "WebApp/login.html", {"mensaje":"Datos incorrectos"})

        else:
            formulario = AuthenticationForm()
            return render(request, "WebApp/login.html", {"mensaje":"Datos incorrectos", 'form':formulario})
    
    formulario = AuthenticationForm()

    return render(request, "WebApp/login.html", {'form':formulario})



def defSearch(request):
    if request.GET.get("producto"):
        producto = request.GET.get("producto", 0)
        busqueda = clsPaquetes.objects.filter(numero__icontains=producto)
        if (len(busqueda.values()) == 0):
            busqueda = [{'name':'NO EXISTE EL PRODUCTO', 'numero':producto}]
            if request.user.is_authenticated:
                return render(request, "WebApp/search.html", {'codigoshtml':busqueda, "url":buscarAvatar(request.user.id)})
            return render(request, "WebApp/search.html", {'codigoshtml':busqueda})
        else:
            if request.user.is_authenticated:
                return render(request, "WebApp/search.html", {"busqueda":busqueda, "url":buscarAvatar(request.user.id)})
            return render(request, "WebApp/search.html", {"busqueda":busqueda})
    else:
        codigos = clsPaquetes.objects.all()
        if request.user.is_authenticated:
            return render(request, "WebApp/search.html", {'codigoshtml':codigos, "url":buscarAvatar(request.user.id)})
        return render(request, "WebApp/search.html", {'codigoshtml':codigos})

### Páginas de Usaurio
@login_required
def defUser (request):
    return render(request, "WebApp/user.html", {"url":buscarAvatar(request.user.id)})

@login_required
def defNew (request):
    if request.method == 'POST':
        new = formPaquetes(request.POST)
        print(new)
        if new.is_valid:
            datos = new.cleaned_data
            #print(datos)
            newProduct = clsPaquetes (name=datos['nombre'],numero=datos['numero'], version=datos['version'], documentacion=datos['documentacion'], licencia=datos['licencia'], fecha=datos['fecha'], tamaño=datos['precio'], imagen=datos['imagen'] ) 
            newProduct.save()
            new = formPaquetes()
            return render(request, "WebApp/new.html", {"new":new, "url":buscarAvatar(request.user.id)})
    else:
        new = formPaquetes()
        return render(request, "WebApp/new.html", {"new":new, "url":buscarAvatar(request.user.id)})

@login_required
def defDelete (request):
    if request.GET.get("deleteCodigo"):
        peticion = request.GET.get("deleteCodigo")
        try:
            deleteProducto = clsPaquetes.objects.get(numero=peticion)
            deleteProducto.delete()
            codigos = clsPaquetes.objects.all()
            return render(request, "WebApp/delete.html", {'codigoshtml':codigos, "url":buscarAvatar(request.user.id)})
        except:
            codigos = [{'name':'NO EXISTE EL PRODUCTO', 'numero':peticion}]
            return render(request, "WebApp/delete.html", {'codigoshtml':codigos, "url":buscarAvatar(request.user.id)})
    else:
        codigos = clsPaquetes.objects.all()
        return render(request, "WebApp/delete.html", {'codigoshtml':codigos, "url":buscarAvatar(request.user.id)})

    

class ListarProductos(LoginRequiredMixin, ListView):
    model = clsPaquetes
    template_name = "WebApp/moreoptions.html"

class DetalleProductos(DetailView):
    model = clsPaquetes
    template_name = "WebApp/detail.html"

class ProductoUpdate(UpdateView):
    model = clsPaquetes
    success_url = "/home/options"
    fields = ['name', 'numero', 'version', 'documentacion', 'licencia', 'fecha', 'tamaño', 'imagen']

class ProductoDelete(DeleteView):
    model = clsPaquetes
    success_url = "/home/options"

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        edit = UserEditForm(request.POST)

        if edit.is_valid:
            inf = edit.cleaned_data

            usuario.email = inf['email']
            usuario.password1 = inf['password1']
            usuario.password2 = inf['password2']
            usuario.save()

            return render(request, "WebApp/user.html", {"url":buscarAvatar(request.user.id)})

    else:

        edit =UserEditForm(initial={'email': usuario.email, "url":buscarAvatar(request.user.id)})

    return render(request, "WebApp/editarperfil.html", {"edit":edit, "usuario":usuario, "url":buscarAvatar(request.user.id)})



