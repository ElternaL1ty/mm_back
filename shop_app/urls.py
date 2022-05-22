from rest_framework.routers import SimpleRouter
from .views import ProductViewSet, CategoryViewSet, OrderViewSet, UserViewSet
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        super().__init__()
        self.trailing_slash = '/?'


api_router = OptionalSlashRouter()
api_router.register(r'product', ProductViewSet)
api_router.register(r'category', CategoryViewSet)
api_router.register(r'order', OrderViewSet)
api_router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(api_router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]