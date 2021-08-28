from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class notice(models.Model):
    company = models.CharField(max_length=20)
    where = models.CharField(max_length=50)
    period = models.IntegerField(blank=True, null=True)
    day = models.CharField(max_length=10)
    time = models.CharField(max_length=20, blank=True, default="")
    pay = models.IntegerField(blank=True, null=True)
    detail = models.TextField()
    valunteer = models.IntegerField(default=0)

    image = models.ImageField(upload_to = 'image/', default="", blank=True)

    def __str__(self):
        return self.company

class comment(models.Model):
    notice_id = models.ForeignKey(notice, on_delete=models.CASCADE, null=True)
    writter = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.writter