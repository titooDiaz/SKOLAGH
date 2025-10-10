from django.urls import path
from .views import AlumnoBoard, AlumnoCalendario, StudentMessages, StudentGrades, StudentPeople, ActividadesRespuestaView, SubjectsView
from .views import *

urlpatterns = [
    #vista estudiantes
    path('board/', AlumnoBoard.as_view(), name='BoardAlumno'),
    path('board/<int:court_id>/', AlumnoBoard.as_view(), name='board_by_court'),
    
    # es - Materias
    # en - Subjects
    path('materias/ver/<int:pk>', SubjectsView.as_view(), name='SubjectsView'),
    
    # es - Actividades
    # en - activities
    path('actividades/responder/<int:pk>', ActividadesRespuestaView.as_view(), name='ResponderActividades'),
    path('calendario/', AlumnoCalendario.as_view(), name='CalendarioAlumno'),

    path('student/profile/', ViewProfile.as_view(), name='ViewProfileStudent'),
    path('student/settings/', ViewSettings.as_view(), name='ViewSettings'),
    # change password
    path('student/profile/password/', ChangePassword.as_view(), name='ChangePasswordStudent'),
    
    # es - Mensajes
    # en - Messages
    path('mensajes/', StudentMessages.as_view(), name='MessagesStudent'),
    
    # es - Notas
    # en - Grades
    path('notas/', StudentGrades.as_view(), name='GradesStudent'),
    
    # es - Personas
    # en - People
    path('personas/', StudentPeople.as_view(), name='PeopleStudent'),
    
    # Menu urls (improve your grades!)
    path('virtual/board/', BoardMenu.as_view(), name='BoardMenu'),
    path('virtual/tomato/', TomatoMenu.as_view(), name='TomatoMenu'),
    path('virtual/sofIA/', SofIAMenu.as_view(), name='SofiaMenu'),
]
