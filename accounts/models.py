from django.db import models
from django.contrib.auth.models import User 
from .constants import GENDER

# Create your models here.
class UserAccount (models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_id = models.IntegerField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    
    def __str__(self):
        return str(self.account_id)
    

