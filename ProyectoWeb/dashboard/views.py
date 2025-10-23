from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from pedidos.models import Pedido

# Helper function to check if user is staff
def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
def dashboard_home(request):
    pedidos = Pedido.objects.all().order_by('-created_at')
    return render(request, 'dashboard/dashboard.html', {'pedidos': pedidos})

@user_passes_test(is_staff)
def order_detail(request, order_id):
    pedido = Pedido.objects.get(id=order_id)
    return render(request, 'dashboard/order_detail.html', {'pedido': pedido})