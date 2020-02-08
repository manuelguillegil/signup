from django.db import models

# Create your models here.

class User_Information(models.Model):
    email = models.EmailField(max_length=40, unique=True)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.email