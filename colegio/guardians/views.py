from django.shortcuts import render
from django.views.generic import TemplateView, View  

class AcudienteBoard(View):
    def get(self, request, *args, **kwargs):
        vista = 'guardian'
        abierto='calendario'
        context = {
            'vista': vista,
            'abierto':abierto,
            'school': request.user.school,
        }
        return render(request, 'users/admin/inicio.html', context)

