from django.forms import ModelForm
from main.models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ["movie_name", "rating", "description"]