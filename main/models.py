from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  # author = models.CharField(max_length=50)
  author = models.ForeignKey(User, on_delete = models.CASCADE)
  body = models.TextField()
  category = models.CharField(max_length=20)
  image = models.ImageField(upload_to="post_images/", blank=True, null=True)

  def __str__(self):
    return self.title
  
  def summary(self):
    return self.body[:10]