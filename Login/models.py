from datetime import date
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    id = models.AutoField(primary_key = True)
    is_staff = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.username
    


class HeroListModel(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    imageUrl = models.CharField(max_length=400)
    description = models.TextField(max_length=400,blank=True)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
    qualification = models.CharField(max_length=50)
    skills = models.CharField(max_length=255)
    dob = models.DateField(max_length=20)
    location = models.CharField(max_length=50)
    yearOfExp = models.CharField(max_length=10)
    designation = models.CharField(max_length=50)
    age =models.IntegerField(blank=True,null=True)
   

    def calculate_age(self):
        today = date.today()
        if self.dob:
            return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return None

    def save(self, *args, **kwargs):
        self.age = self.calculate_age()
        super(Candidate, self).save(*args, **kwargs)


    def __str__(self):
        return self.name