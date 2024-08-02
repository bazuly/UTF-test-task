# urls.py
from django.urls import path
from .views import FoodCategoryListView

urlpatterns = [
    path("v1/foods/", FoodCategoryListView.as_view(), name="food-category-list"),
]
