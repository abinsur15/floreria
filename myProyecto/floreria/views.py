from django.shortcuts import render,redirect
from .forms import CustomUserForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import login,authenticate
from .models import Flor

from rest_framework import viewsets
from .serializers import florserializer

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseBadRequest

from django.core import serializers
import json

from fcm_django.models import FCMDevice
# Create your views here.

@csrf_exempt
@require_http_methods(['POST'])
def guardar_token(request):
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)

    token = bodyDict['token']

    existe = FCMDevice.objects.filter(registration_id = token, active=True)

    if len(existe) > 0:
        return HttpResponseBadRequest(json.dumps({'Mensaje':'el token ya existe'}))

    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True

    if request.user.is_authenticated:
        dispositivo.user = request.user

    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'Mensaje':'token guardado'}))
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'token no se ha podido guardar'}))
    

def inicio(request):

    return render(request, 'core/index.html')
@login_required
def galeria(request):
    flor=Flor.objects.all()
    return render(request, 'core/galeria.html',{'flores':flor})

@permission_required('core.add_flor')
def ingresar(request):
    return render(request, 'core/ingresar.html')

@login_required
def carrito(request):
    return render(request, 'core/carrito.html')

def quienes(request):
    return render(request, 'core/quienes.html')

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method =='POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)

          #  dispositivos = FCMDevice.objects.filter(active=True)
           # dispositivos.send_message(
            #title="Usuario nuevo",
           # body="Se ha creado una nueva cuenta", 
           # icon="/static/img/logofloreria.png"
    #)
            return redirect(to='INICIO')

    return render (request,'registration/registro.html',data)

class FlorViewset(viewsets.ModelViewSet):
    queryset =  Flor.objects.all()
    serializer_class = florserializer

