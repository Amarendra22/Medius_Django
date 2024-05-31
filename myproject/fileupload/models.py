from django.db import models

class uFile(models.Model):
    date = models.DateField()
    accno = models.CharField(max_length=50)
    custState = models.CharField(max_length=50)
    custPin = models.PositiveBigIntegerField()
    dpd = models.IntegerField()

    def __str__(self):
        return f"State: {self.custState}, DPD: {self.dpd}"