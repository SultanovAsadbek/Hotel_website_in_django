# --- home page --.
from index_app.views import home
from index_app.views import feedback
from django.urls import path


urlpatterns = [
    path("", home, name="home"),
    path("feedback/", feedback, name="feedback"),
]
