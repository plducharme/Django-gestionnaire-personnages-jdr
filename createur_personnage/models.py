from django.db import models


class Attribut(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    code = models.CharField(max_length=5)

    # implémenter la méthode __str__ pour afficher le nom de l'attribut dans la console d'administration
    def __str__(self):
        return f"{self.nom} ({self.code})"


# Modificateur d'attributs selon
class ModificateurAttribut(models.Model):
    attribut = models.ForeignKey(Attribut, on_delete=models.CASCADE)
    valeur = models.FloatField()
    classe_personnage = models.ForeignKey('ClassePersonnage', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.classe_personnage.nom} - {self.attribut.nom} ({self.valeur})"


class AttributsPersonnage(models.Model):
    attribut = models.ForeignKey(Attribut, on_delete=models.CASCADE)
    valeur = models.FloatField(default=3)
    personnage = models.ForeignKey('Personnage', on_delete=models.CASCADE)


class ClassePersonnage(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom


class Personnage(models.Model):
    nom = models.CharField(max_length=100)
    histoire = models.TextField()
    classe = models.ForeignKey(ClassePersonnage, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} - {self.classe.nom}"




