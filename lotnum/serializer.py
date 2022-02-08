from rest_framework import serializers
from .models import LotteryNumber

class NumSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotteryNumber
        fields = '__all__'


