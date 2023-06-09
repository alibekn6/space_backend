from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=255, null=False)
    role = models.CharField(max_length=255, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='members')

    def __str__(self):
        return self.name