from django.db import models

# Create your models here.
class members(models.Model):
    name=models.CharField(max_length=100,unique=True)
    age=models.IntegerField()
    var=[
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender=models.CharField(max_length=1,choices=var)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.name
        