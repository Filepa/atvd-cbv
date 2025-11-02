from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control' }),
            'descricao': forms.Textarea(attrs={'class': 'form-control' }),
            'data_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'data_fim': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'secao': forms.TextInput(attrs={'class': 'form-control' }),
        }