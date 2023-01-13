from django.urls import path
from .views import ListOrdersView, ListOrderDetailView

app_name="apps.orders"

urlpatterns = [
    path('get-orders', ListOrdersView.as_view()),
    path('get-order/<transactionId>', ListOrderDetailView.as_view()),
]
