from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.permissions import IsOwner

from django_filters.rest_framework import DjangoFilterBackend
from advertisements.filters import AdvertisementFilter

class AdvertisementViewSet(ModelViewSet):
	"""ViewSet для объявлений."""

	# TODO: настройте ViewSet, укажите атрибуты для кверисета,
	#   сериализаторов и фильтров

	queryset = Advertisement.objects.all()
	serializer_class = AdvertisementSerializer

	filter_backends = [DjangoFilterBackend]
	filterset_class = AdvertisementFilter

	def get_permissions(self):
	#"""Получение прав для действий."""
	#        if self.action in ["create", "update", "partial_update"]:
	#            return [IsAuthenticated]#, IsOwnerOrReadOnly()]
	#        return []
		permission_classes = []
			
		if self.action == "create":
			permission_classes = [IsAuthenticated]
			
		if self.action in ["update","partial_update","destroy"]:
			permission_classes = [IsOwner]
			
		return [permission() for permission in permission_classes]
		
			