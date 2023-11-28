from django.test import TestCase
from .models import Usuario
from .models import Reservacion
from datetime import date

class UsuarioTest(TestCase):
    def setUp(self):
        Usuario.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            password='hashed_password'
        )

    def test_str_method(self):
        usuario = Usuario.objects.get(email='john.doe@example.com')
        self.assertEqual(str(usuario), 'John Doe')

    def test_unique_email_constraint(self):
        with self.assertRaises(Exception):
            Usuario.objects.create(
                first_name='Jane',
                last_name='Doe',
                email='john.doe@example.com',
                password='hashed_password'
            )

    def test_model_fields(self):
        usuario = Usuario.objects.get(email='john.doe@example.com')
        self.assertEqual(usuario.first_name, 'John')
        self.assertEqual(usuario.last_name, 'Doe')
        self.assertEqual(usuario.email, 'john.doe@example.com')
        self.assertEqual(usuario.password, 'hashed_password')  # En una aplicación real, deberías cifrar la contraseña
        
        


class ReservacionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configura los datos de prueba una vez para toda la clase
        Reservacion.objects.create(
            fullname='John Doe',
            emailaddress='john@example.com',
            phone='123456789999',
            street='123 Main St',
            city='Cityville',
            postalcode='12345',
            country='Countryland',
            arrive=date(2023, 1, 1),
            depart=date(2023, 1, 7),
            amtpple=2,
            amtrms=1,
            rmtype='Deluxe Room',
            comments='Some custom needs.'
        )

    def test_fullname_label(self):
        reservacion = Reservacion.objects.get(id=1)
        field_label = reservacion._meta.get_field('fullname').verbose_name
        self.assertEquals(field_label, 'fullname')

    def test_emailaddress_label(self):
        reservacion = Reservacion.objects.get(id=1)
        field_label = reservacion._meta.get_field('emailaddress').verbose_name
        self.assertEquals(field_label, 'emailaddress')

    def test_phone_label(self):
        reservacion = Reservacion.objects.get(id=1)
        field_label = reservacion._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')

    def test_street_label(self):
        reservacion = Reservacion.objects.get(id=1)
        field_label = reservacion._meta.get_field('street').verbose_name
        self.assertEquals(field_label, 'street')

    def test_city_label(self):
        reservacion = Reservacion.objects.get(id=1)
        field_label = reservacion._meta.get_field('city').verbose_name
        self.assertEquals(field_label, 'city')

    def test_postalcode_label(self):
        reservacion = Reservacion.objects.get(id=1)
        field_label = reservacion._meta.get_field('postalcode').verbose_name
        self.assertEquals(field_label, 'postalcode')

    def test_country_label(self):
        reservacion = Reservacion.objects.get(id=1)
        field_label = reservacion._meta.get_field('country').verbose_name
        self.assertEquals(field_label, 'country')

    def test_arrive_label(self):
        reservacion = Reservacion.objects.get(id=1)
        field_label = reservacion._meta.get_field('arrive').verbose_name
        self.assertEquals(field_label, 'arrive')

    def test_depart_label(self):
        reservacion = Reservacion.objects.get(id=1)
        field_label = reservacion._meta.get_field('depart').verbose_name
        self.assertEquals(field_label, 'depart')

    def test_amtpple_label(self):
        reservacion = Reservacion.objects.get(id=1)
        field_label = reservacion._meta.get_field('amtpple').verbose_name
        self.assertEquals(field_label, 'amtpple')

    def test_amtrms_label(self):
        reservacion = Reservacion.objects.get(id=1)
        field_label = reservacion._meta.get_field('amtrms').verbose_name
        self.assertEquals(field_label, 'amtrms')

    def test_rmtype_label(self):
        reservacion = Reservacion.objects.get(id=1)
        field_label = reservacion._meta.get_field('rmtype').verbose_name
        self.assertEquals(field_label, 'rmtype')

    def test_comments_label(self):
        reservacion = Reservacion.objects.get(id=1)
        field_label = reservacion._meta.get_field('comments').verbose_name
        self.assertEquals(field_label, 'comments')

    def test_comments_max_length(self):
        reservacion = Reservacion.objects.get(id=1)
        max_length = reservacion._meta.get_field('comments').max_length
        self.assertEquals(max_length, 300)  # Ajusta el valor según tu modelo

    def test_object_name_is_fullname_and_email(self):
        reservacion = Reservacion.objects.get(id=1)
        expected_object_name = f"{reservacion.fullname} ({reservacion.emailaddress})"
        self.assertEquals(str(reservacion), expected_object_name)        