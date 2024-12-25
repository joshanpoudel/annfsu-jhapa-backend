from django.urls import path
from .views import MembersView


urlpatterns = [path("", MembersView.as_view(), name="members")]
