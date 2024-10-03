from django.db import models
from django.utils import timezone
# Create your models here.
class Ikasle(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    abizena = models.CharField(max_length=100)
    jaiotze_data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f" {self.izena} {self.abizena} {self.jaiotze_data}"


class Ikasgaiak(models.Model):
    id=models.AutoField(primary_key=True)
    izena=models.CharField(max_length=100)
    maila=models.CharField(max_length=100)
    hizkuntza=models.CharField(max_length=75)

    def __str__(self) :
        return f"{self.izena} {self.maila} {self.hizkuntza}"

class Notak(models.Model):
    nota=models.IntegerField()
    oharra=models.CharField(max_length=200)
    Ikasle=models.ForeignKey(Ikasle,  on_delete=models.CASCADE)
    Ikasgaiak=models.ForeignKey(Ikasgaiak,  on_delete=models.CASCADE)#al borrar el ikasgia borra su relacion con el ikasle
    