from django.db import models


class Utilisateur(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField(max_length=70)
    dateInscription = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
    	return self.prenom + ' ' + self.nom

class Etudiant(Utilisateur):
  	classe = models.CharField(max_length=200)
  	def __str__(self):
  		return self.prenom + ' '+ self.nom
  	

class Specialite(models.Model):
	libelle = models.CharField(max_length=200)
	def __str__(self):
  		return self.libelle
	
class Intervenant(Utilisateur):
	specialites = models.ManyToManyField(Specialite)
	def __str__(self):
  		return self.prenom + self.nom

class Equipe(models.Model):
    dateCreation = models.DateTimeField(auto_now_add=True, blank=True)
    nomEquipe = models.CharField(max_length=200)
    tempsAlloue = models.IntegerField(default=0)
    etudiants = models.ManyToManyField(Etudiant)
    def __str__(self):
    	return self.nomEquipe
  		


class Projet(models.Model):
	titre = models.CharField(max_length=200)
	nbMaxEquipe = models.IntegerField()
	description = models.TextField()
	dateCreation = models.DateTimeField(auto_now_add=True, blank=True)
	dateFin = models.DateTimeField(auto_now_add=True, blank=True)
	equipes = models.ManyToManyField(Equipe)
	intervenants = models.ManyToManyField(Intervenant)
	def __str__(self):
		return self.titre

class MessageIntervenant(models.Model):
	contenue = models.TextField()
	dateMessage = models.DateTimeField(auto_now_add=True, blank=True)
	decompteTemps = models.IntegerField(default=0)
	projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
	intervenant = models.ForeignKey(Intervenant, on_delete=models.CASCADE)
	def __str__(self):
		return self.intervenant.nom + ' ' + self.projet.titre
	


class MessageEquipe(models.Model):
	contenue = models.TextField()
	dateMessage = models.DateTimeField(auto_now_add=True, blank=True)
	projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
	equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
	def __str__(self):
		return self.equipe.nomEquipe + ' ' + self.projet.titre



# Create your models here.
