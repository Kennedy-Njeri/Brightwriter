from django.test import TestCase, Client
from .models import Type, Order, AcademicLevel, Format
from django.contrib.auth.models import User



class UserTestCase(TestCase):

    def setUp(self):

        self.user = User.objects.create(
            username='author@test.com',
            email='author@test.com',
            password="30199278Ken"
        )

    def test_user_is_assigned_id_on_creation(self):
        self.assertEquals(self.user.id, 1)


class TypeTestCase(TestCase):

    def setUp(self):

        self.type = Type.objects.create(
            name="Theisis"
        )

    def test_type_is_assigned_id_on_creation(self):
        self.assertEquals(self.type.id, 1)

class FormatTestCase(TestCase):

    def setUp(self):

        self.format = Format.objects.create(

            name="CHICAGO"
        )

    def test_format_is_assigned_id_on_creation(self):
        self.assertEquals(self.format.id, 1)


class AcademicLevelTestCase(TestCase):

    def setUp(self):

        self.academic = AcademicLevel.objects.create(

            name="College",

        )

    def test_academic_is_assigned_id_on_creation(self):
        self.assertEquals(self.academic.id, 1)


class OrderModelTests(TestCase):

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

        self.order = Order.objects.create(
            username=self.user,
            type=self.type,
            academic=self.academic,
            topic="Networking",
            pages=4,
            urgency=3,
            format=self.format,
            instructions="Write in bold",
            pdf="server.pdf",
            total=6000,
            paid=False,
            email="kennedy@gmail.com",


        )

    def test_order_is_assigned_id_on_creation(self):
        self.assertEquals(self.order.id, 1)



    def total_cost_order(self):

        self.order = Order.objects.create(
            username=self.user,
            type=self.type,
            academic=self.academic,
            topic="Networking",
            pages=4,
            urgency=3,
            format=self.format,
            instructions="Write in bold",
            pdf="server.pdf",
            total=6000,
            paid=False,
            email="kennedy@gmail.com",

        )

        self.assertEquals(self.order.id.total_cost, 6000)











