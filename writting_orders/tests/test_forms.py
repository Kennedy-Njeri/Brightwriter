
from django.test import TestCase

from writting_orders.forms import OrderCreateForm, RegistrationForm
from ..models import AcademicLevel, Type, Format




class TestForms(TestCase):



    def setUp(self):

        AcademicLevel.objects.create(

            name="College",

        )

        Type.objects.create(

            name="Theisis",

        )

        Format.objects.create(

            name="Chicago",

        )



    def test_order_form_valid_data(self):


        academic = AcademicLevel.objects.get(name="College")

        type = Type.objects.get(name="Theisis")

        format = Format.objects.get(name="Chicago")

        form = OrderCreateForm(data={

            'username': 'kennedy',
            'type': type.pk,
            'academic': academic.pk,
            'topic': 'Networking',
            'pages': 4,
            'urgency': 3,
            'format': format.pk,
            'instructions': 'write in bold',
            'pdf': 'server.pdf',
            'email': 'mistakenz@gmail.com'


        })




        self.assertTrue(form.is_valid(), form.errors)



    def test_expense_form_no_data(self):

        form = OrderCreateForm(data={})

        self.assertFalse(form.is_valid(), form.errors)

    def test_registration_form(self):
        # test invalid data
        invalid_data = {
            "username": "user@test.com",
            "email": "vin",
            "password1": "30199278Joy",
            "password2": "30199278Kev"
        }
        form = RegistrationForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

        # test valid data
        valid_data = {
            "username": "Kennedy",
            "email": "kennedy@gmail.com",
            "password1": "30199278Joy",
            "password2": "30199278Joy"
        }
        form = RegistrationForm(data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)