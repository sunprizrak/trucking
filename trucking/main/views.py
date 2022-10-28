from django.http import JsonResponse
from django.views.generic import FormView

from claims.forms import PreliminaryClaimForm


class HomeView(FormView):
    form_class = PreliminaryClaimForm
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Главная страница',
    }

    def form_invalid(self, form):
        data = {'result': 'captcha'}
        return JsonResponse(data)

    def form_valid(self, form):
        form.save()
        data = {'result': True}
        return JsonResponse(data)
