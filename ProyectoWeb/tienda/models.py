from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image

# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaProd"
        verbose_name_plural="categoriasProd"

    def __str__(self):
        return self.nombre

from PIL import Image

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField(blank=True, null=True)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio=models.FloatField()
    stock=models.PositiveIntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagen:
            img = Image.open(self.imagen.path)

            # Redimensionar si es más grande que el tamaño objetivo
            output_size = (800, 800)
            if img.height > output_size[0] or img.width > output_size[1]:
                img.thumbnail(output_size)
                img.save(self.imagen.path, optimize=True)

    @property
    def disponibilidad(self):
        return self.stock > 0

class Resena(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('producto', 'user')
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"

    def __str__(self):
        return f'{self.user.username} - {self.producto.nombre}'

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"