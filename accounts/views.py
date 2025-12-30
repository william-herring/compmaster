import json
from django.contrib.auth import login
from dotenv import load_dotenv
import os
import requests
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import User

class SignInPageView(TemplateView):
    template_name = "sign-in.html"

class UserSignIn(View):
    def get(self, request, *args, **kwargs):
        load_dotenv()

        code = request.GET.get('code')
        redirect_url = request.GET.get('url')

        token_res = requests.post(
            f'{os.getenv('WCA_URL')}/oauth/token',
            headers={'Content-Type': 'application/json'},
            params={
                'grant_type': 'authorization_code',
                'code': code,
                'client_id': os.getenv('WCA_CLIENT_ID'),
                'client_secret': os.getenv('WCA_CLIENT_SECRET'),
                'redirect_uri': f'{os.getenv('BASE_URL')}/sign-in/redirect?url={redirect_url}'
            }
        )

        if token_res.status_code != 200:
            return redirect(f'/error?c={token_res.status_code}&msg=Something went wrong.')

        token = token_res.json()['access_token']

        user_res = requests.get(os.getenv('BASE_URL') + os.getenv('LOAD_WCA_ME_RESPONSE'), headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        })

        user_data = user_res.json()['me']

        user = User.objects.filter(wca_id=user_data['wca_id']).first()
        if user is not None:
            login(request, user)
        else:
            user = User(
                wca_id=user_data['wca_id'],
                name=user_data['name'],
                is_delegate=user_data['delegate_status'] is not None,
                profile_picture=user_data['avatar']['thumb_url']
            )
            user.set_unusable_password()
            user.save()

            login(request, user)

        return redirect(redirect_url)
