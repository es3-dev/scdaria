from django.urls import path, include
from rest_framework import routers
from .api import SedeViewSet, ReunionViewSet, AsistenciaViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'api/sede', SedeViewSet, 'sede')
router.register(r'api/reunion', ReunionViewSet, 'reunion')
router.register(r'api/asistencia', AsistenciaViewSet, 'asistencia')


urlpatterns = [
    #Inclusion de api
    path('api/', include(router.urls)),

    #Vista principal - lista de reuniones
    path('', views.listaReuniones, name='lista_reuniones'),
    
    #Gestión de reuniones
    path('reunion/crear/', views.crearReunion, name='crear_reunion'),    
    path('reunion/<int:reunion_id>/', views.reunionCreada, name='reunion_creada'),
    path('reunion/<int:reunion_id>/editar/', views.editarReunion, name='editar_reunion'),
    path('reunion/<int:reunion_id>/eliminar/', views.eliminarReunion, name='eliminar_reunion'),
    
    #Gestión de asistencia
    path('reunion/<int:reunion_id>/asistencia/', views.formularioAsistencia, name='formulario_asistencia'),
    path('reunion/<int:reunion_id>/asistencia/registrar/', views.registrarAsistencia, name='registrar_asistencia'),
    path('reunion/<int:reunion_id>/asistencia/<int:asistencia_id>/editar/', views.editarAsistencia, name='editar_asistencia'),
]