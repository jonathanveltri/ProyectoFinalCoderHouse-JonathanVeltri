from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Federation(models.Model):
    name = models.CharField(max_length=40)
    initials = models.CharField(max_length=40)
    official_website = models.CharField(max_length=40)
    image = models.ImageField(upload_to = "shields", null = True, blank= True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def  __str__(self):
        return f"{self.initials} - {self.name}"