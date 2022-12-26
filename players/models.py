from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    team = models.CharField(max_length=40)
    number = models.IntegerField()
    position = models.CharField(max_length=40)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(
        User, through="Comment", related_name="comments_owned"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        unique_together = (
            "name",
            "last_name",
        )
        ordering = ["-last_name"]
    
    def  __str__(self):
        return f"{self.name} - {self.last_name} - {self.number}"

class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
