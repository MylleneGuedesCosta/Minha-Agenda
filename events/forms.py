from django import forms
from .models import Event, number_of_comments
class EventForm(forms.ModelForm):
    """Formulário ultilizado para criação de novos eventos"""
    class Meta:
        model = Event
        fields = ['date', 'event', 'priority']

class CommentForm(forms.ModelForm):
    """Formulário ultilizado para criação de comentários"""
    class Meta:
        model = Comment
        fields = ['text', 'author', 'email', 'event']