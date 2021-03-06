from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Cadastro(models.Model):
    priorities_list = (
        ('0', 'Sem prioridade'),
        ('1', 'Normal'),
        ('2', 'Urgente'),
        ('3', 'Muito Urgente'),
        ('4', 'Ultra Mrga Hiper Urgente')
    )
    priorities_list = (
        ('0' , 'Sem prioridade'),
        ('1' , 'Normal'),
        ('2','Urgente'),
        ('3', 'Muito Urgente'),
        ('4', 'Ultra Mrga Hiper Urgente')
    )
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    sexo = models.CharField(max_length=1, choices=priorities_list)
    etnia = models.CharField(max_length=1, choices=priorities_list)

    def __str__(self):
        return self.nome