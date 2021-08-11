from django.db import models
from account.models import CustomUser

# Create your models here.
class Artist(models.Model):
    CATEGORY_CHOICES = [
        ("Boy Group", "Boy Group"),
        ("Girl Group", "Girl Group"),
        ("Rock Band", "Rock Band"),
        ("Hip-Hop", "Hip-Hop"),
        ("Etc", "Etc"),
    ]
    GROUP_CHOICES = [
        ("Solo", "Solo"),
        ("Duo", "Duo"),
        ("Trio", "Trio"),
        ("Quatro", "Quatro"),
        ("etc", "etc"),
    ]
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100, default="Solo", choices=GROUP_CHOICES)
    category = models.CharField(
        max_length=100, default="Boy Group", choices=CATEGORY_CHOICES
    )

    like_users = models.ManyToManyField(CustomUser, related_name="like_artists")
