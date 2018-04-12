from django.contrib import admin

from .models import Utilisateur
from .models import Etudiant
from .models import Specialite
from .models import Intervenant
from .models import Equipe
from .models import Projet
from .models import MessageIntervenant
from .models import MessageEquipe

admin.site.register(Utilisateur)
admin.site.register(Etudiant)
admin.site.register(Specialite)
admin.site.register(Intervenant)
admin.site.register(Equipe)
admin.site.register(Projet)
admin.site.register(MessageEquipe)
admin.site.register(MessageIntervenant)

# Register your models here.
