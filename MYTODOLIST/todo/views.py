from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Tache
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        username = request.POST.get('nom')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            messages.error(request, 'Nom ou mot de passe incorrect')
    return render(request, 'todolist/index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('nom')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Cet email est déjà utilisé.')
            return render(request, 'todolist/register.html')
            
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            login(request, user)
            return redirect('list')
        except Exception as e:
            messages.error(request, f'Erreur lors de la création du compte: {str(e)}')
    return render(request, 'todolist/register.html')

@login_required
def list(request):
    taches = Tache.objects.filter(user=request.user).order_by('-date_creation')
    
    if request.method == 'POST':
        tache_texte = request.POST.get('tache')
        date_limite = request.POST.get('date_limite')
        if tache_texte:
            tache = Tache.objects.create(
                tache=tache_texte,
                user=request.user,
                date_limite=date_limite if date_limite else None
            )
            return redirect('list')
    
    return render(request, 'todolist/list.html', {'taches': taches})

@login_required
def delete(request, tache_id):
    try:
        tache = Tache.objects.get(id=tache_id, user=request.user)
        tache.delete()
    except Tache.DoesNotExist:
        messages.error(request, "Cette tâche n'existe pas ou ne vous appartient pas.")
    return redirect('list')

@login_required
def modifier(request, tache_id):
    try:
        tache = Tache.objects.get(id=tache_id, user=request.user)
        if request.method == 'POST':
            tache_texte = request.POST.get('tache')
            tache_status = request.POST.get('statut')
            date_limite = request.POST.get('date_limite')
            
            if tache_texte:
                tache.tache = tache_texte
            if tache_status:
                tache.status = tache_status
            if date_limite:
                tache.date_limite = date_limite
                
            tache.save()
            return redirect('list')
            
    except Tache.DoesNotExist:
        messages.error(request, "Cette tâche n'existe pas ou ne vous appartient pas.")
        return redirect('list')
        
    return render(request, 'todolist/modifier_tache.html', {'tache': tache})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

