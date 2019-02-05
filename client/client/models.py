from django.db import models


class User_Info(models.Model):
    Name = models.CharField(max_length=200, default='')
    LName = models.CharField(max_length=200, default='')
    Fonction = models.CharField(max_length=200, default='')
    Profil = models.FileField(upload_to='Profil/',null=True, blank=True)
    Adresse = models.CharField(max_length=200, default='')
    Naissance = models.CharField(max_length=200, default='')
    Lieu = models.CharField(max_length=200, default='')
    Commune = models.CharField(max_length=200, default='')
    Departement = models.CharField(max_length=200, default='')
    Sexe = models.CharField(max_length=200, default='')
    Statut = models.CharField(max_length=200, default='')
    Dependant = models.CharField(max_length=200, default='')
    Telephone_1 = models.CharField(max_length=200, default='')
    Telephone_2 = models.CharField(max_length=200, default='')
    Email = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.LName + " " + self.Name