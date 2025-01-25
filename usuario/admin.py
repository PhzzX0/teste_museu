from django.contrib import admin
from .models import Usuario, Agendamento

# Personalizando a interface de administração para Usuario
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email')
    search_fields = ('nome', 'sobrenome', 'email')

# Personalizando a interface de administração para AgendamentoVisita
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'tipo_visitante', 'instituicao', 'data', 'horario')
    search_fields = ('nome', 'sobrenome', 'email', 'instituicao')
    list_filter = ('tipo_visitante', 'data', 'horario')

# Registrando os modelos no admin
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)

