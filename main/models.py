from django.db import models
from datetime import datetime


class Email(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)
    sent_at = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.name} --> {self.email} -- > {self.sent_at}'


class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name