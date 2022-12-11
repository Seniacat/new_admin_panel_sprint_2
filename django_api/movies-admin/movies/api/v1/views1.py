from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.list import BaseListView

from movies.models import Filmwork


class MoviesListApi(BaseListView):
    model = Filmwork
    http_method_names = ['get']  # Список методов, которые реализует обработчик
    
    def get_queryset(self):
        queryset = Filmwork.objects.prefetch_related(
            'genres', 'persons').all()
        queryset = queryset.values('id', 'title', 'description', 'rating', 'type', 'creation_date')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'results': list(self.get_queryset()),
        }
        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)
                 

