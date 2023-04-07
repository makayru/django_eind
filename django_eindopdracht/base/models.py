from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    BioText = models.TextField()
    City = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Book(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Genre = models.CharField(max_length=100)
    NumberOfPages = models.IntegerField()
    Apporved = models.BooleanField(default=False)
    ApporvedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approved_by', null=True, blank=True)
    def __str__(self):
        return self.Title
    
class Read(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField()
    Score = models.IntegerField()
    def __str__(self):
        return f"{self.Book.Title} by {self.User.get_username()}"
