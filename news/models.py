from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

    def rate_update(self):
        self.rate = 0
        for e in list(Post.objects.filter(author=self.id).values('rate')):
            self.rate += int(e)
        self.rate *= 3
        for e in list(Comment.objects.filter(author=self.id).values('rate')):
            self.rate += int(e)
        for i in Post.objects.filter(author=self.id):
            for e in list(Comment.objects.filter(post=i).values('rate')):
                self.rate += int(e)


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    article = "art"
    news = "nws"
    POSTS = [
        (article, "Статья"),
        (news, "Новость")
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    post = models.CharField(max_length=3, choices=POSTS, default=news)
    time_post = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(Category, through='PostCategory')
    text = models.TextField()
    rate = models.IntegerField(default=0)

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()

    def preview(self):
        prev = self.text[0:125]+"..."
        return prev


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    rate = models.IntegerField(default=0)

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()



