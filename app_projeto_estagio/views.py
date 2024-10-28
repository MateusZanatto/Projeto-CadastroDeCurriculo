from django.shortcuts import render, redirect
from .models import Curriculos
from .models import usuario
from django.contrib import messages

def cadastro(request):
    return render(request, 'curriculos/cadastro.html')

def curriculos(request):
    novo_curriculo = Curriculos()
    novo_curriculo.nome = request.POST.get('nome')
    novo_curriculo.idade = request.POST.get('idade')
    novo_curriculo.data_nascimento = request.POST.get('nascimento')
    novo_curriculo.email = request.POST.get('email')
    novo_curriculo.telefone = request.POST.get('telefone')
    novo_curriculo.endereco = request.POST.get('endereco')
    novo_curriculo.cargo = request.POST.get('cargo')
    novo_curriculo.empresa = request.POST.get('empresa')
    novo_curriculo.inicio = request.POST.get('inicio')
    novo_curriculo.termino = request.POST.get('termino')
    novo_curriculo.descricao = request.POST.get('descricao')
    novo_curriculo.instituicao = request.POST.get('instituicao')
    novo_curriculo.curso = request.POST.get('curso')
    novo_curriculo.periodo = request.POST.get('periodo')
    novo_curriculo.save()

    return redirect('cadastrado')

def lista(request):
    curriculos = {
        'curriculos': Curriculos.objects.all()
    }
    return render(request, 'curriculos/lista.html', curriculos)

def show(request, id, podeEditar = None):
    curriculo = Curriculos.objects.filter(id=id).first()  
    return render(request, 'curriculos/editar.html', {'curriculo': curriculo, 'podeEditar': podeEditar})

def editar(request,id, podeEditar = True,):
        
        curriculo = Curriculos.objects.filter(id=id).first()
    

        curriculo.nome = request.POST.get('nome')
        curriculo.idade = request.POST.get('idade')
        curriculo.data_nascimento = request.POST.get('nascimento')
        curriculo.email = request.POST.get('email')
        curriculo.telefone = request.POST.get('telefone')
        curriculo.endereco = request.POST.get('endereco')
        curriculo.cargo = request.POST.get('cargo')
        curriculo.empresa = request.POST.get('empresa')
        curriculo.inicio = request.POST.get('inicio')
        curriculo.termino = request.POST.get('termino')
        curriculo.descricao = request.POST.get('descricao')
        curriculo.instituicao = request.POST.get('instituicao')
        curriculo.curso = request.POST.get('curso')
        curriculo.periodo = request.POST.get('periodo')
        curriculo.save()

        return redirect('listar')
    
def deletar(request, id):
     curriculo = Curriculos.objects.filter(id=id).first()
     curriculo.delete()

     return redirect('listar')

def cadastrado(request):
    return render(request, 'curriculos/cadastrado.html')

def login_admin(request):
    if request.method == 'POST':
        
        usuario_db = request.POST.get('usuario')
        senha_db = request.POST.get('senha')
        
        try:
            usuario_obj = usuario.objects.get(usuario=usuario_db)
   
            if usuario_obj.senha == senha_db:
                return redirect('listar')  
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
                return redirect('login') 

        except usuario.DoesNotExist:
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('login')  
 
    return render(request, 'curriculos/login.html')

def login(request):
    return render(request, 'curriculos/login.html')