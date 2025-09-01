from django import forms
from .models import Medico, Especialidade

class AddForm(forms.Form):
    
    class Meta:
        model = Medico
        fields = ('nome', 'endereco', 'telefone', 'email', 'data_nascimento', 'crm', 'especialidade',)

    class Meta:
        model = Especialidade
        fields = ('nome', 'descricao',)