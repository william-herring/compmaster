import json
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View

class SignInPageView(TemplateView):
    template_name = "sign-in.html"

class UserSignIn(View):
    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        print(code)
        redirect_url = request.GET.get('url')
        return redirect(redirect_url)