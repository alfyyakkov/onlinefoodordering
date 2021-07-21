from django.db import models

# Create your models here.
class Newuser(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=20)
class NewItem(models.Model):
    Item_name = models.CharField(max_length=20)
    Item_price = models.FloatField()
    Item_image = models.ImageField(upload_to='Myapp/static')
class Bill(models.Model):
    Name=models.CharField(max_length=20)
    Price=models.FloatField()
    Quatity=models.IntegerField()
    Total=models.FloatField()