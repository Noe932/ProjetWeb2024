"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from App1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('App1/', views.index, name='index'),
    path('liste-joueurs/', views.liste_joueurs, name='liste_joueurs'),
    path('creer-compte/', views.creer_compte, name='creer_compte'),
    path('connexion/', views.connexion, name='connexion'),

    path('acceuil/',views.accueil,name='accueil'),

    path('joueur/', views.joueur, name='joueur'),

    path('tactique/', views.tactique, name='tactique'),
    path('save_tactique/', views.save_tactique, name='save_tactique'),
    path('get_tactiques/', views.get_tactiques, name='get_tactiques'),

]

