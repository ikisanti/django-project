from rest_framework import serializers
from .models import Usuarios, Juntas, Invitados, JuntasInvitados

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['ID_usuario', 'Nombre', 'Correo']

class InvitadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitados
        fields = ['ID_invitado', 'Nombre', 'Correo']

class JuntasSerializer(serializers.ModelSerializer):
    Creador = UsuariosSerializer()

    class Meta:
        model = Juntas
        fields = ['ID_junta', 'Titulo', 'Fecha', 'Hora', 'Tipo', 'Creador']

class JuntasInvitadosSerializer(serializers.ModelSerializer):
    ID_junta = JuntasSerializer()
    ID_invitado = InvitadosSerializer()

    class Meta:
        model = JuntasInvitados
        fields = ['ID_junta', 'ID_invitado']


