from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path ('listar', views.lista_residentes, name='lista_residentes'),
    path ('registroResidente/', views.registroResidente, name='registroResidente'),
    path('registrarResidente/', views.registrarResidente, name='registrarResidente'),
    path('login/', views.login, name='login'),
    path('agregarObservaciones/<int:id>', views.agregarObservaciones, name='agregarObservaciones'),
    path('editarResidente/', views.editarResidente, name='editarResidente'),
    path('eliminarResidente/<int:id>', views.eliminarResidente, name='eliminarResidente'),
    path('historialAportes/', views.historialAportes, name='historialAportes'),
    path('historialAportes/vistaAportador/<int:id>',views.vistaAportador, name='vistaAportador'),
    
]
