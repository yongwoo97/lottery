from django.db import models

# Create your models here.
class LotteryNumber(models.Model):
    date = models.DateTimeField()
    number = models.IntegerField(primary_key=True, null=False, blank=False)
    n1 = models.IntegerField(null=False)
    n2 = models.IntegerField(null=False)
    n3 = models.IntegerField(null=False)
    n4 = models.IntegerField(null=False)
    n5 = models.IntegerField(null=False)
    n6 = models.IntegerField(null=False)
    n7 = models.IntegerField(null=False)
