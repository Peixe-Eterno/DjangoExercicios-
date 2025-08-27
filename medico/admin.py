from django.contrib import admin
from .models import Especialidade, Medico

# Register your models here.

@admin.register(Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']
    list_filter = ['nome']
    list_editable = ['descricao']

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'telefone', 'email', 'data_nascimento', 'crm', 'especialidade']
    list_filter = ['especialidade', 'data_nascimento']
    list_editable = ['endereco', 'telefone', 'email']
    search_fields = ['nome', 'crm']