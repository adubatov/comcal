from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bx_user_id = models.IntegerField(blank=True, null=True)
    is_staff = models.BooleanField()
    

