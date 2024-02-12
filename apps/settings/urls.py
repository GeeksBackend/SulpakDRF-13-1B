from django.urls import path 

from apps.settings.views import SettingAPI

urlpatterns = [
    path('', SettingAPI.as_view(), name="api_setting")
]
