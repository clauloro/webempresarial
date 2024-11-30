from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model): #Relación de muchos a muchos, seleccionar una o varias categorías -  Relación ManyToMany
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    published = models.DateTimeField(default=now, verbose_name="Fecha de publicación")
    image = models.ImageField(upload_to="blog", null=True, blank=True, verbose_name="Imagen")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor") # Si se borra el usuario, se borran todas sus entradas: CASCADE - Relación ForeignKey
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
    def __str__(self):
        return self.title

