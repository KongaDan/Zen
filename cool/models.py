from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class Promotion(models.Model):
    nom=models.CharField(max_length=50)
    heure_debut_cours=models.TimeField()
    heure_fin_cours=models.TimeField()
    def __str__(self) -> str:
        return self.nom



class Section(models.Model):
    nom=models.CharField(max_length=50)
    def __str__(self):
        return self.nom

class Cours(models.Model):
    nom=models.CharField(max_length=50)
    description=models.TextField(max_length=200,default=True)
    nombre_heure=models.IntegerField(null=True)
    prof=models.CharField(max_length=50,default='',blank=True)
    section=models.ManyToManyField(Section)
    promotion=models.ForeignKey(Promotion,on_delete=models.CASCADE)
    jour=models.ManyToManyField("Semaines",through="CoursSemaines",through_fields=('cours','jour'))

    def __str__(self):
        return self.nom
    
class Semaines(models.Model):
    jour=models.CharField(max_length=50,null=True)
    cours_de_semaines=models.ManyToManyField("Cours",through="CoursSemaines",through_fields=('jour','cours'))
    def __str__(self) -> str:
        return self.jour

class CoursSemaines(models.Model):
    jour=models.ForeignKey("Semaines",on_delete=models.CASCADE)
    cours=models.ForeignKey("Cours",on_delete=models.CASCADE)
    avant_midi=models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"{self.jour} : {self.cours}"
    
class User(AbstractUser):
    numero=models.CharField(max_length=20,default='0000')
    promotion=models.ForeignKey("Promotion", on_delete=models.CASCADE,null=True)
    section=models.ForeignKey("Section",on_delete=models.CASCADE,null=True)
    email=models.EmailField(max_length=254, verbose_name='email address')
    EMAIL_FIELD='email'
    def __str__(self):
        return self.username 
          
class Tache(models.Model):
    nom=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
    heure_creation=models.DateTimeField(auto_now_add=True)
    heure_fin=models.DateTimeField(null=True)
    etudiant=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
  