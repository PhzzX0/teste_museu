from django.contrib import admin
from .models import Usuario, Agendamento

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'email')  # Agora usa 'id' gerado automaticamente
    search_fields = ('nome_completo', 'email')  

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nome_completo', 'email', 'telefone', 'tipo_visitante', 'instituicao', 'data', 'horario')
    search_fields = ('nome_completo', 'email', 'instituicao')  
    list_filter = ('tipo_visitante', 'data')  

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
