from django.db import models
from django.db.models.fields.related import OneToOneField
from account.models import CustomUser

# Create your models here.


class Artist(models.Model):
    CATEGORY_CHOICES = [
        ("남자 아이돌", "남자 아이돌"),
        ("여자 아이돌", "여자 아이돌"),
        ("힙합", "랩/힙합"),
        ("인디음악", "인디음악"),
        ("발라드", "발라드"),
        ("락밴드", "락밴드"),
    ]
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100, null=True)
    image_back_url = models.CharField(max_length=100, null=True)
    category = models.CharField(
        max_length=100, default="Boy Group", choices=CATEGORY_CHOICES
    )
    desc = models.CharField(max_length=200, null=True)

    like_users = models.ManyToManyField(
        CustomUser, related_name="like_artists", blank=True
    )

    def __str__(self):
        return self.name


class Comment(models.Model):
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="comments",
    )
    text = models.TextField()

    def __str__(self):
        return (self.author.username if self.author else "무명") + "의 댓글"
