from django.urls import path
from .views import ListCategoriesView

app_name="apps.category"

urlpatterns = [
    path('categories/', ListCategoriesView.as_view())
]
