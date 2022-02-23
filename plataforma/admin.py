from django.contrib import admin
from .models import Imovei,Cidade,Imagem
# Register your models here.

@admin.register(Imovei)
class ImoveiAdmin(admin.ModelAdmin):
    list_display = ('rua', 'valor', 'tamanho', 'cidade', 'tipo')
    list_editable = ('valor', 'tipo')
    list_filter = ('cidade', 'tipo')

admin.site.register(Imagem)
admin.site.register(Cidade)
