from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=35)
    subject =models.CharField(max_length=50)
    message =models.TextField(max_length=300)

    def __str__(self):
        return self.name