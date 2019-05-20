from django.test import TestCase, Client
from ..models import Order, Type, AcademicLevel, Format
from django.urls import reverse
from django.contrib.auth.models import User




class OrderViewsTests(TestCase):

    def setUp(self):


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

        self.order1 = Order.objects.create(

            username=self.user,
            type=self.type,
            academic=self.academic,
            topic="Networking",
            pages=4,
            urgency=3,
            format=self.format,
            instructions="Write in bold",
            pdf="server.pdf",
            total=8000,
            paid=False,
            email="kennedy@gmail.com",

        )

    




