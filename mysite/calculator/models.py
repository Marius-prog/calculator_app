import datetime
from django.db import models
from django.utils import timezone
# from django.utils.timezone import


class Calculator(models.Model):
    id = models.CharField(max_length=(100), primary_key=True)
    name = models.CharField(max_length=50)
    num1 = models.CharField(max_length=100)
    num2 = models.CharField(max_length=100)
    operation = models.CharField(max_length=2)
    result = models.CharField(max_length=100)

    def __str__(self):
        return self.id

    def was_added_recently(self):
        return self.pub_date >= datetime.timezone.now() - datetime.timedelta(days=1)