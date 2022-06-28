from django.shortcuts import redirect, render
from .models import Residente, Aporte
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def lista_residentes(request):
    residentes = Residente.objects.all()
    context = {'residentes': residentes}
    return render(request, 'lista_residentes.html', context)

def registroResidente(request):
    return render(request, 'registroResidente.html')

def registrarResidente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        edad = request.POST['edad']
        rut = request.POST['rut']
        contacto = request.POST['contacto']
        enfermedades = request.POST['enfermedades']
        observaciones = request.POST['observaciones']
        residente = Residente.objects.create(nombre=nombre, apellidos=apellidos, edad=edad, rut=rut, contacto=contacto, enfermedades=enfermedades, observaciones=observaciones)
        return redirect("lista_residentes")

def login(request):
    return render(request, 'login.html')    

def agregarObservaciones(request, id):
    residente = Residente.objects.get(id=id)
    return render(request, 'agregarObservaciones.html', {'residente': residente})

def editarResidente(request):
    if request.method == 'POST':
        id = request.POST['id']
        observaciones = request.POST['observaciones']
        residente = Residente.objects.get(id=id)
        residente.observaciones = observaciones
        residente.save()
        return redirect('lista_residentes')

def eliminarResidente(request, id):
    residente = Residente.objects.get(id=id)
    residente.delete()
    return redirect('lista_residentes')

def historialAportes(request):
    aporte = Aporte.objects.all()
    return render(request, 'historialAportes.html', {'aporte': aporte})

def vistaAportador(request, id):
    aporte = Aporte.objects.get(id=id)
    return render(request, 'vistaAportador.html' , {'aporte': aporte})

def index(request):
    return render(request, 'index.html')