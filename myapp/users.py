from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator


# @login_required(login_url='login')
# def movie(request, movie_id):
#     try:
#         movie = Movie.objects.get(pk=movie_id)
#     except Movie.DoesNotExist:
#         raise Http404("Movie does not exist")
#     return render(request, 'myapp/movie/movie.html', {'movie': movie})


@login_required(login_url='login')
def index(request):
    User = get_user_model()
    users = User.objects.all()

    #paginator = Paginator(users, 3)
    #page_obj = paginator.get_page(page_number)

    return render(request, 'myapp/crud/users.html', {'users': users})