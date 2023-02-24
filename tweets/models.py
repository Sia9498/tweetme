from statistics import mode
from django.db import models
from django.conf import settings
import random as rand
from django.db.models import Q

User = settings.AUTH_USER_MODEL

# Create your models here.
class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class TweetQuerySet(models.QuerySet):
    def by_username(self, username):
        return self.filter(user__username__iexact=username)

    def feed(self, user):
        profiles_exist = user.following.exists()
        followed_users_id = []
        if profiles_exist:
            followed_users_id = user.following.values_list("user__id", flat=True)

        return self.filter(Q(user__id__in=followed_users_id) | Q(user=user)).distinct().order_by("-timestamp")

class TweetManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return TweetQuerySet(self.model, using=self._db)

    def feed(self, user):
        return self.get_queryset().feed(user)

class Tweet(models.Model):
    # id = models.AutoField(primary_key=True)

    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)   # retweet logic
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets') # 1 user can have many tweets, 1 tweet is only by 1 user
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='images/')
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = TweetManager()

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

