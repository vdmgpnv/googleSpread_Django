from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import GetDataOrder
from .serializers import OrderSerializer








class OrderListView(ListAPIView):
    queryset = GetDataOrder.objects.all()
    serializer_class = OrderSerializer
    
# Create your views here.
