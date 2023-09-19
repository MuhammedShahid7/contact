from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
