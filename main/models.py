from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
  name = models.CharField(max_length=30, null=False, blank=False)

  def __str__(self):
    return self.name

class Post(models.Model):
  title = models.CharField(max_length=100)
  # author = models.CharField(max_length=50)
  author = models.ForeignKey(User, null=False, blank=False, on_delete = models.CASCADE)
  body = models.TextField()
  category = models.CharField(max_length=20)
  image = models.ImageField(upload_to="post_images/", blank=True, null=True)
  tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
  like = models.ManyToManyField(User, related_name='likes', blank=True)
  like_count = models.PositiveBigIntegerField(default=0)

  def __str__(self):
    return self.title
  
  def summary(self):
    return self.body[:10]
  
class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)

    def str (self):
      return self.blog.title + " : " + self.content[:20] + "by" + self.author.profile.nicknam