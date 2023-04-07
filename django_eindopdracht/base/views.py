from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    username = request.user.username
    context = {'username' : username}
    return render(request, 'base/index.html', context)


def register(requests):
    if requests.method == 'POST':
        form = UserCreationForm(requests.POST)
        if form.is_valid():
            user = form.save()
            login(requests, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    
    context = {"form": form}
    return render(requests, 'registration/register.html', context)