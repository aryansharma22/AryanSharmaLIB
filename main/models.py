from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    role = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text   

class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    Books = models.ForeignKey(Books, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text 

       