from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Joueur

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the App1 index.")

def liste_joueurs(request):
    # Récupérer tous les joueurs avec leurs rôles et postes
    joueurs = Joueur.objects.select_related('refrole', 'refposte')  # Optimisation pour inclure les relations
    return render(request, 'listeJoueur.html', {'joueurs': joueurs})

def creer_compte(request):
    return render(request, 'creercompte.html')

def connexion(request):
    return render(request, 'connexion2.html')

def accueil(request):
    return render(request, 'accueil2.html')

def joueur(request):
    return render(request, 'joueur.html')

def tactique(request):
    return render(request, 'tactique.html')