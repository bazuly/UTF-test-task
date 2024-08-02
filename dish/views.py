from rest_framework.views import APIView
from .models import FoodCategory
from .serializers import FoodListSerializer, FoodSerializer
from rest_framework import status
from rest_framework.response import Response


class FoodCategoryListView(APIView):
    def get(self, *args, **kwargs):
        categories = FoodCategory.objects.filter(food__is_publish=True).distinct()
        data = []
        for category in categories:
            foods = category.food.filter(is_publish=True)
            if foods.exists():
                category_data = FoodListSerializer(category).data
                category_data["foods"] = FoodSerializer(foods, many=True).data
                data.append(category_data)
        return Response(data, status=status.HTTP_200_OK)
