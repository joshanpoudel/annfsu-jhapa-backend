from django.urls import path

from team.views import OurTeamView

urlpatterns = [
    path("", OurTeamView.as_view(), name="our_team")
]