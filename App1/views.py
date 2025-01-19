from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import get_object_or_404
from functools import wraps
import json
from .models import (
    Joueur, Poste, Role, Stats, Tactique,
    PositionJoueur, Equipe, Coach
)


# Décorateur personnalisé pour vérifier l'authentification
def login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if 'coach_id' not in request.session:
            messages.error(request, "Veuillez vous connecter pour accéder à cette page.")
            return redirect('connexion')
        return view_func(request, *args, **kwargs)

    return wrapper


# Vues d'authentification (non protégées)
def connexion(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            messages.error(request, "Veuillez remplir tous les champs.")
            return render(request, "connexion2.html")

        try:
            coach = Coach.objects.get(username=username)
            if coach.check_password(password):
                request.session['coach_id'] = coach.idcoach
                request.session.modified = True
                return redirect("accueil")
            else:
                messages.error(request, "Mot de passe incorrect.")
        except Coach.DoesNotExist:
            messages.error(request, "Nom d'utilisateur non trouvé.")

    if 'coach_id' in request.session:
        return redirect("accueil")

    return render(request, "connexion2.html")


def creer_compte(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        nom = request.POST.get("nom", "").strip()
        prenom = request.POST.get("prenom", "").strip()
        age = request.POST.get("age", "").strip()
        password = request.POST.get("password", "").strip()

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

        if Coach.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà utilisé.")
            return render(request, "creercompte.html", {
                "nom": nom,
                "prenom": prenom,
                "age": age
            })

        coach = Coach.objects.create(
            username=username,
            nomcoach=nom,
            prenomcoach=prenom,
            agecoach=int(age),
            password=password
        )
        coach.set_password(password)
        coach.save()

        request.session['coach_id'] = coach.idcoach
        request.session.modified = True

        messages.success(request, "Votre compte a été créé avec succès ! Créez maintenant votre équipe.")
        return redirect("equipe")

    return render(request, "creercompte.html")


# Vues protégées (nécessitant une authentification)
@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the App1 index.")


@login_required
def liste_joueurs(request):
    joueurs = Joueur.objects.select_related('refrole', 'refposte')
    return render(request, 'listeJoueur.html', {'joueurs': joueurs})


@login_required
def logout_view(request):
    logout(request)
    return redirect('connexion')


@login_required
def creer_equipe(request):
    try:
        coach = Coach.objects.get(idcoach=request.session['coach_id'])

        try:
            equipe_existante = Equipe.objects.get(refcoach=coach)
            messages.warning(request, "Vous avez déjà une équipe.")
            return redirect('accueil')
        except Equipe.DoesNotExist:
            pass

        if request.method == 'POST':
            nom_equipe = request.POST.get('nomequipe')

            if nom_equipe:
                try:
                    equipe = Equipe(
                        nomequipe=nom_equipe,
                        refcoach=coach
                    )
                    equipe.save()
                    messages.success(request, "Équipe créée avec succès!")
                    return redirect('accueil')
                except Exception as e:
                    messages.error(request, f"Une erreur s'est produite lors de la création de l'équipe: {str(e)}")
            else:
                messages.error(request, "Veuillez fournir un nom d'équipe.")

        return render(request, 'equipe.html', {'coach': coach})

    except Coach.DoesNotExist:
        messages.error(request, "Profil coach non trouvé.")
        return redirect('connexion')


@login_required
def accueil(request):
    try:
        coach = Coach.objects.get(idcoach=request.session['coach_id'])

        try:
            equipe = Equipe.objects.get(refcoach=coach)
        except Equipe.DoesNotExist:
            messages.warning(request, "Vous devez d'abord créer votre équipe.")
            return redirect('equipe')

        return render(request, 'accueil2.html', {'coach': coach})
    except Coach.DoesNotExist:
        del request.session['coach_id']
        return redirect("connexion")


@login_required
def joueur(request):
    if request.method == 'POST':
        prenom = request.POST.get('firstName')
        nom = request.POST.get('lastName')
        age = request.POST.get('age')
        poste_id = request.POST.get('position')

        poste = Poste.objects.get(idposte=poste_id)
        role = Role.objects.get(idrole=1)

        joueur = Joueur.objects.create(
            prenomjoueur=prenom,
            nomjoueur=nom,
            refposte=poste,
            refrole=role
        )

        nbmatchs = request.POST.get('matchesPlayed') or 0
        buts = request.POST.get('goals') or 0
        passes = request.POST.get('assists') or 0

        if nbmatchs or buts or passes:
            Stats.objects.create(
                refjoueur=joueur,
                nbmatchs=int(nbmatchs),
                buts=int(buts),
                passed=int(passes)
            )

        return redirect('liste_joueurs')

    postes = Poste.objects.all()
    return render(request, 'joueur.html', {'postes': postes})


@login_required
def tactique(request):
    joueurs = Joueur.objects.all()
    roles = Role.objects.all()

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


@login_required
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

        equipe = Equipe.objects.first()
        tactique = Tactique.objects.create(
            nom=nom_tactique,
            refequipe=equipe
        )

        for pos in positions:
            if not pos.get('joueur'):
                continue

            nom_complet = pos['joueur'].strip()
            try:
                if ' ' in nom_complet:
                    prenom, nom = nom_complet.split(' ', 1)
                    joueur = Joueur.objects.get(
                        prenomjoueur__iexact=prenom,
                        nomjoueur__iexact=nom
                    )
                else:
                    joueur = Joueur.objects.filter(
                        Q(prenomjoueur__iexact=nom_complet) |
                        Q(nomjoueur__iexact=nom_complet)
                    ).first()

                if joueur:
                    role_id = pos['roleId']
                    role_instance = get_object_or_404(Role, pk=role_id)
                    PositionJoueur.objects.create(
                        reftactique=tactique,
                        refjoueur=joueur,
                        positionx=float(pos['x']),
                        positiony=float(pos['y']),
                        refrole=role_instance
                    )

            except Exception as e:
                continue

        return JsonResponse({
            'status': 'success',
            'message': 'Tactique sauvegardée avec succès',
            'id': tactique.idtactique
        })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Erreur lors de la sauvegarde: {str(e)}'
        }, status=500)


@login_required
@require_http_methods(["GET"])
def get_tactiques(request):
    try:
        tactiques = Tactique.objects.all()
        tactiques_data = []

        for tactique in tactiques:
            positions = PositionJoueur.objects.filter(reftactique=tactique)
            positions_data = []

            for pos in positions:
                positions_data.append({
                    'joueur': f"{pos.refjoueur.prenomjoueur} {pos.refjoueur.nomjoueur}",
                    'x': pos.positionx,
                    'y': pos.positiony,
                    'roleId': pos.refrole.idrole
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

@login_required
def profil_view(request):
    if hasattr(request, 'session') and 'coach_id' in request.session:
        coach_id = request.session['coach_id']
        coach = Coach.objects.get(idcoach=coach_id)

        # Récupérer le nombre de joueurs et de tactiques
        equipe = Equipe.objects.filter(refcoach=coach).first()
        nb_joueurs = Joueur.objects.filter(
            positionjoueur__reftactique__refequipe=equipe).distinct().count() if equipe else 0
        nb_tactiques = Tactique.objects.filter(refequipe=equipe).count() if equipe else 0

        context = {
            'coach': coach,
            'nb_joueurs': nb_joueurs,
            'nb_tactiques': nb_tactiques,
        }
        return render(request, 'profil.html', context)