from datetime import datetime
from rest_framework.filters import BaseFilterBackend


class GlucoseFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        start = request.query_params.get('start')
        stop =  request.query_params.get('stop')

        if start and stop:
            queryset = queryset.filter(gerätezeitstempel__range=(start, stop))
        return queryset
