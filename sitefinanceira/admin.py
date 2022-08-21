from django.contrib import admin
from .models import Beneficios
from .models import Recursos
from .models import Precos
from .models import Index

# Register your models here.
class BeneficiosAdmin(admin.ModelAdmin):
    list_display = ('id','nome','preco')

class RecursosAdmin(admin.ModelAdmin):
        list_display = ('id','nome', 'proposta')

class PrecosAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'preco')

class IndexAdmin(admin.ModelAdmin):
    list_display = ('id','email')


admin.site.register(Beneficios, BeneficiosAdmin)
admin.site.register(Recursos, RecursosAdmin)
admin.site.register(Precos, PrecosAdmin)
admin.site.register(Index, IndexAdmin)