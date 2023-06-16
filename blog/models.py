from django.db import models

# Create your models here.

class Text(models.Model):
    text = models.TextField(blank=True)

    def __str__(self):
        return self.text
    
class Block(models.Model):
    subtitle = models.TextField(blank=True)
    time = models.CharField(max_length=200)
    price = models.CharField(max_length=200)


    def __str__(self):
        return self.subtitle
    
class Prikons(models.Model):
    text = models.TextField(blank=True)

    def __str__(self):
        return self.text
    
class PriKonstruktor(models.Model):
    title = models.CharField(max_length=250,blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title



    
class Faq(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
class ConsAnswers(models.Model):
    name = models.CharField(max_length=200)
    types = models.CharField(max_length=250)
    price = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
# class ConsAnswers(models.Model):
#     title = models.CharField(max_length=250)
#     consa1 = models.CharField(max_length=150)
#     consa2 = models.CharField(max_length=150)
#     consa3 = models.CharField(max_length=150)
#     consa4 = models.CharField(max_length=150)
#     consa5 = models.CharField(max_length=150)
#     price = models.IntegerField(blank=True)



    

class Portfolio(models.Model):
    file = models.FileField(upload_to='news/',max_length=250,null=True,default=0)

    
    