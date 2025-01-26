from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("review/<int:pk>/", views.SingleReviewView.as_view(), name="review"),
]
