from django.shortcuts import redirect
from django.contrib import messages
from utils.services import school_setup_status

class SchoolSetupRequiredMixin:
    """
    Applies access rules based on the school's setup status
    ONLY to the specified roles
    """

    required_roles = ()
    redirect_url = 'CrearHorarios'

    def dispatch(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            return redirect('login')

        if not self.required_roles:
            return super().dispatch(request, *args, **kwargs)

        if user.role not in self.required_roles:
            return super().dispatch(request, *args, **kwargs)

        status = school_setup_status(user.school)

        if not status["has_schedule_parts"]:
            messages.warning(
                request,
                "Debes completar la configuración inicial del colegio."
            )
            messages.info(
                request,
                "Comienza creando el horario base."
            )
            return redirect(self.redirect_url)

        if not status["has_grades"]:
            messages.warning(
                request,
                "Debes crear los grados antes de continuar."
            )
            return redirect('createGradeBase')

        return super().dispatch(request, *args, **kwargs)
