from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Aluno, Prof
from hashlib import sha256

# Create your views here.

########## ALUNO ##########

def login(request):
    if request.session.get('aluno'):
        return redirect('/livro/home')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    turma = request.POST.get('turma')
    ra = request.POST.get('ra')
    senha = request.POST.get('senha')

    aluno = Aluno.objects.filter(turma = turma).filter(ra = ra)

    if len(nome.strip()) == 0 or len(turma.strip()) == 0 or len(ra.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')
    
    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if len(aluno) > 0:
        return redirect('/auth/cadastro/?status=3')
    
    try:
        senha = sha256(senha.encode()).hexdigest()
        aluno = Aluno(nome = nome,
                      turma = turma,
                      ra = ra,
                      senha = senha)
        aluno.save()

        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')

def validar_login(request):
    nome = request.POST.get('nome')
    turma = request.POST.get('turma')
    ra = request.POST.get('ra')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    aluno = Aluno.objects.filter(nome = nome).filter(turma = turma).filter(ra = ra).filter(senha = senha)

    if len(aluno) == 0:
        return redirect('/auth/login/?status=1')
    elif len(aluno) > 0:
        request.session['aluno'] = aluno[0].id
        return redirect('/livro/home')

def sair(request):
    request.session.flush()
    return redirect('/auth/login')


########## PROF ##########

def login_admin(request):
    if request.session.get('prof'):
        return redirect('/livro/home_admin')
    status = request.GET.get('status')
    return render(request, 'login_admin.html', {'status': status})

def cadastro_admin(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_admin.html', {'status': status})

def valida_cadastro_admin(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')

    prof = Prof.objects.filter(nome = nome)

    if len(nome.strip()) == 0:
        return redirect('/auth/cadastro_admin/?status=1')
    
    if len(senha) < 8:
        return redirect('/auth/cadastro_admin/?status=2')

    if len(prof) > 0:
        return redirect('/auth/cadastro_admin/?status=3')
    
    try:
        senha = sha256(senha.encode()).hexdigest()
        prof = Prof(nome = nome,
                    senha = senha)
        prof.save()

        return redirect('/auth/cadastro_admin/?status=0')
    except:
        return redirect('/auth/cadastro_admin/?status=4')

def validar_login_admin(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    prof = Prof.objects.filter(nome = nome).filter(senha = senha)

    if len(prof) == 0:
        return redirect('/auth/login_admin/?status=1')
    elif len(prof) > 0:
        request.session['prof'] = prof[0].id
        return redirect('/livro/home_admin')

def sair_admin(request):
    request.session.flush()
    return redirect('/auth/login_admin')
