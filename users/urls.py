from django.urls import path
from users.views import register, register_thanks ,login
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register", register, name="register"),
    path("register/thanks", register_thanks, name="register_thanks"),
    path("login", login, name="login"),
    path("logout", LogoutView.as_view(template_name="users/logout.html"), name="logout")
]
