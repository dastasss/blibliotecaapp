from django.shortcuts import render, redirect
from .models import Libro, Autor
from .forms import LibroForm, AutorForm
from .utils import ejecutar_consulta_row

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/listar_libros.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/crear_libro.html', {'form': form})

def actualizar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/actualizar_libro.html', {'form': form})

def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'libros/eliminar_libro.html', {'libro': libro})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = AutorForm()
    return render(request, 'libros/crear_autor.html', {'form': form})

def consulta_libros(request):
    consulta = "SELECT * FROM libros_libro"
    libros = ejecutar_consulta_row(consulta)
    return render(request, 'libros/consulta_libro.html', {'libros': libros})
