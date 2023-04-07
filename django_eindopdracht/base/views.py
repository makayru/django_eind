from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

from .models import Profile

# Create your views here.
@login_required
def index(request):

    username = request.user.username
    userprofile = Profile.objects.filter(user=request.user)
    context = {'username': username, 'userprofile': userprofile}
    return render(request, 'base/index.html', context)

@login_required
def edit_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,  instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'base/profileform.html', context)

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