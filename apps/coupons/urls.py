from django.urls import path
from .views import CheckCouponView

app_name="apps.coupons"

urlpatterns = [
    path('check-coupon', CheckCouponView.as_view()),
]
