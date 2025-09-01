from django.urls import path
import medico.views as views

urlpatterns = [
    path('', views.showIndex, name='Index'),
    path('medico/', views.listMedicos, name='ListMedicos'),
    path('medico/<int:pk>/', views.delMedico, name='DelMedico'),
    path('medico/cadastro/', views.addMedico, name='AddMedico'),
    path('medico/edit/<int:pk>/', views.editMedico, name='EditMedico'),

    path('especialidades/', views.listEspecialidades, name='ListEspecialidades'),
    path('especialidades/<int:pk>/', views.delEspecialidade, name='DelEspecialidade'),
    path('especialidades/cadastro/', views.addEspecialidade, name='AddEspecialidade'),
    path('especialidades/edit/<int:pk>/', views.editEspecialidade, name='EditEspecialidade'),
]