import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from patients.models import Patient
from doctors.models import Doctor

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def patient():
    return Patient.objects.create(
        first_name='Paula',
        last_name='Orellana',
        date_of_birth='1997-12-01',
        contact_number='12312312',
        email='example@example.com',
        address='Dirección de prueba',
        medical_history='Ninguna',
    )

@pytest.fixture
def doctor():
    return Doctor.objects.create(
        first_name='Ronaldo',
        last_name='Jimenez',
        qualification='Profesional',
        contact_number='23412341234',
        email='example2@example.com',
        address='Cali',
        biography='Sin',
        is_on_vacation=False,
    )
    
@pytest.mark.django_db
def test_list_should_return_403(api_client, doctor):
    url = reverse('doctor-appointments', kwargs={"pk": doctor.id})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN

