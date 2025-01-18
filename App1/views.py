from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from .models import Joueur, Poste, Role, Stats,Tactique, PositionJoueur,Equipe,Coach
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
import json
from django.shortcuts import get_object_or_404
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Coach
from .models import Joueur
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password, check_password

from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Hello, world. You're at the App1 index.")

def liste_joueurs(request):
    # Récupérer tous les joueurs avec leurs rôles et postes
    joueurs = Joueur.objects.select_related('refrole', 'refposte')  # Optimisation pour inclure les relations
    return render(request, 'listeJoueur.html', {'joueurs': joueurs})

def creer_compte(request):
    if request.method == "POST":
        # Récupérer les champs du formulaire
        username = request.POST.get("username", "").strip()
        nom = request.POST.get("nom", "").strip()
        prenom = request.POST.get("prenom", "").strip()
        age = request.POST.get("age", "").strip()
        password = request.POST.get("password", "").strip()

        # Validation des champs côté serveur
        errors = []
        if not username:
            errors.append("Le nom d'utilisateur est obligatoire.")
        if not nom:
            errors.append("Le champ 'Nom' est obligatoire.")
        if not prenom:
            errors.append("Le champ 'Prénom' est obligatoire.")
        if not age or not age.isdigit() or int(age) < 0:
            errors.append("L'âge doit être un nombre positif.")
        if not password or len(password) < 6:
            errors.append("Le mot de passe doit contenir au moins 6 caractères.")

        if errors:
            return render(request, "creercompte.html", {
                "errors": errors,
                "username": username,
                "nom": nom,
                "prenom": prenom,
                "age": age
            })

        # Vérifier si un utilisateur existe déjà avec ce username
        if Coach.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà utilisé.")
            return render(request, "creercompte.html", {
                "nom": nom,
                "prenom": prenom,
                "age": age
            })

        # Créer un coach dans la base de données
        coach = Coach.objects.create(
            username=username,
            nomcoach=nom,
            prenomcoach=prenom,
            agecoach=int(age),
            password=password
        )
        coach.set_password(password)  # Hachage du mot de passe
        coach.save()

        messages.success(request, "Votre compte a été créé avec succès !")
        return redirect("accueil")

    return render(request, "creercompte.html")

def logout_view(request):
    logout(request)  # Déconnecte l'utilisateur
    return redirect('connexion')  # Redirige vers la page de connexion
def connexion(request):
    if request.method == "POST":
        # Récupérer les données du formulaire
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        # Vérification des champs
        if not username or not password:
            messages.error(request, "Veuillez remplir tous les champs.")
            return render(request, "connexion2.html")

        # Vérification des informations dans la base de données
        try:
            coach = Coach.objects.get(username=username)
            if coach.check_password(password):  # Vérification du mot de passe haché
                request.session['coach_id'] = coach.idcoach
                request.session.modified = True
                return redirect("accueil")
            else:
                messages.error(request, "Mot de passe incorrect.")
        except Coach.DoesNotExist:
            messages.error(request, "Nom d'utilisateur non trouvé.")

    # Si l'utilisateur est déjà connecté, rediriger vers l'accueil
    if 'coach_id' in request.session:
        return redirect("accueil")

    return render(request, "connexion2.html")
def accueil(request):
    # Vérification si l'utilisateur est connecté
    if 'coach_id' not in request.session:
        return redirect("connexion")

    # Récupérer l'utilisateur connecté (le coach)
    coach_id = request.session['coach_id']
    try:
        coach = Coach.objects.get(idcoach=coach_id)  # Utiliser idcoach au lieu de id
        return render(request, 'accueil2.html',{'coach': coach})
    except Coach.DoesNotExist:
        # Si le coach n'existe pas, déconnexion
        del request.session['coach_id']
        return redirect("connexion")
def joueur(request):
    if request.method == 'POST':
        # Données obligatoires
        prenom = request.POST.get('firstName')
        nom = request.POST.get('lastName')
        age = request.POST.get('age')
        poste_id = request.POST.get('position')

        # Récupérer le poste et le rôle par défaut
        poste = Poste.objects.get(idposte=poste_id)
        role = Role.objects.get(idrole=1)  # Remplacez par l'ID du rôle par défaut

        # Créer le joueur
        joueur = Joueur.objects.create(
            prenomjoueur=prenom,
            nomjoueur=nom,
            refposte=poste,
            refrole=role
        )

        # Gérer les statistiques optionnelles
        nbmatchs = request.POST.get('matchesPlayed') or 0
        buts = request.POST.get('goals') or 0
        passes = request.POST.get('assists') or 0

        # Vérifier si les statistiques sont remplies
        if nbmatchs or buts or passes:
            Stats.objects.create(
                refjoueur=joueur,
                nbmatchs=int(nbmatchs),
                buts=int(buts),
                passed=int(passes)
            )

        return redirect('liste_joueurs')  # Redirige vers la liste des joueurs

    postes = Poste.objects.all()
    return render(request, 'joueur.html', {'postes': postes})

