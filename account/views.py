from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import CreateView

from account.forms import RegistrationForm

User = get_user_model()


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('successful-registration')


class SuccessRegistrationView(View):
    def get(self, request):
        return render(request, 'account/success_registration.html', {})


# http://127.0.0.1:8000/account/activate/?u=2wad3r33r
class ActivationView(View):
    def get(self, request):
        code = request.GET.get('u')
        # try:
        #     user = User.objects.get(activation_code=code)
        # except User.DoesNotExist:
        #     raise Http404
        user = get_object_or_404(User, activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return render(request, 'account/activation.html', {})


clas
