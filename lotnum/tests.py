from django.test import TestCase

# Create your tests here.
from datetime import datetime

current_time = datetime.now()

standard = datetime.strptime("2022-02-01 19:50:00", "%Y-%m-%d %H:%M:%S")


dif = current_time-standard
print(dif.days)
print(dif.seconds)