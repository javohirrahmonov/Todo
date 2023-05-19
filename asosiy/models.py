from django.db import models


class Todo(models.Model):
    nom = models.CharField(max_length=100)
    time = models.DateField()
    batafsil = models.TextField()
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

