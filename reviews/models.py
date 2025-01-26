from django.db import models


# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length=20)
    rating = models.IntegerField()
    review_text = models.TextField()

    class Meta:
        verbose_name_plural = "Review's"
