from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import UserEditForm
from claims.forms import ShippingClaimForm


class ProfileView(FormView):
    form_class = UserEditForm
    template_name = 'custom_users/profile.html'
    success_url = reverse_lazy('profile')
    extra_context = {
        'title': 'Профиль компании',
    }

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = {
            "initial": self.get_initial(),
            "prefix": self.get_prefix(),
        }

        if self.request.method in ("POST", "PUT"):
            kwargs.update(
                {
                    "data": self.request.POST,
                    "files": self.request.FILES,
                    "instance": self.request.user,
                }
            )
        elif self.request.method == "GET":
            kwargs.update(
                {
                    "instance": self.request.user,
                }
            )
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(ProfileView, self).form_valid(form)


class ShippingClaimView(FormView):
    form_class = ShippingClaimForm
    template_name = 'claims/shipping_claim.html'
    success_url = reverse_lazy('shipping_claim')
    extra_context = {
        'title': 'Оформление заявки на перевозку',
    }

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return super(ShippingClaimView, self).form_valid(form)


def logout_user(request):
    logout(request)
    return redirect('home')




