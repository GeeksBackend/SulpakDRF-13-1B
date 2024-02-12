from rest_framework.generics import ListAPIView

from apps.settings.models import Setting
from apps.settings.serializers import SettingSerializer

# Create your views here.
class SettingAPI(ListAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer