from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Personne(models.Model):
    nom = models.CharField(max_length=100, blank=True, null=True)
    postnom = models.CharField(max_length=100, blank=True, null=True)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    sexe = models.CharField(max_length=1, blank=True, null=True)
    telephone = models.CharField(max_length=25, blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    lieu_naissance = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.nom

class Role(models.Model):
    libelle=models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.libelle

class Compte(AbstractUser):
    # username=models.CharField(max_length=30, blank=False, null=False)
    mot_de_passe=models.CharField(max_length=30, blank=False, null=False)
    # email=models.CharField(max_length=30, blank=True, null=True)
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    role = models.ManyToManyField(Role, related_name='compte_role') 
         
    def __str__(self):
        return self.username

class Article(models.Model):
    titre=models.CharField(max_length=30, blank=True, null=True)
    contenu=models.TextField(blank=True, null=True) 
    date=models.DateTimeField(blank=True, null=True, auto_now_add=True)
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titre
    
class Commentaire(models.Model):
    description=models.TextField(blank=True, null=True)
    date=models.DateTimeField(blank=True, null=True, auto_now_add=True)
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description
    
    
    