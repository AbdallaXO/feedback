from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .forms import ReviewForm
from .models import Review


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review_form.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review_form.html", {"form": form})


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Test"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_detail.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        query = super().get_queryset()
        return query.order_by("rating").filter(rating__lte=3)


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review 