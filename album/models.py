from django.db import models

# Create your models here.
class Team(models.Model):
    """" EQUIPO """
    name = models.CharField(max_length=50)
    shield = models.ImageField(upload_to='shields/')
    team = models.ImageField(upload_to='teams/')
    pub_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    ()
    
from django.db import models

class Player(models.Model):
    """Futbolista"""

    team = models.ForeignKey('Team',on_delete=models.PROTECT,related_name='players')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='players/')
    pub_date = models.DateField(auto_now_add=True)
    height = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.IntegerField()
    comment = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"