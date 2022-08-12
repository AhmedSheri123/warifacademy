from django.db import models
import datetime
# Create your models here.

class Users(models.Model):
    username = models.CharField(verbose_name="اسم المستخدم", max_length=100)
    email = models.EmailField(verbose_name="ايميل", max_length=254)

    
    def __str__(self):
        return self.username
    
    
class Password(models.Model):
    password = models.CharField(max_length=250)
    is_enabled = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
        return self.password