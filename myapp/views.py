from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from .models import Movie


@login_required(login_url='login')
def movie(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'myapp/movie/movie.html', {'movie': movie})


@login_required(login_url='login')
def index(request):
    latest_question_list = Movie.objects.all()
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'myapp/movie/movies.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.POST:
            username = request.POST['Nombre']
            password = request.POST['pass']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                return render(request, "myapp/login.html", {'error': 'Wrong username or password. Try again'})
        else:
            return render(request, "myapp/login.html")


def logout(request):
    auth_logout(request)
    return render(request, "myapp/login.html")


def register(request):
    return render(request, "myapp/register.html")
