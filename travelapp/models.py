from django.db import models

# Create your models here.
class Mode(models.Model):
    modes=models.CharField(max_length=100)
    
    def __str__(self):
        return self.modes
    
class ModeType(models.Model):
    service=models.CharField(max_length=100,null=True,blank=True)
    modes=models.ForeignKey(Mode,on_delete=models.CASCADE)
    price_per_km=models.FloatField(default=1.1)

    def __str__(self):
        return f"{self.modes} -- {self.service}"


class Route(models.Model):
    
    source=models.CharField(max_length=100)
    via=models.CharField(max_length=500,blank=True,null=True)
    destination=models.CharField(max_length=150)
    distance=models.FloatField(null=True)

    def __str__(self):
        if self.via:
            return f"{self.source} --> {self.destination} | Via: {self.via}"
        return f"{self.source} --> {self.destination}"
    
class Book(models.Model):
    mode=models.ForeignKey(ModeType,on_delete=models.CASCADE)
    route=models.ForeignKey(Route,on_delete=models.CASCADE)

    total_price=models.IntegerField(null=True)
    passengers=models.IntegerField(default=1)
    seat_no=models.CharField(max_length=10)
    is_booked=models.BooleanField(default=False)
    
    def confirmation(self):
        if(self.is_booked):
            return f"Seat  {self.seat_no} is booked "
        return f"Seat Not available"
    def __str__(self):
        return f"{self.seat_no} "

    def calculate_price(self):
        return self.mode.price_per_km*self.route.distance*self.passengers
    
    def save(self,*args,**kwargs):
        self.total_price=self.calculate_price()
        super().save(*args,**kwargs)

    def message(self):
        return f"Your ticket for {self.route} is successfully booked"

    def __str__(self):
        return f"{self.passengers} passengers in {self.mode}"


class Seat(models.Model):
    route=models.ForeignKey(Route,on_delete=models.CASCADE)
    seat_no=models.CharField(max_length=10)
    is_booked=models.BooleanField(default=False)
    
    def confirmation(self):
        if(self.is_booked):
            return f"Seat  {self.seat_no} is booked "
        return f"Seat Not available"
    def __str__(self):
        return f"{self.seat_no} "
    



    





