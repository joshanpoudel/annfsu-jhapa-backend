from django.urls import path

from .views import BloodDonorView, BloodRequestView

urlpatterns = [
    path("", BloodDonorView.as_view(), name="blood_donors"),
    path("request/", BloodRequestView.as_view(), name="blood_request"),
]
