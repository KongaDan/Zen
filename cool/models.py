from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Promotion(models.Model):
    nom=models.CharField(max_length=50)
    heure_debut_cours=models.TimeField()
    heure_fin_cours=models.TimeField()
    nombre_etudiant=models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.nom

@receiver(post_save, sender=Promotion)
def increment_nombre_etudiant(sender, instance, created, **kwargs):
    if created:
        instance.nombre_etudiant += 1
        instance.save()

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
    def __str__(self):
        return self.nom
    
class Horaire(models.Model):
    jour=models.CharField(max_length=50,null=True)
    cours=models.ManyToManyField("Cours",through="CoursHoraire",through_fields=('jour','cours'))

class CoursHoraire(models.Model):
    jour=models.ForeignKey("Horaire",  on_delete=models.CASCADE)
    cours=models.ForeignKey("Cours",on_delete=models.CASCADE)
    instant=models.BooleanField(default=True)
    
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
  