from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from drf_spectacular.utils import extend_schema
from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord

@extend_schema(tags=['Patient'], 
               description="Obtiene la lista de pacientes.",)
class ListPatientView(ListAPIView, CreateAPIView):
    """
    Obtiene la lista de pacientes y permite crear un nuevo paciente.
    """
    allowed_methods = ['GET', 'POST']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

@extend_schema(tags=['Patient'], 
               description="Obtiene un paciente por id.",)
class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

@extend_schema(tags=['Insurance'], 
               description="Obtiene la lista de seguros.",)
class ListInsuranceView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()

@extend_schema(tags=['Insurance'], 
               description="Obtiene un seguro por id.",)
class DetailInsuranceView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()

@extend_schema(tags=['MedicalRecord'], 
               description="Obtiene la lista de expedientes médicos.",)
class ListMedicalRecordView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()

@extend_schema(tags=['MedicalRecord'], 
               description="Obtiene un expediente médico por id.",)
class DetailMedicalRecordView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()