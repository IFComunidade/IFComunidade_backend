from rest_framework.routers import DefaultRouter
from core import views
router = DefaultRouter()

router.register(r'setores', views.SetorViewSet)