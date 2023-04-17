from django.contrib import messages
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, AddNewBookForm, AddReadActionForm

from .models import Profile, Book, Read

# Create your views here.
@login_required
def index(request):
    books = Book.objects.filter(Apporved=True)
    news_feed = Read.objects.all().order_by("-Date")[:10]
    readactions = Read.objects.filter(User=request.user)
    username = request.user.username
    userprofile = Profile.objects.filter(user=request.user)
    context = {"userprofile": userprofile, "username": username, "books": books, "readactions": readactions, "news_feed": news_feed}
    return render(request, "base/index.html", context)


@login_required
def MyProfile(request):
    username = request.user.username
    userprofile = Profile.objects.filter(user=request.user)
    context = {"userprofile": userprofile, "username": username}
    return render(request, "base/profile.html", context)


@login_required
def edit_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ProfileForm(instance=profile)

    context = {"form": form, "username": request.user.username}
    return render(request, "base/profileform.html", context)


@login_required
def AllBooks(request):
    books = Book.objects.filter(Apporved=True)
    context = {"books": books}
    return render(request, "base/books.html", context)


@login_required
def MyReadActions(request):
    read_actions = Read.objects.all()
    context = {"read_actions": read_actions}
    return render(request, "base/myreadactions.html", context)


def register(requests):
    if requests.method == "POST":
        form = UserCreationForm(requests.POST)
        if form.is_valid():
            user = form.save()
            login(requests, user)
            return redirect("index")
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(requests, "registration/register.html", context)


@login_required
def AddNewBooks(request):
    if request.method == "POST":
        form = AddNewBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AddNewBookForm()
    context = {"form": form}
    return render(request, "base/newbookform.html", context)


@login_required
def AddReadAction(request):
    if request.method == "POST":
        form = AddReadActionForm(request.POST)
        if form.is_valid():
            read_action = form.save(commit=False)
            read_action.User = request.user
            read_action.save()
            return redirect("index")
    else:
        form = AddReadActionForm()
    context = {"form": form}
    return render(request, "base/newreadactionform.html", context)


@login_required
def EditReadAction(request, pk):
    readaction = Read.objects.get(pk=pk)

    if request.method == "POST":
        form = AddReadActionForm(request.POST, instance=readaction)
        if form.is_valid():
            form.save()
            messages.success(request, "Read action updated succesfully.")
            return redirect('index')
    else:
        form = AddReadActionForm(instance=readaction)
    
    context = {"form": form}
    return render(request, "base/newreadactionform.html", context)


@login_required
def DeleteReadAction(request, pk):
    readaction = Read.objects.get(pk=pk)
    Read.delete(readaction)
    return render(request, "base/myreadactions.html")
    


@login_required
def UnapprovedBooks(request):
    books = Book.objects.filter(Apporved=False)
    context = {"books": books}
    return render(request, "base/unapprovedbooks.html", context)


@login_required
def Approve_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.Apporved = True
    book.ApporvedBy = request.user
    book.save()
    return redirect("unapprovedbooks")


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the success page after changing the password
            return redirect("password_change_done")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id, Apporved=True)
    read_count = Read.objects.filter(Book=book).count()
    average_score = Read.objects.filter(Book=book).aggregate(Avg('Score'))['Score__avg']
    context = {'book': book, 'read_count': read_count, 'average_score': average_score}
    return render(request, 'base/book_detail.html', context)


@login_required
def News_feed(request):
    read_actions = Read.objects.all()
    context = {"read_actions": read_actions}
    return render(request, "base/newsfeed.html", context)

