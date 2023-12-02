import stripe
from http import HTTPStatus
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from orders.forms import OrderForm
from orders.models import Order
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

class SuccessTemplateView(TemplateView):
    template_name = 'orders/success.html'


class CancelTemplateView(TemplateView):
    template_name = 'orders/cancel.html'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order-create.html'
    success_url = reverse_lazy('order_create')



    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1OIvBtLMnrYSg46p2mPLpqNR',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('order_success')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('order_cancel'))
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)
    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)
    