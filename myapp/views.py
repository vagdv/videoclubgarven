from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from .models import Movie


# Create your views here.
def movie(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'myapp/movie/movie.html', {'movie': movie})


def index(request):
    latest_question_list = Movie.objects.all()
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'myapp/movie/movies.html', context)

def login(request):
    return render(request, "myapp/login.html")

def register(request):
    return render(request, "myapp/register.html")

