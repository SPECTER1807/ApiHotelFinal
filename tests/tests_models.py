from datetime import date
import pytest
from django.core.exceptions import ValidationError
from .models import Usuario, Reservacion

@pytest.fixture
def usuario_data():
    return {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'password': 'hashed_password'
    }

@pytest.fixture
def reservacion_data():
    return {
        'fullname': 'John Doe',
        'emailaddress': 'john@example.com',
        'phone': '123456789999',
        'street': '123 Main St',
        'city': 'Cityville',
        'postalcode': '12345',
        'country': 'Countryland',
        'arrive': date(2023, 1, 1),
        'depart': date(2023, 1, 7),
        'amtpple': 2,
        'amtrms': 1,
        'rmtype': 'Deluxe Room',
        'comments': 'Some custom needs.'
    }

@pytest.mark.django_db
def test_usuario_str_method(usuario_data):
    usuario = Usuario.objects.create(**usuario_data)
    assert str(usuario) == 'John Doe'

@pytest.mark.django_db
def test_unique_email_constraint(usuario_data):
    Usuario.objects.create(**usuario_data)

    with pytest.raises(ValidationError):
        Usuario.objects.create(**usuario_data)

@pytest.mark.django_db
def test_usuario_model_fields(usuario_data):
    usuario = Usuario.objects.create(**usuario_data)
    assert usuario.first_name == 'John'
    assert usuario.last_name == 'Doe'
    assert usuario.email == 'john.doe@example.com'
    assert usuario.password == 'hashed_password'

@pytest.mark.django_db
def test_reservacion_fullname_label(reservacion_data):
    reservacion = Reservacion.objects.create(**reservacion_data)
    field_label = reservacion._meta.get_field('fullname').verbose_name
    assert field_label == 'fullname'
    
def test_reservacion_emailaddress_label(reservacion_data):
    reservacion = Reservacion.objects.create(**reservacion_data)
    field_label = reservacion._meta.get_field('emailaddress').verbose_name
    assert field_label == 'emailaddress'


@pytest.mark.django_db
def test_reservacion_comments_max_length(reservacion_data):
    reservacion = Reservacion.objects.create(**reservacion_data)
    max_length = reservacion._meta.get_field('comments').max_length
    assert max_length == 300

@pytest.mark.django_db
def test_reservacion_object_name_is_fullname_and_email(reservacion_data):
    reservacion = Reservacion.objects.create(**reservacion_data)
    expected_object_name = f"{reservacion.fullname} ({reservacion.emailaddress})"
    assert str(reservacion) == expected_object_name