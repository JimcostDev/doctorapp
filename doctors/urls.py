
from rest_framework.routers import DefaultRouter
from .viewsets import DepartmentViewSet, DoctorViewSet, MedicalNoteViewSet

router = DefaultRouter()
router.register('doctors', DoctorViewSet)
router.register('departments', DepartmentViewSet)
router.register('medicalnotes', MedicalNoteViewSet)

urlpatterns = router.urls
