from django.shortcuts import render
from django.views.generic import TemplateView, View  

class AcudienteBoard(View):
    def get(self, request, *args, **kwargs):
        vista = 'guardian'
        abierto='calendario'
        
        # here we are going to add the guardian's students
        students = request.user.customuserguardian.student.all()
        
        context = {
            'vista': vista,
            'abierto':abierto,
            'school': request.user.school,
            'students': students,
        }
        return render(request, 'users/acudiente/inicio.html', context)

