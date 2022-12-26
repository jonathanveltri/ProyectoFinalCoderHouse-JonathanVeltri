from django.db import models
from federations.models import Federation
# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=40)
    federation = models.ForeignKey(Federation, 
                                    on_delete=models.CASCADE,
                                    null=False,
                                    blank=False)
    country = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    fundation_date = models.DateField()

    def  __str__(self):
        return f"{self.name} - {self.country}"