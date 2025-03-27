from django.urls import path

from . import views

urlpatterns = [
    # L'URL racine redirige vers la vue index de l'application createur_personnage
    # views.index réfère à la fonction index du fichier views.py de l'application createur_personnage
    path("", views.index, name="index"),
    path("creation", views.creation, name="creation"),
    path("creation/ajout", views.ajout_personnage, name="ajout_personnage"),
    path("creation/attributs", views.creation_attributs, name="creation_attributs"),
    path("creation/attributs/ajout", views.ajout_attributs, name="ajout_attributs"),
    path("creation/sommaire", views.sommaire, name="sommaire"),
]