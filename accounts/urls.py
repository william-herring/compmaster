from django.urls import path
from .views import SignInPageView, UserSignIn

urlpatterns = [
    path('', SignInPageView.as_view()),
    path('redirect', UserSignIn.as_view())
]