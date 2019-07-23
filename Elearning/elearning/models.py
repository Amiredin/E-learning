from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length =20,default='')

   
    def __str__(self):
        return self.name



class Exams(models.Model):
    images= models.ImageField(upload_to="elearning" ,null =True)
    category =  models.CharField(max_length =20,default='')



   
    def __str__(self):
        return self.category