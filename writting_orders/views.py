from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)

from .models import User
from django.contrib import messages
from .forms import RegistrationForm
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Order
from .tasks import order_created
from django.contrib.messages.views import SuccessMessageMixin
from .forms import OrderCreateForm

# Create your views here.


class Index(TemplateView):

    template_name = 'index.html'




"""Controls the register module"""
def register(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')

            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')

    else:

        form = RegistrationForm()


    return render(request, 'register.html', {'form': form})



def account(request):

    return render(request, 'account.html')



#class OrderCreateView(SuccessMessageMixin, CreateView):
    #model = Order
    #fields = ('type', 'academic', 'topic', 'pages', 'format', 'urgency', 'instructions', 'pdf',)
    #success_url = reverse_lazy('order-list')
    #template_name = 'create-order.html'
    #success_message = 'Your Order has Been successfully '



   # def form_valid(self, form):

        #form.instance.user = self.request.user

        #return super().form_valid(form)




class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'
    paginate_by = 10


    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)



def order_create(request):

    if request.method == 'POST':

        form = OrderCreateForm(request.POST, request.FILES)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order = form.save()

            order_created.delay(order.id)

            return redirect('order-list')

            #return render(request, 'order-list', )

    else:

        form = OrderCreateForm()

    return render(request, 'create-order.html', {'form': form})