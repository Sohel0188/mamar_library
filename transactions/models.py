from django.db import models
from accounts.models import UserAccount
from books.models import Book
# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(default=0,  max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=100, blank=True, null=True )
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction by {self.user.user.username} "