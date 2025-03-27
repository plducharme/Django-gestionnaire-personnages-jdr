from django.shortcuts import render, redirect
from .models import Personnage, Attribut, ModificateurAttribut, ClassePersonnage


# Create your views here.
def index(request):

    context = {
        "message": "Bienvenue dans le créateur de personnage!"
    }
    return render(request, "createur_personnage/index.html", context=context)


def creation(request):
    attributs = Attribut.objects.all()
    classes_personnages = ClassePersonnage.objects.all()
    modificateurs = ModificateurAttribut.objects.all()
    context = {
        "attributs": attributs,
        "classes_personnages": classes_personnages
    }
    return render(request, "createur_personnage/creation.html", context=context)


def creation_attributs(request):
    attributs = Attribut.objects.all()
    personnage = Personnage.objects.get(pk=request.session["personnage_id"])
    modificateurs_classe = ModificateurAttribut.objects.filter(classe_personnage=personnage.classe)
    # modificateurs_classe_dict = {mc.attribut.nom: mc for mc in modificateurs_classe}
    context = {
        "attributs": attributs,
        "personnage": personnage,
        "modificateurs_classe": modificateurs_classe
    }
    return render(request, "createur_personnage/creation_attributs.html", context=context)


def ajout_personnage(request):
    nom = request.POST["nom"]
    classe_personnage = ClassePersonnage.objects.get(pk=request.POST["classe"])
    personnage = Personnage(nom=nom, classe=classe_personnage)
    personnage.save()

    request.session["personnage_id"] = personnage.id
    return redirect("creation_attributs")


def ajout_attributs(request):
    personnage = Personnage.objects.get(pk=request.session["personnage_id"])
    attributs = Attribut.objects.all()
    modificateur_attributs = ModificateurAttribut.objects.filter(classe_personnage=personnage.classe.id)

    total_points = 0
    # validation rapide
    for attribut in attributs:
        total_points += float(request.POST[attribut.nom])

    if total_points != len(attributs) * 3 + 10:
        context = {
            "message": "Vous avez dépassé le nombre de points alloués"
        }
        return render(request, "createur_personnage/creation_attributs.html", context=context)

    for attribut in attributs:
        valeur = request.POST[attribut.nom]
        # FIXME: fix queryset get() error
        modificateur = modificateur_attributs.get(attribut__nom=attribut.nom)
        valeur = float(valeur) + modificateur.valeur
        personnage.attributspersonnage_set.create(attribut=attribut, valeur=valeur)
    return redirect("sommaire")


def sommaire(request):
    personnage = Personnage.objects.get(pk=request.session["personnage_id"])
    attributs_personnage = personnage.attributspersonnage_set.all()
    context = {
        "personnage": personnage,
        "attributs_personnage": attributs_personnage
    }
    return render(request, "createur_personnage/sommaire.html", context=context)

# TODO implémenter routes restantes
