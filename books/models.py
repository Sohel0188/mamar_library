from django.db import models
from category.models import Category
from accounts.models import UserAccount
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    qunatity = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='media/images', blank=True, null=True)
    def __str__(self):
        return self.title
    
    
            

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Reviewed by {self.name}"
    
class BorrowedBooks(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='buybook')
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    is_returned = models.BooleanField(default=False)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Borrowed {self.book.title} by {self.user.user.username} "