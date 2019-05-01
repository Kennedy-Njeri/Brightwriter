from django.shortcuts import render

from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from writting_orders.models import Order
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import get_object_or_404

from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver


@csrf_exempt
def payment_done(request):
    return render(request, 'done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request, 'canceled.html')


@csrf_exempt
def payment_process(request):
    return render(request, 'process.html')



def payment_process(request, pk):



    order = get_object_or_404(Order, pk=pk)

    host = request.get_host()

    paypal_dict = {
      'business': settings.PAYPAL_RECEIVER_EMAIL ,
      'amount': order.total,
      'item_name': 'Order {}'.format(order.topic),
      'invoice': str(order.id),
      'currency_code': 'USD',
      'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
      'return_url': 'http://{}{}'.format(host, reverse('done')),
      'cancel_return': 'http://{}{}'.format(host, reverse('canceled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)

    return render(request, 'process.html', {'form': form, order: order})





@receiver(valid_ipn_received)
def payment_notification(order, **kwargs):
    ipn = order
    if ipn.payment_status == 'Completed':
        # payment was successful
        order = get_object_or_404(Order, id=ipn.invoice)

        if order.total == ipn.mc_gross:
            # mark the order as paid
            order.paid = True
            order.save()