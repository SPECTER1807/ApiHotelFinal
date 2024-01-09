
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.views import APIView

# Create your views here.

def registro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password2')
        
        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=username, email=email, password=password)
                    if user is not None:
                        # Envío del correo
                        subject = 'Registro Exitoso'
                        from_email = 'victorm.mtz.1999@gmail.com'  #
                        to_email = [email]
                        
                        # Renderiza el template HTML del correo
                        html_content = render_to_string('correo.html', {
                            'username': username,
                            'password': password,
                        })
                        
                        text_content = strip_tags(html_content)
                        
                        msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()
                        
                    
                        return redirect('login_view')
                else:
                    error_message = "El correo electrónico ya está en uso."
                    return render(request, 'authentication-register.html', {'error_message': error_message})
            else:
                error_message = "El nombre de usuario ya existe."
                return render(request, 'authentication-register.html', {'error_message': error_message})
        else:
            error_message = "Las contraseñas no coinciden."
            return render(request, 'authentication-register.html', {'error_message': error_message})

    return render(request, 'authentication-register.html')


def login_view(request):
    # Verificar si hay usuarios registrados
    if User.objects.exists():
        if request.method == 'POST':
            # Obtener el correo y la contraseña del formulario
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            # Autenticar al usuario
            user = authenticate(request, email=email, password=password)
            
            # Si el usuario es autenticado correctamente, iniciar sesión
            if user is not None:
                login(request, user)
                # Redirige a la página deseada después del inicio de sesión
                return redirect('dashboard')
            else:
                error_message = "Correo o contraseña incorrectos. Por favor, inténtalo de nuevo."
                return render(request, 'authentication-login.html', {'error_message': error_message})
        
        return render(request, 'authentication-login.html')
    else:
        # Si no hay usuarios registrados, redirige al formulario de registro
        return redirect('authentication-registro')

class Dashboard(APIView):
    template_name="dashboard.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Home(APIView):
    template_name="index.html"
    def get(self, request):
        return render(request,self.template_name) 

class Login(APIView):
    template_name="login.html"
    def get(self,request):
        return render(request,self.template_name)    

class Register(APIView):
    template_name="login.html"
    def get(self,request):
        return render(request,self.template_name)    
class About(APIView):
    template_name="about.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Amenities(APIView):
    template_name="amenities.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Bookings(APIView):
    template_name="bookings.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Contact(APIView):
    template_name="contact.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Failed(APIView):
    template_name="failed.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Faqs(APIView):
    template_name="faqs.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Gallery(APIView):
    template_name="gallery.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Privacy(APIView):
    template_name="privacy-policy.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Rooms(APIView):
    template_name="rooms.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Alcove(APIView):
    template_name="alcove.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Business(APIView):
    template_name="business-suite.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Cottage(APIView):
    template_name="cottage.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Deluxe(APIView):
    template_name="deluxe.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Executive(APIView):
    template_name="executive.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class RoundHouse(APIView):
    template_name="round-house.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Studio(APIView):
    template_name="studio.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Vip(APIView):
    template_name="vip.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Vvip(APIView):
    template_name="vvip.html"
    def get(self, request):
        return render(request,self.template_name) 
                
class Success(APIView):
    template_name="success.html"
    def get(self, request):
        return render(request,self.template_name) 


from .forms import ReservaForm
from .models import Reserva

def reservas(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas_confirmacion')
    else:
        form = ReservaForm()

    return render(request, 'reservas.html', {'form': form})

def reservas_confirmacion(request):
    return render(request, 'reservas_confirmacion.html')

    
# # views.py

# from django.shortcuts import render
# from django.http import HttpResponse
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from googleapiclient.discovery import build
# from django.views.decorators.csrf import csrf_exempt

# def autenticar_google():
#     creds = None
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json')

#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 settings.GOOGLE_CREDENTIALS_FILE,
#                 ['https://www.googleapis.com/auth/calendar']
#             )
#             creds = flow.run_local_server(port=0)

#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     return creds

# @csrf_exempt
# def reservar_habitacion(request):
#     if request.method == 'POST':
#         # Obtener datos del formulario
#         nombre = request.POST.get('nombre')
#         correo = request.POST.get('correo')
#         fecha_entrada = request.POST.get('fechaEntrada')
#         fecha_salida = request.POST.get('fechaSalida')

#         # Autenticar con Google
#         creds = autenticar_google()
#         service = build('calendar', 'v3', credentials=creds)

#         # Crear evento en Google Calendar
#         evento = {
#             'summary': f'Reservación de Hotel - {nombre}',
#             'description': f'Reservación para {nombre} ({correo})',
#             'start': {'dateTime': f'{fecha_entrada}T12:00:00', 'timeZone': 'America/New_York'},
#             'end': {'dateTime': f'{fecha_salida}T12:00:00', 'timeZone': 'America/New_York'},
#         }

#         event = service.events().insert(calendarId='primary', body=evento).execute()

#         return HttpResponse(f'¡Reservación creada! Evento en Google Calendar: {event.get("htmlLink")}')

#     return render(request, 'reservar_habitacion.html')

#********************+Paypal*****************************
 
# from ProductsApp.models import Product
 
# def CheckOut(request, product_id):
#      product = Product.objects.get(id=product_id)
     
#      context = {
#          'product': product,
#      }
#      return render(request, 'checkout.html', context)
 
# def PaymentSuccessful(request,product_id):
#      product = Product.objects.get(id=product_id)
#      return render(request, 'payment-success.html', {'product': product})
 
# def PaymentFailed(request,product_id):
#      product = Product.objects.get(id=product_id)
#      return render(request, 'payment-failed.html', {'product': product})

# def index(request):
#     return render(request='payments/index.html')