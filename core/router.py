from rest_framework.routers import DefaultRouter
from core import views
router = DefaultRouter()

router.register(r'ocorrencias', views.OcorrenciaViewSet)
router.register(r'postagens', views.PostagemViewSet)
router.register(r'opcoes', views.OpcaoViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'cursos', views.CursoViewSet)