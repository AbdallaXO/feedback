from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length=20)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review_text = models.TextField()

    def __str__(self):
        return f"Review by {self.username}: {self.rating}/5 - {self.review_text[:50]}..."

    class Meta:
        verbose_name_plural = "Review's"

    def get_absolute_url(self):
        return reverse("review", args=[self.pk])
