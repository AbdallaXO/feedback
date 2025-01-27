from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you/", views.ThankYouView.as_view(), name="thank-you"),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("review/<int:pk>/", views.SingleReviewView.as_view(), name="review"),
    path("review/update/<int:pk>/", views.UpdateForm.as_view(), name="update_review"
    ),  # Add this line
]
