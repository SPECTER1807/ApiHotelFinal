import pytest
from django.core.exceptions import ValidationError
from api.models import Usuario, Reservacion

@pytest.fixture
def usuario_data():
    return {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'juandoe@example.com',
        'password': 'hashed_password',
    }

@pytest.fixture
def reservacion_data():
    return {
        'fullname': 'Jane Doe',
        'emailaddress': 'jane.doe@example.com',
        'phone': '1234567890',
        'street': '123 Main St',
        'city': 'Cityville',
        'postalcode': '12345',
        'country': 'Countryland',
        'arrive': '2023-01-01',
        'depart': '2023-01-10',
        'amtpple': 2,
        'amtrms': 1,
        'rmtype': 'Single',
        'comments': 'Some comments about the reservation.',
    }

@pytest.mark.django_db
def test_create_usuario(usuario_data):
    Usuario.objects.create(**usuario_data)
    usuario = Usuario.objects.get(email=usuario_data['email'])
    assert usuario.first_name == usuario_data['first_name']
    assert usuario.last_name == usuario_data['last_name']
    assert usuario.email == usuario_data['email']



@pytest.mark.django_db
def test_create_reservacion(reservacion_data):
    Reservacion.objects.create(**reservacion_data)
    reservacion = Reservacion.objects.get(emailaddress=reservacion_data['emailaddress'])
    assert reservacion.fullname == reservacion_data['fullname']
    assert reservacion.emailaddress == reservacion_data['emailaddress']