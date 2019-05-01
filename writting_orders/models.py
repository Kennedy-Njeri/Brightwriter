from django.db import models
from django.contrib.auth.models import User
import datetime



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


class Order(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    academic = models.ForeignKey(AcademicLevel, on_delete=models.CASCADE, null=True)
    topic = models.CharField(max_length=30)
    pages = models.IntegerField(choices=list(zip(range(1, 10), range(1, 10))))
    urgency = models.IntegerField(choices=list(zip(range(1, 10), range(0, 10))), default=0)
    format = models.ForeignKey(Format, on_delete=models.CASCADE, null=True)
    instructions = models.TextField(max_length=200, null=True)
    pdf = models.FileField(upload_to='uploads/pdfs', null=True, blank=True)
    total = models.DecimalField(verbose_name="Total", max_digits=10, decimal_places=2, null=True)
    paid = models.BooleanField(default=False)

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


    def __str__(self):

        return str(self.user)










