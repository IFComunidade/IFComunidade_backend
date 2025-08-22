from rest_framework.routers import DefaultRouter
from core import views
router = DefaultRouter()

router.register(r'ocorrencias', views.OcorrenciaViewSet)
router.register(r'postagens', views.PostagemViewSet)