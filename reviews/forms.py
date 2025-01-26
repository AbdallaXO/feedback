from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(
        label="Your Name",
        max_length=20,
        error_messages={
            "required": "type ur name bitch",
            "max_length": "Maximum 20 Characters",
        },
    )
    review_text = forms.CharField(
        label="Your Feedback", widget=forms.Textarea, max_length=200
    )
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
