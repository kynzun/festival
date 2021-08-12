from django.db import models
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
