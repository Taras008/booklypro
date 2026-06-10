from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        CLIENT = "client", "Client"
        OWNER = "owner", "Owner"
        STAFF = "staff", "Staff"

    role = models.CharField(max_length=20, choices=Role.choices , default=Role.CLIENT)
    
    def __str__(self):
        return self.username
    


