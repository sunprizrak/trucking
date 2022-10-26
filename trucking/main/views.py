from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin

from claims.forms import PreliminaryClaimForm


class HomeView(FormMixin, TemplateView):
    form_class = PreliminaryClaimForm
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Главная страница',
    }

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        data = {'result': True}
        return JsonResponse(data)

    def form_invalid(self, form):
        data = {'result': 'captcha'}
        return JsonResponse(data)
