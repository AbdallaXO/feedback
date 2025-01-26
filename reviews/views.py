from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import ReviewForm
from .models import Review


# Create your views here.
"""Will validate input and make sure its not empty
    and make sure form is valid as a whole, if data is valid it will make another field
    with the valid data"""


def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            entry = Review.objects.create(rating = request.POST['rating'], username = request.POST['username'],
            review_text = request.POST['review_text'])
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
    return render(request, "reviews/review.html", {"form": form})


def thank_you(request):
    return render(request, "reviews/thank_you.html")
