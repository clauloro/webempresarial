from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Service
class ServiceAdmin(admin.ModelAdmin):
 readonly_fields = ('created', 'updated')
admin.site.register(Service, ServiceAdmin)
