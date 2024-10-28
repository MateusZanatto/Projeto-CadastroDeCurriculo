
from django.urls import path
from app_projeto_estagio import views
from django.contrib import admin
    

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('login/', views.login_admin, name='login_admin'),
    path('',views.cadastro, name='cadastro' ),
    path('login/admin', views.login,name='login'),
    path('curriculos/', views.curriculos,name='listagem_curriculos'),
    path('curriculos/lista/', views.lista,name='listar'),
    path('curriculos/cadastrado/', views.cadastrado,name='cadastrado'),
    path('curriculos/show/<int:id>', views.show, name='show'),
    path('curriculos/editar/<int:id>', views.editar, name='editar'),
    path('curriculos/deletar/<int:id>', views.deletar, name='deletar'),
   
]
