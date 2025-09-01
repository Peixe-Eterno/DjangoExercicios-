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

            medico_nome = django_form.data.get('nome'),
            medico_endereco = django_form.data.get('endereco'),
            medico_telefone = django_form.data.get('telefone'),
            medico_email = django_form.data.get('email'),
            medico_data_nascimento = django_form.data.get('data_nascimento'),
            medico_crm = django_form.data.get('crm'),
            medico_especialidade = django_form.data.get('especialidade'),

            Medico.objects.create(
                medico_nome,
                medico_endereco, 
                medico_telefone, 
                medico_email, 
                medico_data_nascimento, 
                medico_crm, 
                medico_especialidade
            )

            return render(request, 'medico/listmedico.html', {'list': Medico.objects.all()})

        else:
            return render(request, 'medico/cadmedico.html',)
    else:
        return render(request, 'background.html',)

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

            especialidade_nome = django_form.data.get('especialidade'),
            especialidade_descricao = django_form.data.get('descricao'),

            Especialidade.objects.create(
                especialidade_nome,
                especialidade_descricao
            )

            return render(request, 'medico/listespecialideda.html', {'list': Especialidade.objects.all()})
        else:
            return render(request, 'medico/cadespecialidade.html',)
    else:
        return render(request, 'background.html',)

def editEspecialidade(request):
    pass
