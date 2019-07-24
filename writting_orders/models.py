from django.db import models
from django.contrib.auth.models import User
import datetime
from paypal.standard.ipn.signals import valid_ipn_received
from paypal.standard.models import ST_PP_COMPLETED
from tinymce import HTMLField


class AcademicLevel(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Format(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):

        return str(self.name)



class Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


PROCESS_CHOICES = (
    ("Processing", ("Processing")),
    ("Finished", ("Finished"))
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    academic = models.ForeignKey(AcademicLevel, on_delete=models.CASCADE, null=True)
    topic = models.CharField(max_length=30)
    pages = models.IntegerField(choices=list(zip(range(1, 10), range(1, 10))))
    urgency = models.IntegerField(choices=list(zip(range(1, 10), range(0, 10))), default=0)
    format = models.ForeignKey(Format, on_delete=models.CASCADE, null=True)
    instructions = HTMLField(null=True)
    pdf = models.FileField(upload_to='uploads/pdfs', null=True, blank=True)
    total = models.DecimalField(verbose_name="Total", max_digits=10, decimal_places=2, null=True)
    paid = models.BooleanField(default=False)
    email = models.EmailField(null=True)
    process = models.CharField(max_length=12, choices=PROCESS_CHOICES, default='Processing')


    def show_me_the_money(sender, **kwargs):
        ipn_obj = sender
        if ipn_obj.payment_status == ST_PP_COMPLETED:
            # Undertake some action depending upon `ipn_obj`.

           return Order.objects.update(paid=True)

        else:

            return Order.objects.update(paid=False)



    valid_ipn_received.connect(show_me_the_money)





    @property
    def total_cost(self):

        if self.urgency <= 1:
            rate = 2500

        elif self.urgency >= 1 and self.urgency <= 3:
            rate = 2000

        elif self.urgency >= 3 and self.urgency <= 5:
            rate = 1500

        elif self.urgency >= 5 and self.urgency <= 7:
            rate = 1000

        elif self.urgency >= 7 and self.urgency <= 9:
            rate = 500

        return (self.pages) * rate


    def save(self, *args, **kwargs):
        self.total = self.total_cost
        super(Order, self).save(*args, **kwargs)




    class Meta:

        ordering = ['id']



    def __str__(self):

        return str(self.user)












