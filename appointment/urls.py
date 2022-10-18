from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview, name='home'),
    path('book/', views.book, name='book'),
    path('book/form/', views.form, name="form")
]
