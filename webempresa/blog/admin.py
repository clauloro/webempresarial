from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories') # Muestra los campos en la lista de entradas.
    ordering = ('author', 'published') # Ordena las entradas por autor y fecha de publicación.
    search_fields = ('title','content','author__username', 'categories__name') # Campos por los que se puede buscar.
    date_hierarchy = 'published' # Jerarquía de fechas.
    list_filter = ('author__username','categories__name') # Filtros de búsqueda.
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)





