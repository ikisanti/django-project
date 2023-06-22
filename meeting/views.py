from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UsuariosSerializer, JuntasSerializer, InvitadosSerializer, JuntasInvitadosSerializer
from .models import Usuarios, Juntas, Invitados, JuntasInvitados

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class JuntasViewSet(viewsets.ModelViewSet):
    queryset = Juntas.objects.all()
    serializer_class = JuntasSerializer

class InvitadosViewSet(viewsets.ModelViewSet):
    queryset = Invitados.objects.all()
    serializer_class = InvitadosSerializer

class JuntasInvitadosViewSet(viewsets.ModelViewSet):
    queryset = JuntasInvitados.objects.all()
    serializer_class = JuntasInvitadosSerializer
    
    

