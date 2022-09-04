from django.shortcuts import render, redirect
from django.http import HttpResponse

import construction
from .models import Construction
from .forms import ConstructionForm


def home(request):
    return render(request, 'pages/home.html')

def aboutus(request):
    return render(request, 'pages/us.html')

def constructions(request):
    constructions = Construction.objects.all()
    return render(request, 'demo/index.html', {'constructions': constructions})

def new_construction(request):
    form = ConstructionForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('constructions')
    return render(request, 'demo/new.html', {'form': form})

def edit_construction(request, id):
    construction = Construction.objects.get(id=id)
    form = ConstructionForm(request.POST or None, request.FILES or None, instance=construction)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('constructions')
        
    return render(request, 'demo/edit.html', {'form': form})

def delete(request, id):
    construction = Construction.objects.get(id=id)
    construction.delete()
    return redirect('constructions')
    