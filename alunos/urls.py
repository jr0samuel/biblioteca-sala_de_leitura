from django.urls import path
from . import views

urlpatterns = [
    # ALUNO #
    path('login/', views.login, name = 'login'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('valida_cadastro/', views.valida_cadastro, name = 'valida_cadastro'),
    path('validar_login/', views.validar_login, name = 'validar_login'),
    path('sair/', views.sair, name = 'sair'),
    # PROF #
    path('login_admin/', views.login_admin, name = 'login_admin'),
    path('cadastro_admin/', views.cadastro_admin, name = 'cadastro_admin'),
    path('valida_cadastro_admin/', views.valida_cadastro_admin, name = 'valida_cadastro_admin'),
    path('validar_login_admin/', views.validar_login_admin, name = 'validar_login_admin'),
    path('sair_admin/', views.sair_admin, name = 'sair_admin')
]