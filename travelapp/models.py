from django.db import models

# Create your models here.
class Mode(models.Model):
    modes=models.CharField(max_length=100)
    per_km=models.FloatField(default=1.3)

    def __str__(self):
        return self.modes


class Route(models.Model):
    modes=models.ForeignKey(Mode,on_delete=models.CASCADE)
    source=models.CharField(max_length=100)
    via=models.CharField(max_length=500)
    destination=models.CharField(max_length=150)

    def __str__(self):
        return f"{self.source} --> {self.destination}"
    
class Book(models.Model):
    mode=models.ForeignKey(Mode,on_delete=models.CASCADE)
    route=models.ForeignKey(Route,on_delete=models.CASCADE)
    price=models.IntegerField()
    passengers=models.IntegerField(default=1)

    def __str__(self):
        return f"{self.passengers} passengers in {self.mode}"

    





