
from django.urls import path
from . import views


urlpatterns = [


    path('<int:pk>', views.payment_process, name="process"),
    path('done/', views.payment_done, name="done"),
    path('canceled/', views.payment_canceled, name="canceled"),






]