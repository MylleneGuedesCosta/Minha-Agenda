from django import forms
from .models import Event, Coment, Cadastro

class EventForm(forms.ModelForm):
    """Formulário utilizado para a inserção de novos eventos."""
    class Meta:
        model = Event
        fields = ['date', 'event', 'priority',]

class CommentForm(forms.ModelForm):
    """Formulário usado para a inserção de comentários em um evento."""
    class Meta:
        model = Coment
        fields = ['text', 'author', 'email', 'event']

class CadastroForm(forms.ModelForm):
    """Formulário usado para a inserção de comentários em um evento."""
    class Meta:
        model = Cadastro
        fields = ['name', 'cidade', 'pais', 'cep', 'idade', 'sexo', 'etnia']