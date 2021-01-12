from django.db import models

# Create your models here.
class contact(models.Model):
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank = True)
    message_date = models.DateTimeField()
