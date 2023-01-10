from statistics import mode
from django.db import models
from django.conf import settings
import random as rand

User = settings.AUTH_USER_MODEL

# Create your models here.
class Tweet(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 1 user can have many tweets, 1 tweet is only by 1 user
    content = models.TextField(blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='images/')

    class Meta:
        ordering = ["-id"]
        
    def serialize(self):
        return {
            "id" : self.id, 
            "content" : self.content, 
            "likes": rand.randint(0, 200)
        }

