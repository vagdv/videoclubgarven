from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Movie
from .forms import MovieForm


@staff_member_required(login_url='login')
def index(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
    movies = Movie.objects.all().order_by('-id')

    return render(request, 'myapp/crud/movies.html', {'movies': movies})


@staff_member_required(login_url='login')
def deleteMovie(request, movie_id):
    movieToDelete = Movie.objects.get(pk=movie_id)
    movieToDelete.delete()
    return redirect('/admin/movies')
