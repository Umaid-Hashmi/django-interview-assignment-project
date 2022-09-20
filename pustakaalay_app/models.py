from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    is_librarian = models.BooleanField(default=False)

class Book(models.Model):
    borrower = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    book_id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=20)
