from django.test import TestCase, Client
from ..models import Order, Type, AcademicLevel, Format
from django.urls import reverse
from django.contrib.auth.models import User




class OrderViewsTests(TestCase):

    def setUp(self):

        self.client = Client()


        self.user = User.objects.create(
            username='author@test.com',
            email='author@test.com',
            password="30199278Ken"
        )

        self.type = Type.objects.create(
            name="Theisis"
        )

        self.academic = AcademicLevel.objects.create(

            name="College",

        )

        self.format = Format.objects.create(

            name="CHICAGO"
        )


    def test_order_create_POST(self):

        url = reverse('order-create')


        

        order = Order.objects.get(id=3)

        self.assertEquals(order.username, 'kennedy')
















