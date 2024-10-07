from django.db import models

# Create your models here.
class Kotxea(models.Model):
    id=models.AutoField(primary_key=True)
    marca=models.CharField(max_length=100)
    modelo=models.CharField(max_length=100)
    matricula=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.marca} - {self.modelo} - {self.matricula}'
