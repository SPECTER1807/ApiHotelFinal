from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

class Success(APIView):
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