from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  nickname = models.TextField(max_length=10)
  major = models.TextField(null=True, max_length=30)
  phone_number = models.TextField(max_length=13)  # 전화번호 (대시 포함 13글자)
  intro = models.TextField(max_length=200, null=True)  # 자기소개