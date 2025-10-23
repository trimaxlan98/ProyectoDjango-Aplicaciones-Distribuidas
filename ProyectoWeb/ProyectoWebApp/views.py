from django.shortcuts import render
from tienda.models import Producto

# Create your views here.

def home(request):
    productos_destacados = Producto.objects.filter(disponibilidad=True).order_by('-created')[:4]
    return render(request, "ProyectoWebApp/home.html", {"productos_destacados": productos_destacados})