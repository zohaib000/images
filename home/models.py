from django.db import models

# Create your models here.

class img(models.Model):
    name=models.ImageField(upload_to="images")