from email.policy import default
from django.db import models

# Create your models here.

class Genders(models.Model):
  name = models.CharField(max_length=20)

  def __str__(self):
    return self.name


class Appointment(models.Model):

  name = models.CharField(max_length=100)
  age = models.IntegerField()
  sex = models.ForeignKey(Genders, on_delete= models.CASCADE)
  date = models.DateField()
  desc = models.CharField(max_length = 1000)

  def __str__(self):
    return (self.name + 'Appointment')
