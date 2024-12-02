from rest_framework.routers import DefaultRouter
from .viewsets import AppointmentViewSet

router = DefaultRouter()
router.register('appointments', AppointmentViewSet)

urlpatterns = router.urls