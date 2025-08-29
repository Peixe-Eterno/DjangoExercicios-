from django.urls import path
from .views import views

urlpatterns = [
    path('medico/', views.listMedicos, name='ListMedicos'),
    path('medico/', views.delMedico, name='DelMedico'),
    path('medico/cadastro/', views.addMedico, name='AddMedico'),
    path('medico/edit/<int:id>/', views.editMedico, name='EditMedico'),

    path('especialidades/', views.listEspecialidades, name='ListEspecialidades'),
    path('especialidades/', views.delEspecialidade, name='DelEspecialidade'),
    path('especialidades/cadastro/', views.addEspecialidade, name='AddEspecialidade'),
    path('especialidades/edit/<int:id>/', views.editEspecialidade, name='EditEspecialidade'),
]