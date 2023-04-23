from django import forms
from .models import Profile, Book, Read
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["FirstName", "LastName", "Email" ,"BioText", "City"]
        widgets = {
            'FirstName': forms.TextInput(attrs={'class': 'form-control'}),
            'LastName': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
            'BioText': forms.Textarea(attrs={'class': 'form-control'}),
            'City': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',  'city']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),        }

        

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        profile = user.profile
        profile.FirstName = self.cleaned_data.get('first_name')
        profile.LastName = self.cleaned_data.get('last_name')
        profile.City = self.cleaned_data.get('city')
        profile.Email = self.cleaned_data.get('email')
        profile.save()

        return user
    
class AddNewBookForm(forms.ModelForm) :
    book_image = forms.FileField(required=False, label='Upload an image', widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Book
        fields = ["Title", "Description" ,"Author", "Genre", "NumberOfPages", "book_image"]
        widgets = {
            'Title': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control'}),
            'Author': forms.TextInput(attrs={'class': 'form-control'}),
            'Genre': forms.TextInput(attrs={'class': 'form-control'}),
            'NumberOfPages': forms.NumberInput(attrs={'class': 'form-control'}),
            'book_image': forms.FileInput(attrs={'class': 'form-control', "required": True}),
        }
    
    

class AddReadActionForm(forms.ModelForm):
    SCORE_CHOICES = [(i, i) for i in range(1, 11)]
    Score = forms.ChoiceField(choices=SCORE_CHOICES, label='Score', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Read
        fields = ('Book', 'Date' ,'Score')
        widgets = {
            'Book': forms.Select(attrs={'class': 'form-control'}),
            'Date': forms.DateInput(attrs={'class': 'form-control'}),
            'Score': forms.Select(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(AddReadActionForm, self).__init__(*args, **kwargs)
        self.fields['Book'].queryset = Book.objects.filter(Apporved=True)

    def clean_Score(self):
        score = self.cleaned_data['Score']
        if int(score) < 1 or int(score) > 10:
            raise forms.ValidationError('Score must be between 1 and 10.')
        return score


class ExtAddReadActionForm(forms.ModelForm):
    SCORE_CHOICES = [(i, i) for i in range(1, 11)]
    Score = forms.ChoiceField(choices=SCORE_CHOICES, label='Score', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Read
        fields = ('Date' ,'Score')
        widgets = {
            'Date': forms.DateInput(attrs={'class': 'form-control'}),
            'Score': forms.Select(attrs={'class': 'form-control'}),
        }


    def clean_Score(self):
        score = self.cleaned_data['Score']
        if int(score) < 1 or int(score) > 10:
            raise forms.ValidationError('Score must be between 1 and 10.')
        return score

    
