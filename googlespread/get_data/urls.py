from django.urls import path
from .views import OrderListView



urlpatterns = [
    path('get_order_data/', OrderListView.as_view())
]
