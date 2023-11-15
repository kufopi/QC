from django.urls import path
from .views import PublicationCreateView
from . import views

urlpatterns = [
    path("m", views.update_staff, name="modric"),
    path("journal/", views.journal, name="journal"),
    path("conference/", views.conference, name="conference"),
    path("book/", views.book, name="book"),
    path("promo/", views.promo, name="promotion"),
    path("seek/", views.seeker, name="seek"),
    path("", views.update_staff, name="update_staff"),
    path("publication/", PublicationCreateView.as_view(), name="pub"),
    path("register/", views.register, name="register"),
    path("end/", views.endpage, name="endpage"),
    path("profile/", views.profile, name="profile"),
]