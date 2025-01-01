from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    provinsi_choices = [
        ('JT', 'Jawa Tengah'),
        ('JB', 'Jawa Barat'),
        ('JT', 'Jawa Timur'),
    ]
    gender_choices = [
        ('P', 'Pria'),
        ('W', 'Wanita')
    ]

    avatar = models.ImageField(null=True, default="avatar.svg")
    email = models.EmailField(unique=True, null=True)
    gender = models.CharField(max_length=2, choices=gender_choices, null=True)
    provinsi = models.CharField(max_length=2, choices=provinsi_choices, null=True)
    tanggal_lahir = models.DateField(null=True)
    studi_industri = models.CharField(max_length=200, null=True)
    bio = models.TextField(null=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

