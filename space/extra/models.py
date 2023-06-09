from django.db import models

# Create your models here.


class Tutorials(models.Model):
    title = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to='tutor')
    image2 = models.ImageField(upload_to='tutor')
    image3 = models.ImageField(upload_to='tutor')
    image4 = models.ImageField(upload_to='tutor')
    image5 = models.ImageField(upload_to='tutor')
    image6 = models.ImageField(upload_to='tutor')
    image7 = models.ImageField(upload_to='tutor')
    image8 = models.ImageField(upload_to='tutor')
    image9 = models.ImageField(upload_to='tutor')
    image10 = models.ImageField(upload_to='tutor')