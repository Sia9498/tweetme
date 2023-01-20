from statistics import mode
from django.db import models
from django.conf import settings
import random as rand

User = settings.AUTH_USER_MODEL

# Create your models here.
class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):
    # id = models.AutoField(primary_key=True)

    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)   # retweet logic
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 1 user can have many tweets, 1 tweet is only by 1 user
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='images/')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]

    @property
    def is_retweet(self):
        return self.parent != None

    def serialize(self):
        '''
        no longer needed, can be deleted
        '''
        return {
            "id" : self.id, 
            "content" : self.content, 
            "likes": rand.randint(0, 200)
        }

