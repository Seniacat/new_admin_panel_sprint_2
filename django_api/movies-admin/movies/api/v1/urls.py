from django.urls import include, path
from rest_framework.routers import DefaultRouter

from movies.api.v1 import views

router = DefaultRouter()
router.register('movies', views.MoviesViewSet)

urlpatterns = [
    path('movies/', views.MoviesViewSet.as_view),
    path('', include(router.urls))
]
