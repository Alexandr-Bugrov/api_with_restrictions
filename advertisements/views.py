from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []
