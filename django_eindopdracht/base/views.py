from django.contrib import messages
from django.db.models import Avg
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, AddNewBookForm, AddReadActionForm, ExtAddReadActionForm, CustomUserCreationForm
from datetime import date
from django.utils.timezone import make_aware
import os, sys
from .models import Profile, Book, Read

# Create your views here.
def index(request):
    books = Book.objects.filter(Apporved=True)
    news_feed = Read.objects.all().order_by("-Date")[:10]
    if request.user.is_authenticated:
        readactions = Read.objects.filter(User=request.user)
        username = request.user.username
        userprofile = Profile.objects.filter(user=request.user)
        context = {
            "userprofile": userprofile,
            "username": username,
            "books": books,
            "readactions": readactions,
            "news_feed": news_feed,
        }
    else:
        context = {"books": books, "news_feed": news_feed}
    return render(request, "base/index.html", context)


@login_required
def MyProfile(request):
    username = request.user.username

    reads = Read.objects.filter(User=request.user)
    userprofile = Profile.objects.filter(user=request.user)
    context = {"userprofile": userprofile, "username": username, "reads": reads}
    return render(request, "base/profile.html", context)


@login_required
def edit_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Succesfully Updated.")

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


def DeleteBooksAdmin(request, pk):
    book = Book.objects.get(pk=pk)
    Book.delete(book)
    messages.success(request, "Book Succesfully Deleted.")

    return redirect("admin_books")


def EditBooksAdmin(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == "POST":
        form = AddNewBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            if form.cleaned_data['book_image']:
                book_image = form.cleaned_data['book_image']
                with open(os.path.join(sys.path[0], f"base/static/base/images/{book.id}.jpg"), "wb+") as f:
                    for chunk in book_image.chunks():
                        f.write(chunk)
            form.save()
            messages.success(request, "Book Updated succesfully.")
            return redirect("book_detail", pk)
    else:
        form = AddNewBookForm(instance=book)

    context = {"form": form}
    return render(request, "base/newbookform.html", context)


def AdminReadactions(request):
    read_actions = Read.objects.all()
    context = {"read_actions": read_actions}
    return render(request, "base/adminreadactions.html", context)


def DeleteReadActions(request, pk):
    readaction = Read.objects.get(pk=pk)
    Read.delete(readaction)
    messages.success(request, "Read Action Succesfully Deleted.")
    return redirect("admin_readactions")


@login_required
def MyReadActions(request):
    read_actions = Read.objects.all()
    context = {"read_actions": read_actions}
    return render(request, "base/myreadactions.html", context)


def register(requests):
    if requests.method == "POST":
        form = CustomUserCreationForm(requests.POST)
        if form.is_valid():
            user = form.save()
            login(requests, user)
            messages.success(requests, "Welcome to our website! Tell us about yourself by adding a Biography.")
            return redirect("edit_profile", requests.user.pk)
    else:
        form = CustomUserCreationForm()

    context = {"form": form}
    return render(requests, "registration/register.html", context)


@login_required
def AddNewBooks(request):
    if request.method == "POST":
        form = AddNewBookForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_superuser:
                book = form.save(commit=False)
                book.Apporved = True
                book.ApporvedBy = request.user
                book.save()
                if form.cleaned_data['book_image']:
                    book_image = form.cleaned_data['book_image']
                    with open(os.path.join(sys.path[0], f"base/static/base/images/{book.id}.jpg"), "wb+") as f:
                        for chunk in book_image.chunks():
                            f.write(chunk)
            form.save()
            messages.success(request, "Book Succesfully Added.")
            return redirect("books")
    else:
        form = AddNewBookForm()

    context = {"form": form}
    return render(request, "base/newbookform.html", context)



@login_required
def AddReadAction(request):
    if request.method == "POST":
        user = request.user
        current_date = date.today()
        string_current_date = str(current_date)
        form = AddReadActionForm(request.POST)

        if form.is_valid():
            read_action = form.save(commit=False)
            # Check if a read action for the same book and date already exists for the current user
            existing_read_action = Read.objects.filter(
                User=request.user, Book=read_action.Book, Date=read_action.Date
            ).exists()
            if existing_read_action:
                messages.error(
                    request,
                    "You have already added a read action for this book on the same day.",
                )
                return redirect("myreadactions")
            else:
                read_action.User = request.user
                read_action.save()
                messages.success(
                    request, "Your read action has been added successfully."
                )
            return redirect("myreadactions")
    else:
        form = AddReadActionForm()
    context = {"form": form}
    return render(request, "base/newreadactionform.html", context)

@login_required
def ExtAddReadAction(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        form = ExtAddReadActionForm(request.POST)

        if form.is_valid():
            read_action = form.save(commit=False)
            read_action.Book = Book.objects.get(pk=book_id)

            existing_read_action = Read.objects.filter(
                User=request.user, Book=read_action.Book, Date=read_action.Date
            ).exists()
            if existing_read_action:
                messages.error(
                    request,
                    "You have already added a read action for this book on the same day.",
                )
                return redirect("myreadactions")
            else:
                read_action.User = request.user
                read_action.save()
                messages.success(
                    request, "Your read action has been added successfully."
                )
            return redirect("myreadactions")
    else:
        form = ExtAddReadActionForm()
    context = {"form": form, "book": book}
    return render(request, "base/extreadactionform.html", context)


@login_required
def EditReadAction(request, pk):
    readaction = Read.objects.get(pk=pk)

    if request.method == "POST":
        form = AddReadActionForm(request.POST, instance=readaction)
        if form.is_valid():
            form.save()
            messages.success(request, "Read action updated succesfully.")
            return redirect("myreadactions")
    else:
        form = AddReadActionForm(instance=readaction)

    context = {"form": form}
    return render(request, "base/newreadactionform.html", context)


@login_required
def DeleteReadAction(request, pk):
    readaction = Read.objects.get(pk=pk)
    Read.delete(readaction)
    messages.success(request, "Read action Deleted succesfully.")

    return render(request, "base/myreadactions.html")


@login_required
def UnapprovedBooks(request):
    books = Book.objects.filter(Apporved=False)
    context = {"books": books}
    return render(request, "base/unapprovedbooks.html", context)


@login_required
def Approve_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            book.Apporved = True
            book.ApporvedBy = request.user
            book.save()
            messages.success(request, "Book Succesfully Approved.")
        elif action == 'deny':
            book.delete()
            messages.success(request, "Book Succesfully Denied.")
        return redirect("unapprovedbooks")
    else:
        return HttpResponseNotAllowed(['POST'])

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password Updated.")
            return redirect("password_change_done")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "registration/change_password.html", {"form": form})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id, Apporved=True)
    read_count = Read.objects.filter(Book=book).count()
    average_score = Read.objects.filter(Book=book).aggregate(Avg("Score"))["Score__avg"]
    context = {"book": book, "read_count": read_count, "average_score": average_score}
    return render(request, "base/book_detail.html", context)


def News_feed(request):
    read_actions = Read.objects.all().order_by("-Date")
    context = {"read_actions": read_actions}
    return render(request, "base/newsfeed.html", context)

def user_profile(request, pk):
    user = get_object_or_404(Profile, pk=pk)
    reads = Read.objects.filter(User_id=pk)

    context = {"profile": user, "reads": reads}
    return render(request, "base/profiles.html", context)

