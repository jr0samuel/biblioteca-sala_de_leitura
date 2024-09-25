from django.shortcuts import render, redirect
from django.http import HttpResponse
from alunos.models import Aluno, Prof
from .models import Livros
from datetime import date, datetime
from .forms import CadastroLivro
from django.db.models import F

# Create your views here.

########## PARA TODOS ##########

def inicio(request):
    # return HttpResponse("Mundo Mário da Leitura")
    return redirect('inicio.html', {})# parece que pode ser com ou sem {}
##########
def sala(request):
    return HttpResponse("Sala de Leitura")
##########

########## ALUNO ##########

def home(request):
    if request.session.get('aluno'):
        aluno = Aluno.objects.get(id = request.session['aluno'])
        livros = Livros.objects.filter(aluno = aluno)
        data_atual = date.today
        return render(request, 'home.html', {'livros': livros,
                                             'aluno_logado': request.session.get('aluno'),
                                             'data_atual': data_atual,
                                             'aluno': aluno})
    else:
        return redirect('/auth/login/?status=2')

def ver_livro(request, id):
    if request.session.get('aluno'):
        livro = Livros.objects.get(id = id)
        data_atual = date.today
        if request.session.get('aluno') == livro.aluno.id:
            aluno = Aluno.objects.get(id = request.session['aluno'])
            return render(request, 'ver_livro.html', {'livro': livro,
                                                      'id_livro': id,
                                                      'aluno_logado': request.session.get('aluno'),
                                                      'data_atual': data_atual,
                                                      'aluno': aluno})
        else:
            return HttpResponse('Esse livro não é seu')
    return redirect('/auth/login/?status=2')

def devolver_livro(request, id):
    livro_devolver = Livros.objects.get(id = id)
    livro_devolver.quantidade = F('quantidade') + 1
    livro_devolver.aluno = None
    livro_devolver.data_emprestimo = None
    livro_devolver.data_devolucao = None
    livro_devolver.save()
    livro_devolver.refresh_from_db()
    return redirect('/livro/home/')
# ver esse redirect e o path vazio em biblioteca/urls

def sala_de_leitura(request):
        if request.session.get('aluno'):
            aluno = Aluno.objects.get(id = request.session['aluno'])
            livros = Livros.objects.all()

            return render(request, 'sala_de_leitura.html', {'livros': livros,
                                                            'aluno_logado': request.session.get('aluno'),
                                                            'aluno': aluno})

        else:
            livros = Livros.objects.all()
            return render(request, 'sala_de_leitura.html', {'livros': livros})

########## PROF ##########

def sala_de_leitura_admin(request):
        if request.session.get('prof'):
            prof = Prof.objects.get(id = request.session['prof'])
            livros = Livros.objects.all()

            return render(request, 'sala_de_leitura_admin.html', {'livros': livros,
                                                                  'prof_logada': request.session.get('prof'),
                                                                  'prof': prof})
        else:
            livros = Livros.objects.all()
            return render(request, 'sala_de_leitura_admin.html', {'livros': livros})

def home_admin(request):
    if request.session.get('prof'):
        prof = Prof.objects.get(id = request.session['prof'])
        form = CadastroLivro()

        return render(request, 'home_admin.html', {'form': form,
                                                   'prof': prof})
    else:
        return redirect('/auth/login_admin/?status=2')

def ver_livro_admin(request, id):
    if request.session.get('prof'):
        livro = Livros.objects.get(id = id)
        if request.session.get('prof') == livro.prof.id:
            prof = Prof.objects.get(id = request.session['prof'])
            alunos = Aluno.objects.all()
            return render(request, 'ver_livro_admin.html', {'livro': livro,
                                                            'id_livro': id,
                                                            'prof_logada': request.session.get('prof'),
                                                            'prof': prof,
                                                            'alunos': alunos})
        else:
            return HttpResponse('Esse livro não é seu')
    return redirect('/auth/login_admin/?status=2')

def emprestar_livro(request, id):
    livro_devolver = Livros.objects.get(id = id)
    livro_devolver.quantidade = F('quantidade') - 1
    livro_devolver.save()
    livro_devolver.refresh_from_db()
    return redirect('/livro/home_admin/')

def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/livro/home_admin/?status=0')
        else:
            return redirect('/livro/home_admin/?não_cadastrou')

def tabela1(request):
    if request.session.get('prof'):
        prof = Prof.objects.get(id = request.session['prof'])
        return render(request, 'tabela_1.html', {'prof': prof})
    else:
        return redirect('/auth/login_admin/?status=2')

def tabela2(request):
    if request.session.get('prof'):
        prof = Prof.objects.get(id = request.session['prof'])
        return render(request, 'tabela_2.html', {'prof': prof})
    else:
        return redirect('/auth/login_admin/?status=2')

def tabela3(request):
    if request.session.get('prof'):
        prof = Prof.objects.get(id = request.session['prof'])
        return render(request, 'tabela_3.html', {'prof': prof})
    else:
        return redirect('/auth/login_admin/?status=2')
