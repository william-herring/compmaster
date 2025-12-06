from django.shortcuts import render
from django.views.generic import TemplateView

class SignInPageView(TemplateView):
    template_name = "sign-in.html"
