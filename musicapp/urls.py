from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtisteViewSet, SongViewSet, LyricViewSet
from . import views

router = DefaultRouter()
router.register(r'artiste', ArtisteViewSet, basename='artiste')
router.register(r'song', SongViewSet, basename='song')
router.register(r'lyric', LyricViewSet, basename='lyric')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]