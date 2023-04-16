from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, AddNewBookForm

from .models import Profile, Book

# Create your views here.
@login_required
def index(request):
    username = request.user.username
    userprofile = Profile.objects.filter(user=request.user)
    context = {'userprofile': userprofile, 'username': username}
    return render(request, 'base/index.html', context)

@login_required
def MyProfile(request):
    username = request.user.username
    userprofile = Profile.objects.filter(user=request.user)
    context = {'userprofile': userprofile, 'username': username}
    return render(request, 'base/profile.html', context)

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

    context = {'form': form, "username": request.user.username}
    return render(request, 'base/profileform.html', context)

@login_required
def AllBooks(request):
    books = Book.objects.filter(Apporved=True)
    context = {'books': books}
    return render(request, 'base/books.html', context)

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

@login_required
def AddNewBooks(request):
    if request.method == 'POST':
        form = AddNewBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
            form = AddNewBookForm()
    context = {"form": form}
    return render(request, 'base/newbookform.html', context)

@login_required
def UnapprovedBooks(request):
    books = Book.objects.filter(Apporved=False)
    context = {'books': books}
    return render(request, 'base/unapprovedbooks.html', context)

@login_required
def Approve_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.Apporved = True
    book.ApporvedBy = request.user
    book.save()
    return redirect('unapprovedbooks')