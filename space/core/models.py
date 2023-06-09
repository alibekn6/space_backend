from django.db import models

# Create your models here.


class WhoAreWe(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='main_images')


class Achivements(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='achivements')


