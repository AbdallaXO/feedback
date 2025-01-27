from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from .models import UserProfile
from django.views.generic import ListView

# Create your views here.


class CreateProfileViews(CreateView):
    model = UserProfile
    template_name = "profiles/create_profile.html"
    fields = "__all__"
    success_url = "/profiles"


class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profile.html"
    context_object_name = "profiles"
