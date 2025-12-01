from django.urls import path
from .views import *

urlpatterns = [
    path('board/', AcudienteBoard.as_view(), name='GuardianBoard'),
    path('schedule/', AcudienteSchedule.as_view(), name='GuardianSchedule'),
    path('people/', AcudientePeople.as_view(), name='GuardianPeople'),
    path('grades/', AcudienteGrades.as_view(), name='GuardianGrades'),
]