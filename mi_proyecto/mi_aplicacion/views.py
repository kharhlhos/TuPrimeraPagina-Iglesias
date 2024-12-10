from django.shortcuts import render, redirect
from .models import Autor, Libro, Editorial
from .forms import AutorForm, LibroForm, EditorialForm, BusquedaForm

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AutorForm()
    return render(request, 'mi_aplicacion/formulario.html', {'form': form, 'titulo': 'Crear Autor'})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = LibroForm()
    return render(request, 'mi_aplicacion/formulario.html', {'form': form, 'titulo': 'Crear Libro'})

def crear_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EditorialForm()
    return render(request, 'mi_aplicacion/formulario.html', {'form': form, 'titulo': 'Crear Editorial'})

def buscar_libro(request):
    libros = []
    if 'titulo' in request.GET:
        form = BusquedaForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            libros = Libro.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaForm()
    return render(request, 'mi_aplicacion/buscar.html', {'form': form, 'libros': libros})
