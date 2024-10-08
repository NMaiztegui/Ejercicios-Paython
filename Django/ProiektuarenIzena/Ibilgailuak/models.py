from django.db import models
from django.utils import timezone

# Create your models here.
class Kotxea(models.Model):
    id=models.AutoField(primary_key=True)
    marca=models.CharField(max_length=100)
    modelo=models.CharField(max_length=100)
    matricula=models.CharField(max_length=100)
    alokatua = models.BooleanField(default=False) 

    def __str__(self):
        return f'{self.marca} - {self.modelo} - {self.matricula}-{self.alokatua}'
class Bezeroa(models.Model):
    id=models.AutoField(primary_key=True)
    izena=models.CharField(max_length=100)
    abizena=models.CharField(max_length=100)
    dni=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.izena} - {self.abizena} - {self.dni}'

class AlokatutakoKotxeak(models.Model):
    kotxea=models.ForeignKey(Kotxea, on_delete=models.CASCADE)
    bezeroa=models.ForeignKey(Bezeroa, on_delete=models.CASCADE)
    alokatze_data=models.DateTimeField (default=timezone.now)# se estable automaticamente la  hora y fecha en la que se ha metido a la base de datos

    def __str__(self) :
        return f'{self.kotxea} - {self.bezeroa} - Alokatua'