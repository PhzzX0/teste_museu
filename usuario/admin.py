from django.contrib import admin
from .models import Usuario, Agendamento

# Personalizando a interface de administração para Usuario
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'email')  # Mostra o nome completo e o e-mail
    search_fields = ('nome_completo', 'email')  # Permite a busca por nome completo e e-mail

# Personalizando a interface de administração para Agendamento
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'email', 'telefone', 'tipo_visitante', 'instituicao', 'data', 'horario')
    search_fields = ('nome_completo', 'email', 'instituicao')  # Pesquisa por nome, e-mail e instituição
    list_filter = ('tipo_visitante', 'data')  # Filtros por tipo de visitante e data

# Registrando os modelos no admin
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)


