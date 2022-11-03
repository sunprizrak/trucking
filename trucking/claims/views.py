from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from claims.forms import ShippingClaimForm, StaticDeclarationForm, ImportDeclarationForm


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
        messages.success(self.request, 'Завка на перевозку оформлена успешно!')
        return super(ShippingClaimView, self).form_valid(form)


class StaticDeclarationView(FormView):
    form_class = StaticDeclarationForm
    template_name = 'claims/static_declaration.html'
    success_url = reverse_lazy('static_declaration')
    extra_context = {
        'title': 'Оформление статической декларации',
    }

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        messages.success(self.request, 'Статическая декларация успешно оформлена!')
        return super(StaticDeclarationView, self).form_valid(form)
    

class ImportDeclarationView(FormView):
    form_class = ImportDeclarationForm
    template_name = 'claims/import_declaration.html'
    success_url = reverse_lazy('import_declaration')
    extra_context = {
        'title': 'Оформление импортной декларации',
    }

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        messages.success(self.request, 'Импортная декларация успешно оформлена!')
        return super(ImportDeclarationView, self).form_valid(form)