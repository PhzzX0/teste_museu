from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=150)  # Limite de caracteres para o nome
    sobrenome = models.CharField(max_length=150)  # Limite de caracteres para o sobrenome
    email = models.EmailField(unique=True, default='@example.com')  # Garante que os e-mails sejam únicos
    senha = models.CharField(max_length=128)  # Para senhas seguras

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Agendamento(models.Model):
    nome = models.CharField(max_length=150)  # Nome do visitante
    sobrenome = models.CharField(max_length=150)  # Sobrenome do visitante
    email = models.EmailField(default='visitante@example.com')  # E-mail do visitante com um padrão
    telefone = models.CharField(max_length=15, default='(00) 00000-0000')  # Telefone de contato
    tipo_visitante = models.CharField(
        max_length=20,
        choices=[('individual', 'Individual'), ('instituicao', 'Instituição')],
        default='individual',  # Define um valor padrão
    )
    instituicao = models.CharField(max_length=255, blank=True, null=True)  # Nome da instituição (opcional)
    data = models.DateField()  # Data da visita
    horario = models.TimeField()  # Horário da visita

    def __str__(self):
        return f"{self.nome} {self.sobrenome} - {self.data} {self.horario}"
