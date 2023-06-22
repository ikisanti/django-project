from django.db import models

class Usuarios(models.Model):
    ID_usuario = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Correo = models.EmailField(max_length=255)

class Juntas(models.Model):
    ID_junta = models.IntegerField(primary_key=True)
    Titulo = models.CharField(max_length=255)
    Fecha = models.DateField()
    Hora = models.TimeField()
    Tipo = models.CharField(max_length=50)
    Creador = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

class Invitados(models.Model):
    ID_invitado = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Correo = models.EmailField(max_length=255)

class JuntasInvitados(models.Model):
    ID_junta = models.ForeignKey(Juntas, on_delete=models.CASCADE)
    ID_invitado = models.ForeignKey(Invitados, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('ID_junta', 'ID_invitado')
