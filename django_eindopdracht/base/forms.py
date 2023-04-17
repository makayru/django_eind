from django import forms
from .models import Profile, Book, Read


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["BioText", "City"]


class AddNewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["Title", "Author", "Genre", "NumberOfPages"]
    

class AddReadActionForm(forms.ModelForm):
    class Meta:
        model = Read
        fields = ["Book", "Date", "Score"]
