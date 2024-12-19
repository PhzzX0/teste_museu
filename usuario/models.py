from django.db import models


class CadastroUsuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome_usuario = models.CharField(max_length=255, unique=True)
    email_usuario = models.CharField(max_length=255, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    senha_usuario = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.nome_usuario}'


class LoginUsuario(models.Model):
    id_login = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(CadastroUsuario, on_delete=models.PROTECT)
    nome_usuario = models.CharField(max_length=25)
    senha_usuario = models.CharField(max_length=15)
    data_login = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Sucesso', 'Sucesso'), ('Falha', 'Falha')])

    def __str__(self):
        return f'{self.nome_usuario} - {self.status} ({self.data_login})'
