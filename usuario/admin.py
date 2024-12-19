from django.contrib import admin
from .models import CadastroUsuario, LoginUsuario

# Personalizando a interface de administração para CadastroUsuario
class CadastroUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nome_usuario', 'email_usuario', 'data_cadastro', 'senha_usuario')
    search_fields = ('id_usuario', 'nome_usuario', 'email_usuario')

# Personalizando a interface de administração para LoginUsuario
class LoginUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_login', 'nome_usuario', 'status', 'data_login')
    search_fields = ('nome_usuario', 'status')
    list_filter = ('status', 'data_login')

# Registrando os modelos no admin
admin.site.register(CadastroUsuario, CadastroUsuarioAdmin)
admin.site.register(LoginUsuario, LoginUsuarioAdmin)
