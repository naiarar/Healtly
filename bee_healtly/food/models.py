from django.db import models

class Food(models.Model):
    tipe = models.CharField(max_length=15, blank=False, null=False)
    calories = models.DecimalField(max_digits=3, decimal_places=2, blank=False, null=False)
    protein = models.DecimalField(max_digits=3, decimal_places=2, blank=False, null=False)
    cholesterol = models.DecimalField(max_digits=3, decimal_places=2, blank=False, null=False)
    fiber = models.DecimalField(max_digits=3, decimal_places=2, blank=False, null=False)
    carbohydrate = models.DecimalField(max_digits=3, decimal_places=2, blank=False, null=False)
    lipids = models.DecimalField(max_digits=3, decimal_places=2, blank=False, null=False)