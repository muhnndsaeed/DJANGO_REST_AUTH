from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title= models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




