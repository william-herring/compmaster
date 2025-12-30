from django.contrib import admin
from django.urls import path, include
from system.views import ErrorView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('sign-in/', include('accounts.urls')),
    path('error', ErrorView.as_view()),
]
