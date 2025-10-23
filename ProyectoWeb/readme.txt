Proyecto Tienda Online en Django

== Descripción ==
Esta es una aplicación web de comercio electrónico desarrollada con Django. El objetivo es simular las funcionalidades y la experiencia de usuario de una tienda online profesional como Amazon o Mercado Libre.

== Características Principales ==
- Catálogo de productos con filtrado por categorías.
- Buscador de productos por nombre y descripción.
- Páginas de detalle de producto.
- Sistema de reseñas y calificaciones por estrellas.
- Carrito de compras persistente (basado en sesión).
- Proceso de checkout simulado con creación de pedidos.
- Gestión de inventario (stock numérico que se descuenta con la compra).
- Panel de "Mi Cuenta" para usuarios registrados.
- Historial de pedidos para cada usuario.
- Panel de Administración básico para ver los pedidos de la tienda.
- Optimización automática de imágenes al subirlas.
- Notificaciones de confirmación de pedido por email (simuladas en consola).

== Instrucciones de Instalación y Ejecución ==

1. **Clonar el Repositorio:**
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_DIRECTORIO>

2. **Crear y Activar un Entorno Virtual:**
   python -m venv venv
   source venv/bin/activate   # En Windows: venv\Scripts\activate

3. **Instalar las Dependencias:**
   pip install -r requirements.txt

4. **Aplicar las Migraciones:**
   python manage.py migrate

5. **Crear un Superusuario (Administrador):**
   (Necesario para acceder al panel de Django y al Dashboard)
   python manage.py createsuperuser

6. **Ejecutar el Servidor de Desarrollo:**
   python manage.py runserver

   La aplicación estará disponible en http://127.0.0.1:8000/
