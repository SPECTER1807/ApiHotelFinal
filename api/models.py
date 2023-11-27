from django.db import models

class Usuario(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Este campo debería ser cifrado en una aplicación real

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Reservacion(models.Model):
    fullname = models.CharField(max_length=255)
    emailaddress = models.EmailField()
    phone = models.CharField(max_length=10)  # Ajusta la longitud según tus necesidades
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postalcode = models.CharField(max_length=20, blank=True)  # Puede ser opcional
    country = models.CharField(max_length=255)
    arrive = models.DateField()
    depart = models.DateField()
    amtpple = models.IntegerField()
    amtrms = models.IntegerField()
    rmtype = models.CharField(max_length=255)
    comments = models.TextField(max_length=300)  # Ajusta la longitud según tus necesidades

    def __str__(self):
        return f"{self.fullname} ({self.emailaddress})"
