from django.db import models
# from django.http.response import StreamingHttpResponse
from django.contrib.auth.models import User, auth
from datetime import datetime
# Create your models here.

# class registerDB(models.Model) :
#     uname = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     pwd = models.CharField(max_length=100)

# class ganpatiProducts(models.Model) :
#     productName = models.CharField(max_length=100)
#     price = models.FloatField()
#     description = models.TextField()
#     image = models.ImageField(upload_to='pics')

# class diwaliProducts(models.Model) :
#     productName = models.CharField(max_length=100)
#     price = models.FloatField()
#     description = models.TextField()
#     image = models.ImageField(upload_to='dProductpics')

# class christmasProducts(models.Model) :
#     productName = models.CharField(max_length=100)
#     price = models.FloatField()
#     description = models.TextField()
#     image = models.ImageField(upload_to='cProductpics')

class siteProducts(models.Model) :
    productName = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='productPics')
    category = models.CharField(max_length=100)

class MyCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(siteProducts, on_delete=models.CASCADE)
    added_date = models.DateTimeField(default=datetime.now())

class MyOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(siteProducts, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())