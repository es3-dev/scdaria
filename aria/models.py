from django.db import models

# Create your models here.
class Sede(models.Model):
    nombre_sede = models.CharField(max_length=65)

    def __str__(self):
        return f'{self.nombre_sede}'

class Reunion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titulo}'

class Asistencia(models.Model):
    VINCULACION_CHOICES = [
        ('docente', 'Docente'),
        ('estudiante', 'Estudiante'),
        ('administrativo', 'Administrativo'),
        ('director', 'Director de Programa'),
        ('decano', 'Decano'),
        ('invitado', 'Invitado Externo'),
    ]

    nombre = models.CharField(max_length=200)
    documento = models.IntegerField()
    correo = models.CharField(max_length=200)
    vinculacion = models.CharField(blank=True, max_length=200, choices=VINCULACION_CHOICES)
    es_graduado = models.BooleanField(default=False)
    reunion = models.ForeignKey(Reunion, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} {self.documento} {self.correo}'

