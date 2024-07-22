from django.db import models




# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    
    def __str__(self):
        return self.name
    

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
    
#This signal create authtoken for users
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_authToken(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)