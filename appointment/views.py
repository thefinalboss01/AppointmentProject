from django.shortcuts import render
from .models import Genders
from users.models import DoctorProfile

# Create your views here.
def homeview(request):
  return render(request, 'appointment/index.html' )

def book(request):
  doctors = DoctorProfile.objects.all()
  context = {
    'doctors': doctors
  }
  return render(request, 'appointment/book.html', context)


def form(request):
  genders = Genders.objects.all()
  context = {
    'genders': genders
  }
  return render(request, 'appointment/form.html')