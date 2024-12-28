from django.urls import path

from .views import BloodDonorView

urlpatterns = [path("", BloodDonorView.as_view(), name="blood_donors")]
