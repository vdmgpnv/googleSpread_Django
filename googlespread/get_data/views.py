from rest_framework.generics import ListAPIView
from .models import GetDataOrder
from .serializers import OrderSerializer


class OrderListView(ListAPIView):
    '''Контроллер-класс, который передает на фронт данные их модели'''
    queryset = GetDataOrder.objects.all()
    serializer_class = OrderSerializer
    
# Create your views here.
