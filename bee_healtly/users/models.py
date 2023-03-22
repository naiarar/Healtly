from django.db import models


class Training_level(models.Model):
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.level



class User(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    adress = models.CharField(max_length=200,blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    training_level = models.ForeignKey(Training_level, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return self.name
class Measurements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='measurements')
    height = models.DecimalField(max_digits=3, decimal_places=2, blank=False, null=False)
    weight = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False)
    arms = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False) #braço
    chest = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False) #peito
    waist = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False) #cintura
    hips = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False) #quadril
    legs = models.DecimalField(max_digits=4, decimal_places=1, blank=False, null=False) #perna

