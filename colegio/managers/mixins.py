from django.shortcuts import redirect
from django.contrib import messages
from utils.services import school_setup_status


class SchoolSetupRequiredMixin:
    """
    Enforce school setup rules ONLY for specific user types
    """

    required_user_types = ()  # ej: ('Administrador', 'Gestor')
    redirect_url = 'CrearHorarios'

    def dispatch(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            return redirect('login')

        # if no user types are specified, let it pass
        if not self.required_user_types:
            return super().dispatch(request, *args, **kwargs)

        # if user has no user_type attribute, let it pass
        if not hasattr(user, "user_type"):
            return super().dispatch(request, *args, **kwargs)

        # if user type does not apply, let it pass
        if user.user_type not in self.required_user_types:
            return super().dispatch(request, *args, **kwargs)

        # if user has no school assigned, it's a logical error
        if not user.school:
            messages.error(
                request,
                "Tu usuario no está asociado a ningún colegio."
            )
            return redirect("logout")

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
