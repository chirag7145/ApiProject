from django.db import models

# Create your models here.
class Pizza(models.Model):
    REGULAR = 'RG'
    SQUARE = 'SQ'
    PIZZA_TYPES = [
        (REGULAR, 'Regular'),
        (SQUARE, 'Square'),
    ]

    type = models.CharField(max_length=2,choices=PIZZA_TYPES,default=REGULAR)
    size = models.ForeignKey('Size',on_delete=models.CASCADE,to_field='size',db_column='size')
    topping = models.ForeignKey('Topping',on_delete=models.CASCADE,to_field='topping',db_column='topping')

    def __str__(self):
        return self.type

class Size(models.Model):
    size = models.CharField(max_length=50,unique=True,primary_key=True)

    def __str__(self):
        return self.size

class Topping(models.Model):
    topping = models.CharField(max_length=50,unique=True,primary_key=True)

    class Meta:
        ordering =('topping',)

    def __str__(self):
        return self.topping