from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Message(models.Model):
    emisor = models.CharField(max_length=1000)
    receptor = models.CharField(max_length=1000)
    text = models.CharField(max_length=64)
    date = models.DateTimeField(default=datetime.now, blank=True)
   
    def __str__(self):
        return self.text
