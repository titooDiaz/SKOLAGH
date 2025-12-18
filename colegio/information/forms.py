from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import DailySchedule
from users.models import CustomUserStudent
from .models import GradeBase


# Grades Forms
class GradeBaseForm(forms.ModelForm):
    class Meta:
        model = GradeBase
        fields = [
            'grade_name',
            'grade_number',
            'schedule_parts',
            'school',
        ]

        labels = {
            'grade_name': 'Nombre del grado',
            'grade_number': 'Número del grado',
            'schedule_parts': 'Tipo de horario',
            'school': 'Colegio',
        }

        widgets = {
            'grade_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Undécimo'
            }),
            'grade_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),
            'schedule_parts': forms.Select(attrs={
                'class': 'form-control'
            }),
            'school': forms.Select(attrs={
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
