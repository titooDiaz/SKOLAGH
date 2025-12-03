from django.shortcuts import render
from django.views.generic import TemplateView, View  

class AcudienteBoard(View):
    def get(self, request, *args, **kwargs):
        vista = 'guardian'
        abierto='home'
        
        # here we are going to add the guardian's students
        students = request.user.customuserguardian.student.all()
        
        context = {
            'vista': vista,
            'abierto':abierto,
            'school': request.user.school,
            'students': students,
        }
        return render(request, 'users/acudiente/inicio.html', context)


class AcudienteSchedule(View):
    def get(self, request, *args, **kwargs):
        vista = 'guardian'
        abierto='schedule'
        
        # here we are going to add the guardian's students
        students = request.user.customuserguardian.student.all()
        
        context = {
            'vista': vista,
            'abierto':abierto,
            'school': request.user.school,
        }
        return render(request, 'users/acudiente/schedule.html', context)

class AcudientePeople(View):
    def get(self, request, *args, **kwargs):
        vista = 'guardian'
        abierto='people'
        
        # here we are going to add the guardian's students
        students = request.user.customuserguardian.student.all()
        
        context = {
            'vista': vista,
            'abierto':abierto,
            'students': students,
            'school': request.user.school,
        }
        return render(request, 'users/acudiente/people.html', context)
    
class AcudienteGrades(View):
    def get(self, request, *args, **kwargs):
        vista = 'guardian'
        abierto='grades'
        
        # here we are going to add the guardian's students
        students = request.user.customuserguardian.student.all()
        
        context = {
            'vista': vista,
            'abierto':abierto,
            'school': request.user.school,
        }
        return render(request, 'users/acudiente/grades.html', context)