from django.shortcuts import render
from .models import Joueur, Stats, Role

def tactique(request):
    joueurs = Joueur.objects.all()
    roles = Role.objects.all()

    # Associer chaque joueur à ses statistiques
    joueurs_stats = []
    for joueur in joueurs:
        try:
            joueur_stats = Stats.objects.get(refjoueur=joueur)
        except Stats.DoesNotExist:
            joueur_stats = None
        joueurs_stats.append({
            'joueur': joueur,
            'stats': joueur_stats,
            'full_name': f"{joueur.prenomjoueur} {joueur.nomjoueur}"
        })

    items = [{'id': role.idrole, 'name': role.nomrole, 'description': role.descriptionrole} for role in roles]
    return render(request, 'tactique.html', {'joueurs_stats': joueurs_stats, 'items': items})

def save_tactique(request):
    try:
        data = json.loads(request.body)
        nom_tactique = data.get('nom')
        positions = data.get('positions', [])

        if not nom_tactique:
            return JsonResponse({
                'status': 'error',
                'message': 'Le nom de la tactique est requis.'
            }, status=400)

        # Créer la tactique
        equipe = Equipe.objects.first()  # À adapter selon votre logique
        tactique = Tactique.objects.create(
            nom=nom_tactique,
            refequipe=equipe
        )

        # Sauvegarder les positions
        for pos in positions:
            if not pos.get('joueur'):
                continue

            # Rechercher le joueur par nom complet
            nom_complet = pos['joueur'].strip()
            try:
                if ' ' in nom_complet:
                    prenom, nom = nom_complet.split(' ', 1)
                    joueur = Joueur.objects.get(
                        prenomjoueur__iexact=prenom,
                        nomjoueur__iexact=nom
                    )
                else:
                    # Si un seul mot, chercher dans le prénom ou le nom
                    joueur = Joueur.objects.filter(
                        Q(prenomjoueur__iexact=nom_complet) |
                        Q(nomjoueur__iexact=nom_complet)
                    ).first()
                role_id = pos['roleId']
                role_instance = get_object_or_404(Role, pk=role_id)
                if joueur:
                    print(f"Joueur trouvé: {joueur.prenomjoueur} {joueur.nomjoueur}")
                    PositionJoueur.objects.create(
                        reftactique=tactique,
                        refjoueur=joueur,
                        positionx=float(pos['x']),
                        positiony=float(pos['y']),
                        refrole=role_instance
                    )
                else:
                    print(f"Joueur non trouvé pour: {nom_complet}")

            except Joueur.DoesNotExist:
                print(f"Joueur non trouvé: {nom_complet}")
                continue
            except Exception as e:
                print(f"Erreur lors de la création de la position pour {nom_complet}:", str(e))
                continue

        return JsonResponse({
            'status': 'success',
            'message': 'Tactique sauvegardée avec succès',
            'id': tactique.idtactique
        })

    except Exception as e:
        import traceback
        print("Erreur complète:", traceback.format_exc())
        return JsonResponse({
            'status': 'error',
            'message': f'Erreur lors de la sauvegarde: {str(e)}'
        }, status=500)
@require_http_methods(["GET"])
@require_http_methods(["GET"])
def get_tactiques(request):
    try:
        tactiques = Tactique.objects.all()
        tactiques_data = []
        print(f"Nombre de tactiques trouvées : {tactiques.count()}")

        for tactique in tactiques:
            positions = PositionJoueur.objects.filter(reftactique=tactique)
            positions_data = []

            for pos in positions:
                positions_data.append({
                    'joueur': f"{pos.refjoueur.prenomjoueur} {pos.refjoueur.nomjoueur}",
                    'x': pos.positionx,
                    'y': pos.positiony,
                    'roleId':pos.refrole.idrole
                })

            tactiques_data.append({
                'id': tactique.idtactique,
                'nom': tactique.nom,
                'positions': positions_data
            })

        return JsonResponse({
            'status': 'success',
            'tactiques': tactiques_data
        })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f"Erreur lors de la récupération des tactiques: {str(e)}"
        }, status=500)