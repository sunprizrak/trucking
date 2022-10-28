from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from claims.forms import ShippingClaimForm


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
