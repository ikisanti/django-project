from rest_framework import routers
from .views import UsuariosViewSet, JuntasViewSet, InvitadosViewSet, JuntasInvitadosViewSet

router = routers.DefaultRouter()
router.register('api/usuarios', UsuariosViewSet, basename='usuarios')
router.register('api/juntas', JuntasViewSet, basename='juntas')
router.register('api/invitados', InvitadosViewSet, basename='invitados')
router.register('api/juntas-invitados', JuntasInvitadosViewSet, basename='juntas-invitados')

urlpatterns = router.urls