from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=155)


class Product(models.Model):
    class ChoiceSize(models.TextChoices):
            XS = 'xs'
            X = 'x'
            M = 'm'
            L = 'l'
            XL = 'xl'

    class ChoiceColor(models.TextChoices):
            BLACK = 'Black'
            WHITE = 'White'
            RED = 'Red'
            BLUE = 'Blue'
            GREEN = 'Green'

    image = models.ImageField(upload_to='static/')
    title = models.CharField(max_length=155)
    review = models.IntegerField(default=1, null=True, blank=True)
    price = models.FloatField()
    text = models.TextField()
    choice = models.CharField(max_length=55, choices=ChoiceSize.choices, default=ChoiceSize.XL)
    color = models.CharField(max_length=25, choices=ChoiceColor.choices, default=ChoiceColor.WHITE)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey('app.Category', on_delete=models.CASCADE)
