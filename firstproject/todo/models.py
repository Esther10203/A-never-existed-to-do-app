from django.utils import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
   title = models.CharField(max_length=200)
   task = models.CharField(max_length=200)
   created_date = models.DateTimeField(default=timezone.now)

   def __str__(self):
      return self.title