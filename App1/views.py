from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from .models import Joueur, Poste, Role, Stats,Tactique, PositionJoueur,Equipe
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
import json
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

    items = [{'name': role.nomrole, 'description': role.descriptionrole} for role in roles]
    return render(request, 'tactique.html', {'joueurs_stats': joueurs_stats, 'items': items})

# Dans views.py, modifiez la fonction save_tactique :
@ensure_csrf_cookie
@require_http_methods(["POST"])
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

                if joueur:
                    print(f"Joueur trouvé: {joueur.prenomjoueur} {joueur.nomjoueur}")
                    PositionJoueur.objects.create(
                        reftactique=tactique,
                        refjoueur=joueur,
                        positionx=float(pos['x']),
                        positiony=float(pos['y'])
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
def get_tactiques(request):
    try:
        tactiques = Tactique.objects.all()

        if not tactiques:
            return JsonResponse({
                'status': 'error',
                'message': "Aucune tactique trouvée."
            }, status=404)

        tactiques_data = []

        for tactique in tactiques:
            positions = PositionJoueur.objects.filter(tactique=tactique)
            positions_data = []

            for position in positions:
                positions_data.append({
                    'joueur': position.joueur.nom,
                    'x': position.position_x,
                    'y': position.position_y
                })

            tactiques_data.append({
                'id': tactique.id,
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
            'message': f"Une erreur inattendue est survenue : {str(e)}"
        }, status=500)
