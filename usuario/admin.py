from django.contrib import admin
from .models import Usuario, Agendamento

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'email')
    search_fields = ('nome_completo', 'email')

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_nome_completo', 'get_email', 'telefone', 'tipo_visitante', 'instituicao', 'data', 'horario')
    search_fields = ('usuario__nome_completo', 'usuario__email', 'instituicao')
    list_filter = ('tipo_visitante', 'data')

    def get_nome_completo(self, obj):
        return obj.usuario.nome_completo
    get_nome_completo.short_description = 'Nome Completo'
    get_nome_completo.admin_order_field = 'usuario__nome_completo'

    def get_email(self, obj):
        return obj.usuario.email
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'usuario__email'

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)

