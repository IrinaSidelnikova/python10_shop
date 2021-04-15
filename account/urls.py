from django.urls import path

from account.views import RegistrationView, SuccessRegistrationView, ActivationView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('successful_registration/', SuccessRegistrationView.as_view(), name='successful-registration'),
    path('activation/', ActivationView.as_view(), name='activation')
]
