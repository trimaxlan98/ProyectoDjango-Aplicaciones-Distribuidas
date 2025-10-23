from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from pedidos.models import LineaPedido, Pedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    # Descontar stock
    for linea in lineas_pedido:
        producto = linea.producto
        producto.stock -= linea.cantidad
        producto.save()

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email

    )

    messages.success(request, "El pedido se ha creado correctamente")

    return redirect('../tienda')

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario")
    })

    mensaje_texto=strip_tags(mensaje)
    from_email="cursos@pildorasinformaticas.es"
    #to=kwargs.get("emailusuario")
    to="programadorpython2020@gmail.com"
    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)

@login_required(login_url='logear')
def historial_pedidos(request):
    pedidos = Pedido.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "pedidos/historial.html", {"pedidos": pedidos})