from django.contrib import admin

from .models import Personnage, ClassePersonnage, Attribut, ModificateurAttribut


# Register your models here.
admin.site.register(Personnage)
admin.site.register(ClassePersonnage)
admin.site.register(Attribut)
admin.site.register(ModificateurAttribut)
