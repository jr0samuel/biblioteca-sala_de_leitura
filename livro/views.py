from django.shortcuts import render, redirect, get_object_or_404
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
        status = request.GET.get('status')

        return render(request, 'home_admin.html', {'form': form,
                                                   'prof': prof,
                                                   'status': status})
    else:
        return redirect('/auth/login_admin/?status=2')

def ver_livro_admin(request, id):
    if request.session.get('prof'):
        livro = Livros.objects.get(id = id)
        if request.session.get('prof') == livro.prof.id:
            prof = Prof.objects.get(id = request.session['prof'])
            alunos = Aluno.objects.all()
            data_atual = date.today
            status = request.GET.get('status')
            return render(request, 'ver_livro_admin.html', {'livro': livro,
                                                            'id_livro': id,
                                                            'prof_logada': request.session.get('prof'),
                                                            'prof': prof,
                                                            'alunos': alunos,
                                                            'data_atual': data_atual,
                                                            'status': status})
        else:
            return HttpResponse('Esse livro não é seu')
    return redirect('/auth/login_admin/?status=2')

def emprestar_livro(request):
    livro_id = request.POST.get('livro_id')
    data_emprestimo = request.POST.get('data_emprestimo')
    data_devolucao = request.POST.get('data_devolucao')
    aluno_id = request.POST.get('aluno')

    livro_emprestar = Livros.objects.get(id = livro_id)
    if livro_emprestar.prof.id == request.session['prof']:
        livro_emprestar.quantidade = F('quantidade') - 1
        livro_emprestar.data_de_empréstimo = data_emprestimo
        livro_emprestar.data_de_devolução = data_devolucao

        try:
            aluno_instance = Aluno.objects.get(id=aluno_id)
            livro_emprestar.aluno = aluno_instance
        except Aluno.DoesNotExist:
            return redirect(f'/livro/ver_livro_admin/{livro_id}/?aluno_nao_encontrado/?status=4')

        livro_emprestar.save()
        livro_emprestar.refresh_from_db()
        return redirect(f'/livro/ver_livro_admin/{livro_id}/?livro_emprestado/?status=1')
    else:
        return redirect(f'/livro/ver_livro_admin/{livro_id}/?livro_nao_emprestado/?status=2')

def devolver_livro_admin(request, id):
    livro_devolver_admin = Livros.objects.get(id = id)
    livro_devolver_admin.quantidade = 1
    livro_devolver_admin.aluno = None
    livro_devolver_admin.data_de_empréstimo = None
    livro_devolver_admin.data_de_devolução = None
    livro_devolver_admin.save()
    livro_devolver_admin.refresh_from_db()
    return redirect(f'/livro/ver_livro_admin/{id}/?livro_devolvido/?status=3')

def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/livro/home_admin/?livro_cadastrado/?status=0')
        else:
            return redirect('/livro/home_admin/?livro_nao_cadastrado/?status=1')

def alunos_cadastrados(request):
    prof = Prof.objects.get(id = request.session['prof'])
    alunos = Aluno.objects.all()
    status = request.GET.get('status')
    return render(request, 'alunos_cadastrados.html', {'alunos': alunos,
                                                       'prof': prof,
                                                       'status': status})

def aluno_excluir(request, aluno_id):
    prof = Prof.objects.get(id = request.session['prof'])
    aluno = get_object_or_404(Aluno, id=aluno_id)
    if request.method == "POST":
        aluno.delete()
        return redirect('/livro/alunos_cadastrados/?aluno_descadastrado/?status=0')
    return render(request, 'aluno_excluir.html', {'aluno': aluno,
                                                  'prof': prof})
