from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import OrderingFilter

from api.filter import GlucoseFilter
from api.models import GlucoseLevel
from api.page import GlucosePageNumberPagination
from api.serializers import GlucoseLevelSerilizer


class GlucoseLevelView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = GlucoseLevel.objects.all()
    serializer_class = GlucoseLevelSerilizer
    pagination_class = GlucosePageNumberPagination
    filter_backends = [GlucoseFilter, OrderingFilter]

    ordering_filters = ['id', 'user_id', 'seriennummer', 'gerätezeitstempel']
