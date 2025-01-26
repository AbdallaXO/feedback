from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "username": "Your Name",
            "rating": "Your Rating (1-5)",
            "review_text": "Your Feedback",
        }
        error_messages = {
            "username": {
                "required": "Please Enter your username",
                "max_length": "Name cannot exceed 20 characters",
            },
            "rating": {
                "required": "Please Enter A Rating From 1-5",
            },
            "review_text": {
                "required": "Please enter your feedback to submit the review",
            },
        }  # includes all fields except this if that was a field exlude = ['owner_comment']
