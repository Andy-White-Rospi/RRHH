from django.shortcuts import render, redirect
from .models import Boleta_permiso

def bol_per(request):
    boleta_permisos = Boleta_permiso.objects.all()
    #print(boleta_permisos[0].id)
    return render(request,'permisos.html',{"boleta_permisos": boleta_permisos})

def guardar_per(request):
    boleta_permiso = Boleta_permiso(Nombre=request.POST['Nombre'],Motivo=request.POST['Motivo'])
    boleta_permiso.save()
    return redirect("/permisos/")

def borrar_per(request,task_id):
    boleta_permiso = Boleta_permiso.objects.get(id=task_id)
    boleta_permiso.delete()
    return redirect("/permisos/")