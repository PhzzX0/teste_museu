from django.db import models

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    senha = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome_completo  # Exibe o nome completo


class Agendamento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)  # Relacionamento com Usuario
    nome_completo = models.CharField(max_length=150)  
    email = models.EmailField(default='')  
    telefone = models.CharField(max_length=15, default='')  
    tipo_visitante = models.CharField(
        max_length=20,
        choices=[('individual', 'Individual'), ('grupo', 'Grupo de Amigos'), ('instituicao', 'Instituição')],
        default='individual',  
    )
    instituicao = models.CharField(max_length=255, blank=True, null=True)  
    quantidade_visitantes = models.PositiveIntegerField(default=1)  
    data = models.DateField()  
    horario = models.TimeField()  

    def __str__(self):
        return f"{self.nome_completo} - {self.data} {self.horario}"
