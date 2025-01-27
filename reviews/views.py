from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy


from .forms import ReviewForm
from .models import Review


class UpdateForm(UpdateView):
    model = Review
    fields = ["rating"]
    success_url = reverse_lazy("thank-you")


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
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get('favorite_review')
        context['is_favorite'] =  favorite_id == str(loaded_review.id)
        return context


class AddFavoriteView(View):
    def post(self, request):
         review_id = request.POST['review_id']
         request.session['favorite_review'] = review_id
         return HttpResponseRedirect(reverse('review', args=[review_id]))
    
"""Note, the Review_ID always gets stored as a STRING so when u referrence it
convert other comparison to str or convert it to int"""