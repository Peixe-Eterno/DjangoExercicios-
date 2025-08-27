from django.db import models

# Create your models here.
class Medico(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField(auto_now=False, auto_now_add=False)
    crm = models.CharField(max_length=10)
    especialidade = models.ForeignKey('Especialidade', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome