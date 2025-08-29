from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import ( SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView, )
from django.views.generic import RedirectView
from core.router import router as core_router
from usuario.router import router as usuario_router
from uploader.router import router as uploader_router
router = DefaultRouter()

router.registry.extend(core_router.registry)
router.registry.extend(usuario_router.registry)
router.registry.extend(uploader_router.registry)

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=False)),
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/media/', include(uploader_router.urls)),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name="schema"), name="swagger ui"),
    path('api/redoc/', SpectacularRedocView.as_view(url_name="schema"), name="redoc")
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)