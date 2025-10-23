from django.shortcuts import render, redirect
from .models import Producto, CategoriaProd, Resena
from .forms import ResenaForm
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def tienda(request):
    productos_list = Producto.objects.all()
    paginator = Paginator(productos_list, 6) # 6 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categorias = CategoriaProd.objects.all()
    return render(request, "tienda/tienda.html", {"page_obj": page_obj, "categorias": categorias})

def categoria(request, categoria_id):
    categoria = CategoriaProd.objects.get(id=categoria_id)
    productos_list = Producto.objects.filter(categorias=categoria)
    paginator = Paginator(productos_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categorias = CategoriaProd.objects.all()
    return render(request, "tienda/categoria.html", {'categoria': categoria, "page_obj": page_obj, "categorias": categorias})

from django.db.models import Q

def buscar(request):
    query = request.GET.get('q')
    productos_list = Producto.objects.filter(
        Q(nombre__icontains=query) | Q(descripcion__icontains=query)
    ).distinct() if query else Producto.objects.none()
    paginator = Paginator(productos_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categorias = CategoriaProd.objects.all()
    return render(request, 'tienda/tienda.html', {'page_obj': page_obj, 'categorias': categorias, 'query': query})

def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    reviews = Resena.objects.filter(producto=producto)
    related_products = Producto.objects.filter(categorias=producto.categorias).exclude(id=producto_id).order_by('?')[:4]

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('logear')
        
        form = ResenaForm(request.POST)
        if form.is_valid():
            if Resena.objects.filter(producto=producto, user=request.user).exists():
                pass
            else:
                review = form.save(commit=False)
                review.producto = producto
                review.user = request.user
                review.save()
                return redirect('detalle_producto', producto_id=producto.id)
    else:
        form = ResenaForm()

    return render(request, 'tienda/detalle_producto.html', {
        'producto': producto,
        'reviews': reviews,
        'form': form,
        'related_products': related_products
    })
