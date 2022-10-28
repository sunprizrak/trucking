from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib import messages

from .forms import UserEditForm


class ProfileView(FormView):
    form_class = UserEditForm
    template_name = 'custom_users/profile.html'
    success_url = reverse_lazy('profile')
    extra_context = {
        'title': 'Профиль организации',
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
        messages.success(self.request, 'Профиль организации успешно обновлён!')
        return super(ProfileView, self).form_valid(form)


def logout_user(request):
    logout(request)
    return redirect('home')




