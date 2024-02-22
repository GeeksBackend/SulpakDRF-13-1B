from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.settings.models import Setting
from apps.settings.serializers import SettingSerializer

# Create your views here.
class SettingAPI(GenericViewSet,
                 mixins.ListModelMixin):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer