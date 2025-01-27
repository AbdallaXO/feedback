from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


from .forms import ReviewForm
from .models import Review

class UpdateForm(UpdateView):
    model = Review
    fields = ["rating"]
    success_url = reverse_lazy('thank-you')

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_form.html"
    success_url = "thank-you"


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
        return query.order_by("rating")


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
