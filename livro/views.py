from django.shortcuts import render, redirect
from django.http import HttpResponse
from alunos.models import Aluno, Prof
from .models import Livros
from .forms import CadastroLivro
from datetime import date, datetime
from django.db.models import F

# Create your views here.

########## PARA TODOS ##########

def inicio(request):
    return render(request, 'inicio.html', {})
##########
def sala(request):
    return HttpResponse("Sala Ambiente de Leitura -- Mundo Mário da Leitura")
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
    livro_devolver.data_de_empréstimo = None
    livro_devolver.data_de_devolução = None
    livro_devolver.save()
    livro_devolver.refresh_from_db()
    return redirect('/livro/home/')

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
            data_atual = date.today
            return render(request, 'ver_livro_admin.html', {'livro': livro,
                                                            'id_livro': id,
                                                            'prof_logada': request.session.get('prof'),
                                                            'prof': prof,
                                                            'alunos': alunos,
                                                            'data_atual': data_atual})
        else:
            return HttpResponse('Esse livro não é seu')
    return redirect('/auth/login_admin/?status=2')

def emprestar_livro(request):# aluno_id
    # aluno_id = Aluno.objects.get(id=aluno_id)
    livro_id = request.POST.get('livro_id')
    data_emprestimo = request.POST.get('data_emprestimo')
    data_devolucao = request.POST.get('data_devolucao')
    # aluno = request.POST.get('aluno')

    livro_emprestar = Livros.objects.get(id = livro_id)
    if livro_emprestar.prof.id == request.session['prof']:
        livro_emprestar.quantidade = F('quantidade') - 1
        livro_emprestar.data_de_empréstimo = data_emprestimo
        livro_emprestar.data_de_devolução = data_devolucao
        # livro_emprestar.aluno = aluno
        # livro_emprestar.aluno = aluno_id
        livro_emprestar.save()
        livro_emprestar.refresh_from_db()
        return redirect(f'/livro/ver_livro_admin/{livro_id}')
    else:
        return redirect('/livro/ver_livro_admin/?livro_não_emprestado')

def devolver_livro_admin(request, id):
    livro_devolver_admin = Livros.objects.get(id = id)
    livro_devolver_admin.quantidade = F('quantidade') + 1
    livro_devolver_admin.aluno = None
    livro_devolver_admin.data_de_empréstimo = None
    livro_devolver_admin.data_de_devolução = None
    livro_devolver_admin.save()
    livro_devolver_admin.refresh_from_db()
    return redirect(f'/livro/ver_livro_admin/{id}')

def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/livro/home_admin/?status=0')
        else:
            return redirect('/livro/home_admin/?não_cadastrou')
