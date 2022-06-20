from rest_framework import serializers
from .models import GetDataOrder


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор для модели заказов, приводим дату к человеческому виду"""
    delivery_date = serializers.DateTimeField(format='%d.%m.%Y')
    class Meta:
        model = GetDataOrder
        fields = '__all__'