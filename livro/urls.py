from django.urls import path
from . import views

urlpatterns = [
    # Para Todos #
    path('', views.inicio, name = 'inicio'),
    path('sala', views.sala),
    # ALUNO #
    path('home/', views.home, name = 'home'),
    path('sala_de_leitura/', views.sala_de_leitura, name = 'sala_de_leitura'),
    path('ver_livro/<int:id>', views.ver_livro, name = 'ver_livro'),
    path('devolver_livro/<int:id>', views.devolver_livro, name = 'devolver_livro'),
    # PROF #
    path('home_admin/', views.home_admin, name='home_admin'),
    path('cadastrar_livro/', views.cadastrar_livro, name='cadastrar_livro'),
    path('tabela_1/', views.tabela1, name='tabela_1'),
    path('tabela_2/', views.tabela2, name='tabela_2'),
    path('tabela_3/', views.tabela3, name='tabela_3'),
    path('sala_de_leitura_admin/', views.sala_de_leitura_admin, name='sala_de_leitura_admin'),
    path('ver_livro_admin/<int:id>', views.ver_livro_admin, name='ver_livro_admin'),
    path('emprestar_livro/<int:id>', views.emprestar_livro, name='emprestar_livro'),
    path('devolver_livro_admin/<int:id>', views.devolver_livro_admin, name='devolver_livro_admin')
]
