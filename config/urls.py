from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView )
from core.router import router as core_router
from usuario.router import router as usuario_router
router = DefaultRouter()

router.registry.extend(core_router.registry)
router.registry.extend(usuario_router.registry)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/', include(router.urls)),
    path('api/', include(usuario_router.urls)),
    path('admin/', admin.site.urls),
]
