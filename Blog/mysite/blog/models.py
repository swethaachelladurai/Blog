

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        ordering=('-date',)
    def __str(self):
        return self.title    

class Contact(models.Model):
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    description=models.TextField()
    def __str__(self):
        return self.title    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'         

