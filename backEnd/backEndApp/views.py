from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuarioSerializer,EjercitoSerializer
from .models import Usuario,UnidadEjercito
from rest_framework.permissions import IsAuthenticated

class UserCreate(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    def get(self, request, format=None):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

class EjercitoList(APIView):
    def get(self,request):
        ejercitos = UnidadEjercito.objects.all()
        serializer = EjercitoSerializer(ejercitos, many=True)
        return Response(serializer.data)



class EjercitoCreate(APIView):
    def post(self, request, format=None):
        serializer = EjercitoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        