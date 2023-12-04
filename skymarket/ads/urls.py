from django.urls import path
from rest_framework.routers import DefaultRouter
from .apps import SalesConfig
from .views import AdViewSet, AdAutorListAPIView, CommentViewSet

app_name = SalesConfig.name

router_ads = DefaultRouter()
router_ads.register(r'ads', AdViewSet, basename='ads')

router_comments = DefaultRouter()
router_comments.register(r'ads/(?P<ad_pk>[^/.]+)/comments', CommentViewSet, basename='ad-comments')


urlpatterns = [
    path('ads/me/', AdAutorListAPIView.as_view(), name='me'),

] + router_ads.urls + router_comments.urls
