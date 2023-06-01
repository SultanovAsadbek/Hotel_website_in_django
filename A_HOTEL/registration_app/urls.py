from django.urls import path


# --- registration, authorization and logout users. ---
from registration_app.views import register
from registration_app.views import loginUser
from registration_app.views import logoutUser
from registration_app.views import profile

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", loginUser, name="login"),
    path("logout/", logoutUser, name="logout"),
    path("profile/", profile, name="profile"),
]