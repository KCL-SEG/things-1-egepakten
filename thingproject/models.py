from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name = models.CharField(blank=False, unique=True,max_length = 30)
    description = models.CharField(blank=True, unique=False,max_length = 120)
    quantity =  models.IntegerField(default=0,
        validators=[MaxValueValidator(100),MinValueValidator(0)])
