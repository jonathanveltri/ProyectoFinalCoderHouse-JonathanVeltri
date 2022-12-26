from django.urls import path
from django.contrib.auth.views import LogoutView
from home import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("about/", views.about, name="about"),
    path('login', views.login_required, name='login'),
    path('register', views.register, name='user-register'),
    path('register/update/', views.user_update, name='user-update'),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/change-password.html',
            success_url=reverse_lazy("home:password-change-done")
        ),
        name="password-change"
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='registration/change-password-done.html'
        ),
        name="password-change-done"
    ),
]
