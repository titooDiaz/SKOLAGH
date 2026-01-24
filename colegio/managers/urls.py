from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    #ver usuarios para modificar o ...
    path('board/', BoardGestores.as_view(), name='BoardGestores'),
    path('calendario/', CalendarioGestores.as_view(), name='CalendarioGestores'),
    path('personas/', ViewUsersSettings.as_view(), name='ViewUsersSettings'),
    path('ajustes/', AjustesGestores.as_view(), name='AjustesGestores'),
    path('manager/profile/', ViewProfile.as_view(), name='ViewProfile'),
    # change password
    path('manager/profile/password/', ChangePassword.as_view(), name='ChangePasswordManager'),

    #crear
    path('crear/profesores/', CreateProfesor.as_view(), name='CreateTeacher'),
    path('crear/gestores/', CreateGestor.as_view(), name='CrearGestor'),
    path('crear/alumnos/', CreateAlumno.as_view(), name='CrearAlumno'),
    path('crear/acudiente/', CreateAcudiente.as_view(), name='CrearAcudiente'),
    path('crear/admin/', CreateAdmin.as_view(), name='CrearAdmin'),
    path('crear/grados/', CreateGrados.as_view(), name='CrearGrado'),
    path('crear/gradeOrGradeBase/', GradeOrGradeBase.as_view(), name='GradeOrGradeBase'),
    path('crear/gradeBase/', CreateGradosBase.as_view(), name='CreateGradeBase'),
    path('crear/materias/<int:pk>', CreateMaterias.as_view(), name='CrearMaterias'),
    path('grados-template/create/<int:grade_base_id>/', CreateGradeTemplate.as_view(), name='create_grade_template'),

    
    # Horarios
    path('crear/horario/', CreateHorarios.as_view(), name='CrearHorarios'),
    path('crear/horario/cortes/', EditCortesHorarios.as_view(), name='CrearHorariosCortesGrados'),
    path('crear/horario/cortes/<int:pk>', CreateCortes.as_view(), name='CrearHorariosCortes'),
    path('crear/horario/cortes/<int:corte_pk>/<int:pk>', EditCortes.as_view(), name='EditHorariosCortes'),
    
    path('crear/materias/', CreateMateriasVer.as_view(), name='VerGradosMaterias'),
    
    # Actividades tipo
    path('crear/actividad/tipo/', CreateActividadTipo.as_view(), name='ActividadTipo'),

    #mensajes
    path('mensajes/',  ManagersMessages.as_view(), name='MessagesManagers'),
    
    #subjects tempalte
    path('grade-template/<int:grade_template_id>/subject/add/', SubjectTemplate.as_view(), name='add_subject_template'),
    
    # Settings of school
    path('create/school/year/', CreateSchoolYear.as_view(), name='CreateSchoolYear'),
    path('mark/ready/<int:grade_template_id>/', MarkGradeTemplateReady.as_view(), name='mark_grade_template_ready'),

]