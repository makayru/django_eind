from django import forms
from .models import Profile, Book, Read


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["BioText", "City"]


class AddNewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["Title", "Description" ,"Author", "Genre", "NumberOfPages"]
    

class AddReadActionForm(forms.ModelForm):
    SCORE_CHOICES = [(i, i) for i in range(1, 11)]
    Score = forms.ChoiceField(choices=SCORE_CHOICES, label='Score')

    class Meta:
        model = Read
        fields = ('Book', 'Date' ,'Score')

    def clean_Score(self):
        score = self.cleaned_data['Score']
        if int(score) < 1 or int(score) > 10:
            raise forms.ValidationError('Score must be between 1 and 10.')
        return score


class ExtAddReadActionForm(forms.ModelForm):
    SCORE_CHOICES = [(i, i) for i in range(1, 11)]
    Score = forms.ChoiceField(choices=SCORE_CHOICES, label='Score')

    class Meta:
        model = Read
        fields = ('Date' ,'Score')
        widgets = {
            'Date': forms.DateInput(attrs={'class': 'form-control'}),
        }


    def clean_Score(self):
        score = self.cleaned_data['Score']
        if int(score) < 1 or int(score) > 10:
            raise forms.ValidationError('Score must be between 1 and 10.')
        return score
