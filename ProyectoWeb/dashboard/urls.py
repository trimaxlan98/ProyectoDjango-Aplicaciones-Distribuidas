from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('pedido/<int:order_id>/', views.order_detail, name='dashboard_order_detail'),
]
