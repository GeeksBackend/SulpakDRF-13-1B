from django.urls import path 

from apps.categories.views import CategoryListAPI

urlpatterns = [
    path('', CategoryListAPI.as_view(), name="api_categories")
]