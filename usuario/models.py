from django.db import models

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    senha = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome_completo  # Exibe o nome completo

class Agendamento(models.Model):
    nome_completo = models.CharField(max_length=150)  # Nome do visitante
    email = models.EmailField(default='')  # E-mail do visitante
    telefone = models.CharField(max_length=15, default='')  # Telefone de contato
    tipo_visitante = models.CharField(
        max_length=20,
        choices=[('individual', 'Individual'), ('grupo', 'Grupo de Amigos'), ('instituicao', 'Instituição')],
        default='individual',  # Define um valor padrão
    )
    instituicao = models.CharField(max_length=255, blank=True, null=True)  # Nome da instituição (opcional)
    quantidade_visitantes = models.PositiveIntegerField(default=1)  # Quantidade de visitantes
    data = models.DateField()  # Data da visita
    horario = models.TimeField()  # Horário da visita

    def __str__(self):
        return f"{self.nome_completo} - {self.data} {self.horario}"


