from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    movie_name = models.CharField(max_length=255)
    release_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField()#Rating dari film
    likes = models.IntegerField(default=0)#Jumlah likes dari film(equivalent dengan amount pada soal)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
