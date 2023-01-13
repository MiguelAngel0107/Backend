from django.urls import path
from .views import GetShippingView

app_name="apps.shipping"

urlpatterns = [
    path('get-shipping-options', GetShippingView.as_view()),
]
