from django.urls import path
from users.views import register, register_thanks, update, help_update, update_success, show
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView


urlpatterns = [
    path("register", register, name="register"),
    path("register/thanks", register_thanks, name="register_thanks"),
    path("login", LoginView.as_view(
        template_name="users/login.html"
    ), name="login"),
    path("logout", LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("update/<int:user_id>", update, name="update"),
    path("help_update", help_update, name="help_update"),
    path("update_success", update_success, name="update_success"),
    path("show/<int:id>", show, name="show"),

]
