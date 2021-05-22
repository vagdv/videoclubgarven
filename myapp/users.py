from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import RegisterUserForm
from django.core.paginator import Paginator


@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
    User = get_user_model()
    users = User.objects.all()

    return render(request, 'myapp/crud/users.html', {'users': users})
