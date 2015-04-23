from django.shortcuts import render
from models import Page
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import get_template
from django.template import Context

# Create your views here.


def processCMS(request, recurso):
    if request.method == "GET":
        try:
            fila = Page.objects.get(name=recurso)
            plantilla = get_template('plantilla.html')
            c = Context({'contenido': fila.page})
            renderizado = plantilla.render(c)
            return HttpResponse(renderizado)
        except Page.DoesNotExist:
            return HttpResponseNotFound('Page not found: /%s' % recurso)
    elif request.method == "PUT":
        try:
            cuerpo = request.body
            fila = Page.objects.create(name=recurso, page=cuerpo)
            fila.save()
            return HttpResponse("Nuevo recurso")
        except:
            return HttpResponseNotFound("Error")

def addCSS(request, recurso):
     if request.method == "GET":
        try:
            fila = Page.objects.get(name='css/' + recurso)
            return HttpResponse(fila.page, content_type='text/css')
        except Page.DoesNotExist:
            return HttpResponseNotFound('Page not found: /%s' % recurso)
     elif request.method == "PUT":
        try:
            cuerpo = request.body
            fila = Page.objects.create(name='css/' + recurso, page=cuerpo)
            fila.save()
            return HttpResponse("Add CSS")
        except:
            return HttpResponseNotFound("Error")
    
