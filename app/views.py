from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *
# Create your views here.


def fbv_string(request):
    return HttpResponse('<h1>This is Function based views</h1>')

class Cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1>This is Class based views</h1>')

def fbv_htmlpage(request):
    d={'name':'Muniraji','subject':'Django'}
    return render(request,'fbv_htmlpage.html',d)

class Cbv_htmlpage(View):
    def get(self,request):
        d={'name':'Muniraji','subject':'Django'}
        return render(request,'Cbv_htmlpage.html',d)

def fbv_djangoform(request):
    dfo=Djangoform()
    d={'dfo':dfo}
    if request.method=='POST':
        fd=Djangoform(request.POST)
        if fd.is_valid():
            return HttpResponse(str(fd.cleaned_data))
    return render(request,'fbv_djangoform.html',d)

class Cbv_djangoform(View):
    def get(self,request):
        dfo=Djangoform()
        d={'dfo':dfo}
        return render(request,'Cbv_djangoform.html',d)

    def post(self,request):
        fd=Djangoform(request.POST)
        if fd.is_valid():
            return HttpResponse(str(fd.cleaned_data))

def fbv_modelform(request):
    mfo=Modelform()
    d={'mfo':mfo}
    if request.method=='POST':
        fd=Modelform(request.POST)
        if fd.is_valid():
            fd.save()
            return HttpResponse('Your data is submitted successfully')
    return render(request,'fbv_modelform.html',d)


class Cbv_modelform(View):
    def get(self,request):
        mfo=Modelform()
        d={'mfo':mfo}
        return render(request,'Cbv_modelform.html',d)

    def post(self,request):
        fd=Modelform(request.POST)
        if fd.is_valid():
            fd.save()
            return HttpResponse('Your data is submitted successfully')

def display_profile(request):
    display=Profile.objects.all()
    d={'dis':display}
    return render(request,'display_profile.html',d)

