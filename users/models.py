from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  image = models.ImageField(default="profile.jpg", upload_to='doctor_pictures')
  contact_number = models.CharField(max_length=100, default='99999')

  def __str__(self):
    return self.user.username

class DoctorProfile(models.Model):
  user = models.OneToOneField(Profile, on_delete = models.CASCADE)
  speciality = models.CharField(max_length=100, default='General Physician')

  def __str__(self):
    return self.user.user.username

