from django.urls import path

from orders.views import (CanceledTemplateView, OrderDetail, OrderListView,
                          SuccessTemplateView, my_webhook_handler,
                          order_create)

app_name = 'orders'

urlpatterns = [
    path('order-create/', order_create, name='order_create'),
    path('order-success/', SuccessTemplateView.as_view(), name='order_success'),
    path('order-canceled/', CanceledTemplateView.as_view(), name='order_canceled'),
    path('', OrderListView.as_view(), name='orders_list'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='order'),
    path('notification/', my_webhook_handler, name='notification'),
]
