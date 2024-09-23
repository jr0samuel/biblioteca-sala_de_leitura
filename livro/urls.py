from django.urls import path
from . import views

urlpatterns = [
    # Para Todos #
    path('', views.inicio, name='inicio'),
    path('sala', views.sala),
    # ALUNO #
    # path('home/', views.home, name = 'home'),
    # path('sala_de_leitura/', views.sala_de_leitura, name = 'sala_de_leitura'),
    # path('ver_livro/<int:id>', views.ver_livro, name = 'ver_livro'),
    # path('devolver_livro/<int:id>', views.devolver_livro, name='devolver_livro'),
    # PROF #
    # path('home_admin/', views.home_admin, name = 'home_admin'),
    # path('sala_de_leitura_admin/', views.sala_de_leitura_admin, name = 'sala_de_leitura_admin'),
    # path('tabela1', views.tabela1, name = 'tabela1'),
    # path('tabela2', views.tabela2, name = 'tabela2'),
    # path('tabela3', views.tabela3, name = 'tabela3'),
    # path('ver_livro_admin/<int:id>', views.ver_livro_admin, name = 'ver_livro_admin'),
    # path('cadastrar_livro/', views.cadastrar_livro, name='cadastrar_livro')
]