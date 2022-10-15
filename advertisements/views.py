from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement, AdvertisementFilter
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated(), IsOwner()]
        return []
