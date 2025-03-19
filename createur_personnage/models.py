from django.db import models


class Attribut(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    code = models.CharField(max_length=5)

    # implémenter la méthode __str__ pour afficher le nom de l'attribut dans la console d'administration
    def __str__(self):
        return f"{self.nom} ({self.code})"

class ModificateurAttribut(models.Model):
    attribut = models.ForeignKey(Attribut, on_delete=models.CASCADE)
    valeur = models.FloatField()

    def __str__(self):
        return f"{self.attribut.nom} ({self.valeur})"


class ClassePersonnage(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    modificateurs = models.ManyToManyField(ModificateurAttribut)

    def __str__(self):
        return self.nom

class Personnage(models.Model):
    nom = models.CharField(max_length=100)
    histoire = models.TextField()
    classe = models.ForeignKey(ClassePersonnage, on_delete=models.CASCADE)
    attributs = models.ManyToManyField(Attribut)

    def __str__(self):
        return self.nom