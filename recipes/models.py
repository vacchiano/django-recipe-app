from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()

  author = models.ForeignKey(User, on_delete=models.CASCADE)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title