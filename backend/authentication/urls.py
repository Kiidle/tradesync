from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", views.sign_in, name="login"),
    path("logout/", views.logout, name="logout"),
]