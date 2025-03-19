from django.urls import path

from . import views

urlpatterns = [
    # L'URL racine redirige vers la vue index de l'application createur_personnage
    # views.index réfère à la fonction index du fichier views.py de l'application createur_personnage
    path("", views.index, name="index"),
]