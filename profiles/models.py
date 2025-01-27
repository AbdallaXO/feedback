from django.db import models


# Create your models here.
class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    image = models.FileField(upload_to="images")
