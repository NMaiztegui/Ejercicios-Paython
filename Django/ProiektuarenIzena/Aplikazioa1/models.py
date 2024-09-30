from django.db import models
from django.utils import timezone
# Create your models here.
class Ikasle(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    abizena = models.CharField(max_length=100)
    jaiotze_data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Ikaslearen izena {self.izena} da eta abizenak   {self.abizena}."

