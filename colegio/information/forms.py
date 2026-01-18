from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import DailySchedule, GradeTemplate, SubjectsTemplate
from users.models import CustomUserStudent, CustomUserTeachers
from .models import GradeBase, StudentAcademicYear
from django.core.exceptions import ValidationError


# Grades Forms
class GradeBaseForm(forms.ModelForm):
    def __init__(self, *args, schedule_parts, **kwargs):
        schedule_parts = kwargs.pop('schedule_parts', None)
        super().__init__(*args, **kwargs)

        if schedule_parts is not None:
            self.fields['schedule_parts'].queryset = schedule_parts
            
    class Meta:
        model = GradeBase
        fields = [
            'grade_name',
            'schedule_parts',
        ]

        labels = {
            'grade_name': 'Nombre del grado',
            'schedule_parts': 'Tipo de horario',
        }

        widgets = {
            'grade_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Undécimo'
            }),
            'schedule_parts': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

class HoraHorarioForm(forms.ModelForm):
    class Meta:
        model = DailySchedule
        fields = ('start_time', 'end_time')

        widgets = {
            'start_time': forms.TimeInput(attrs={'class': 'mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-orange-300', 'type':'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-orange-300', 'type':'time'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class MateriasHorarioForm(forms.ModelForm):
    def __init__(self, *args, materias_grado=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra las materias dependientes de este grado
        if materias_grado:
            self.fields['monday'].queryset = materias_grado
            self.fields['tuesday'].queryset = materias_grado
            self.fields['wednesday'].queryset = materias_grado
            self.fields['thursday'].queryset = materias_grado
            self.fields['friday'].queryset = materias_grado
            self.fields['saturday'].queryset = materias_grado
            print("hola")
            
    class Meta:
        model = DailySchedule
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        widgets = {
            'monday': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),
            'tuesday': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),
            'wednesday': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),
            'thursday': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),
            'friday': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),
            'saturday': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),
            }
        
class EditarVerNotasAlumnosForm(forms.ModelForm):
    class Meta:
        model = CustomUserStudent
        fields = ['see_notes']
        widgets = {
            'see_notes': forms.CheckboxInput(attrs={'class': 'h-8 w-8 m-0 text-blue-600 bg-gray-100 border-gray-300 rounded', 'id':'Checkbox'}),

            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# information/forms.py
from django import forms
from .models import ChatMessage

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['content', 'file']
        widgets = {
            "content": forms.TextInput(attrs={
                'autocomplete': 'off',
                'id': 'message_input',
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5',
                'placeholder': 'Escribe tu mensaje...'
            }),
            "file": forms.ClearableFileInput(attrs={
                'class': 'hidden',
                'id': 'file_input',
                'accept': 'image/*,application/pdf,.doc,.docx,.ppt,.pptx,.xls,.xlsx,.zip,.rar',
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class StudentAcademicYearForm(forms.ModelForm):
    class Meta:
        model = StudentAcademicYear
        fields = []
        widgets = {
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class GradeTemplateForm(forms.ModelForm):
    class Meta:
        model = GradeTemplate
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Undécimo A'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del grado',
                'rows': 3
            }),
        }
    def __init__(self, *args, **kwargs):
        school = kwargs.pop('school', None)
        super().__init__(*args, **kwargs)

        if school:
            self.fields['subjects'].queryset = SubjectsTemplate.objects.filter(
                school=school,
            )
        
class SubjectsTemplateForm(forms.ModelForm):

    class Meta:
        model = SubjectsTemplate
        fields = ['name', 'teachers', 'hourly_intensity']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la materia'
            }),
            'teachers': forms.SelectMultiple(attrs={
                'class': 'form-control',
            }),
            'hourly_intensity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Intensidad horaria (horas a la semana)',
                'min': 0,
            })
        }

    def __init__(self, *args, **kwargs):
        self.grade_template = kwargs.pop('grade_template', None)
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user and self.user.school:
            self.fields['teachers'].queryset = (
                CustomUserTeachers.get_by_school(self.user.school)
            )
        else:
            self.fields['teachers'].queryset = CustomUserTeachers.objects.none()
            
    def clean_hourly_intensity(self):
        hours = self.cleaned_data.get('hourly_intensity')
        
        if hours is None or hours<0:
            raise forms.ValidationError(
            "La intensidad horaria debe ser un número mayor o igual a 0."
            )

        if not self.grade_template:
            return hours

        remaining = self.grade_template.remaining_hours

        if hours > remaining:
            raise ValidationError(
                f"No hay suficientes horas disponibles. "
                f"Quedan {remaining} horas y querias agregar {hours}."
            )

        return hours
    def save(self, commit=True):
        obj = super().save(commit=False)

        if not self.grade_template:
            raise ValueError("GradeTemplate is required")

        obj.author = self.user
        obj.grade_template = self.grade_template
        obj.school = self.grade_template.school

        if commit:
            obj.save()
            self.save_m2m()

        return obj
