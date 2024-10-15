from django.db import models
from django.contrib.auth.models import User

class Post_Band(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200) # Band 이름
    create_date = models.DateTimeField()