from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Advisors_DB(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    adv_name = models.CharField(max_length=40)
    adv_id = models.CharField(max_length=40, primary_key=True)
    adv_pic = models.ImageField()

    def __str__(self):
        return self.adv_id

class Booking_DB(models.Model):
    # user = models.OneToOneField(Advisors_DB, on_delete=models.CASCADE)
    advisor = models.ForeignKey(Advisors_DB, on_delete=models.CASCADE)
    booking_id = models.CharField(max_length=40, primary_key=True)
    # booking_time = models.DateTimeField(auto_now=True)
    # schedule_time = models.DateTimeField()
    # booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_time= models.DateTimeField()

    # def __str__(self):
    #     return self.booked_by.first_name
    # @property
    # def get_name(self):
    #     return self.user.first_name