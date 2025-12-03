from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ClienteSignUpForm, OficinaSignUpForm, ProblemaForm, OficinaPerfilForm
from .models import Problema, User, PerfilOficina

def home(request):
    if request.user.is_authenticated:
        if request.user.is_cliente:
            return redirect('dashboard_cliente')
        elif request.user.is_oficina:
            return redirect('dashboard_oficina')
    return render(request, 'core/home.html')


def signup_cliente(request):
    if request.method == 'POST':
        form = ClienteSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard_cliente')
    else:
        form = ClienteSignUpForm()
    return render(request, 'registration/signup.html', {'form': form, 'tipo': 'Cliente'})

def signup_oficina(request):
    if request.method == 'POST':
        form = OficinaSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard_oficina')
    else:
        form = OficinaSignUpForm()
    return render(request, 'registration/signup.html', {'form': form, 'tipo': 'Oficina'})

@login_required
def dashboard_cliente(request):
    problemas = Problema.objects.filter(cliente=request.user).order_by('-data_criacao')
    if request.method == 'POST':
        form = ProblemaForm(request.POST, request.FILES)
        if form.is_valid():
            problema = form.save(commit=False)
            problema.cliente = request.user
            problema.save()
            return redirect('dashboard_cliente')
    else:
        form = ProblemaForm()
    return render(request, 'core/dashboard_cliente.html', {'problemas': problemas, 'form': form})

# Views para Oficina (Simplificadas para o exemplo)
# Nota: Num cenário real, você criaria um registro separado para oficina
@login_required
def dashboard_oficina(request):
    # Listar problemas em aberto (sem oficina atribuída)
    problemas_abertos = Problema.objects.filter(status='ABERTO')
    meus_servicos = Problema.objects.filter(oficina=request.user)
    return render(request, 'core/dashboard_oficina.html', {
        'problemas_abertos': problemas_abertos,
        'meus_servicos': meus_servicos
    })

@login_required
def pegar_servico(request, pk):
    problema = get_object_or_404(Problema, pk=pk)
    if not problema.oficina and request.user.is_oficina:
        problema.oficina = request.user
        problema.status = 'ANDAMENTO'
        problema.save()
    return redirect('dashboard_oficina')

@login_required
def concluir_servico(request, pk):
    problema = get_object_or_404(Problema, pk=pk)
    if problema.oficina == request.user:
        problema.status = 'CONCLUIDO'
        problema.save()
    return redirect('dashboard_oficina')