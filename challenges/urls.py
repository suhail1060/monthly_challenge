from django.urls import path

from . import views
# creating list of patterns

urlpatterns = [
    path("<int:month>", views.monthly_challenge_numbers),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
    path("", views.display_list,name="index")
]
