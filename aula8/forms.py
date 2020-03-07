from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    model = Pet
    fields = '__all__'

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')

        if nome.upper() == 'PUTINHO':
            raise forms.ValidationError("Nome muito ofensivo")
            
        return nome