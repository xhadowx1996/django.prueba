from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions
from rest_framework.response import Response
import json
import csv
import io
from rest_framework import viewsets, status
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Clientes,Product

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


  

@api_view(['GET', 'POST', ])
def postCreateClientes(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    if  request.method == 'POST':
        print(body)
        for data in body:
             clientes = Clientes()
             print(data['documento'])
             clientes.documento = data['documento']
             clientes.nombres = data['nombres']
             clientes.apellido = data['apellido']
             clientes.correo = data['correo']
             clientes.save()

        return Response(body)


@api_view(['GET', 'POST', ])
def excels(request):
        clie = Clientes.objects.values()
        encoding ='utf-8'
        print('estoes unapura',list(clie))
        for data in clie:
            print(data['id'])
        fields = ['documento', 'nombres','apellido','correo']
        writer_file = io.StringIO()
        with open('prueba.csv','w',newline='') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=fields)
            writer.writeheader()
            for i in clie:
                writer.writerow({'documento': i['documento'],'nombres': i['nombres'],'apellido': i['apellido'],'correo': i['correo']})
                content = writer_file.getvalue()
                content = content.encode(encoding)
        return Response(content)  



@api_view(['GET', 'POST', ])
def produtos(self, request):
        products = Product.objects.all()
        serializer = ProductosSerializer(products, many=True)
        print(f'Se envio la respuesta {serializer.data}')
        return Response(ProductosSerializer.data)