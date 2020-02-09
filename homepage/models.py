from django.conf import settings
from django.db import models
from django.utils import timezone
from enum import Enum

class Cities(Enum):
    HELSINKI = 'Helsinki'
    TURKU = 'Turku'

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    city = models.CharField(
        max_length=20, 
        choices=[(city.name, city.value) for city in Cities]
    )
    header_image = models.ImageField(upload_to='images/events/')
    host = models.ForeignKey(
        'Partner',
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Partner(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/partners/')
    gcc_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=60)
    is_board_member = models.BooleanField(default=False)
    role = models.CharField(max_length=100)
    bio = models.CharField(max_length=150)
    profile_picture = models.ImageField(upload_to='images/members/')
    city = models.CharField(
        max_length=20, 
        choices=[(city.name, city.value) for city in Cities]
    )
    
    def __str__(self):
        return self.name

class Value(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
