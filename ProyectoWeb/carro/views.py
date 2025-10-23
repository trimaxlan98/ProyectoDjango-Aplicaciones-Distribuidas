from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import Producto

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    agregado = carro.agregar(producto=producto)
    if agregado:
        messages.success(request, f"Se ha añadido {producto.nombre} al carro.")
    else:
        messages.error(request, f"No se pudo añadir {producto.nombre}. Stock insuficiente.")
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Tienda")

def limpiar_carro(request):

    carro = Carro(request)

    carro.limpiar_carro()

    return redirect("Tienda")



def ver_carro(request):

    return render(request, "carro/carro.html")
