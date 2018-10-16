from django.db import models
from django.utils import timezone
from libgravatar import Gravatar


class Event(models.Model):
    priorities_list = (
        ('0', 'Sem prioridade'),
        ('1', 'Normal'),
        ('2', 'Urgente'),
        ('3', 'Muito Urgente'),
        ('4', 'Ultra Mrga Hiper Urgente')
    )

    date = models.DateField()
    event = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=priorities_list)


class Meta:
    ordering = ('-date''-priority''event')


    def number_of_comments(self):
        return self.comment_event.count()


    def __str__(self):
        return self.event


class Coment(models.Model):
    """Comentários efetuados em um determinado evento."""
    author = models.CharField(max_length=80)
    email = models.EmailField()
    text = models.CharField(max_length=160)
    commented = models.DateTimeField(default=timezone.now)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comment_event')

    """Retorna a partir do endereço de email, um avatar configurado no Gravatar"""


    def avatar(self):
        g = Gravatar(self.email)
        return g.get_image(default='identicon')


def __str__(self):
    return "{} comentou em {:%c}".format(self.author, self.commented)


class Cadastro(models.Model):
    sexo_list = (
        ('0', 'Masculino'),
        ('1', 'Feminino'),
        ('2', 'Outro'),
    )

    etnia_list = (
        ('0', 'Albino'),
        ('1', 'Branco'),
        ('2', 'Pardo'),
        ('3', 'Negro'),
    )

    name = models.CharField(max_length=80)
    cidade = models.CharField(max_length=80)
    pais = models.CharField(max_length=80)
    cep = models.CharField(max_length=80)
    idade = models.CharField(max_length=80)

    sexo = models.CharField(max_length=1, choices=sexo_list)
    etnia = models.CharField(max_length=1, choices=etnia_list)

    def __str__(self):
        return self.name
