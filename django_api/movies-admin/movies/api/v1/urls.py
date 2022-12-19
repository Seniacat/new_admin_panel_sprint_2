from django.urls import include, path
from movies.api.v1 import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movies', views.MoviesViewSet, basename='movie')

urlpatterns = [
    path('', include(router.urls))
]
