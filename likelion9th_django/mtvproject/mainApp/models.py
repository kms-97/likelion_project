from django.db import models

# Create your models here.


class Teammate(models.Model):
    name = models.CharField(max_length=10)
    birth = models.DateField()
    live = models.CharField(max_length=20)
    birthlocation = models.CharField(max_length=20)
    major = models.CharField(max_length=50)
    food = models.CharField(max_length=20)
    haslover = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    alchol = models.CharField(max_length=20)
    dream = models.TextField()

    def __str__(self):
        return self.name