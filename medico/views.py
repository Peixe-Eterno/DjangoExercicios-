from django.shortcuts import render

from .models import Medico, Especialidade
from .forms import AddForm

# Create your views here.

def showIndex(request):
    return render(request, 'medico/background.html',)

def listMedicos(request):
      
        return render(request, 'medico/listmedico.html', {'list': Medico.objects.all()})

def delMedico(request, pk):
    
    Medico.objects.filter(id=pk).delete()
    return render(request, 'medico/listmedico.html', {'list': Medico.objects.all()})
    

def addMedico(request):
    if request.method == 'POST':
        django_form = AddForm(request.POST)
        if django_form.is_valid():

            novo_medico_nome = django_form.data.get('nome'),
            novo_medico_endereco = django_form.data.get('endereco'),
            novo_medico_telefone = django_form.data.get('telefone'),
            novo_medico_email = django_form.data.get('email'),
            novo_medico_data_nascimento = django_form.data.get('data_nascimento'),
            novo_medico_crm = django_form.data.get('crm'),
            novo_medico_especialidade = django_form.data.get('especialidade'),

            Medico.objects.create(
                nome = novo_medico_nome,
                endereco = novo_medico_endereco,
                telefone = novo_medico_telefone,
                email = novo_medico_email,
                data_nascimento = novo_medico_data_nascimento,
                crm = novo_medico_crm,
                especialidade = novo_medico_especialidade
            )

            return render(request, 'medico/listmedico.html', {'list': Medico.objects.all()})

        else:
            return render(request, 'medico/cadmedico.html',)
    else:
        return render(request, 'medico/cadmedico.html',)

def editMedico(request):
    pass


def listEspecialidades(request):

    return render(request, 'medico/listespecialideda.html', {'list': Especialidade.objects.all()})

def delEspecialidade(request, pk):
    
    Especialidade.objects.filter(id=pk).delete()
    return render(request, 'medico/listespecialideda.html', {'list': Especialidade.objects.all()})
    

def addEspecialidade(request):
    if request.method == 'POST':
        django_form = AddForm(request.POST)
        if django_form.is_valid():

            novo_especialidade_nome = django_form.data.get('especialidade'),
            novo_especialidade_descricao = django_form.data.get('descricao'),

            Especialidade.objects.create(
                nome = novo_especialidade_nome,
                descricao = novo_especialidade_descricao
            )

            return render(request, 'medico/listespecialideda.html', {'list': Especialidade.objects.all()})
        else:
            return render(request, 'medico/cadespecialidade.html',)
    else:
        return render(request, 'medico/cadespecialidade.html',)

def editEspecialidade(request):
    pass
