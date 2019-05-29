from django.test import TestCase, Client
from ..models import Order, Type, AcademicLevel, Format
from django.urls import reverse
from django.contrib.auth.models import User




class OrderViewsTests(TestCase):

    def test_order_list_GET(self):




        self.list_url = reverse('order-list')

        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 302)



    def test_view_url_by_name(self):
        response = self.client.get(reverse('order-list'))
        self.assertEquals(response.status_code, 200)











