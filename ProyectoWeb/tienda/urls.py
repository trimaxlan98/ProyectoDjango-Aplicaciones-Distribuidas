from django.urls import path
from . import views


urlpatterns = [
    path('',views.tienda, name="Tienda"),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('buscar/', views.buscar, name='buscar'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]