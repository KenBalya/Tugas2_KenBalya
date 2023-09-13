from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'PyMovie',
        'name': 'Ken Balya',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)