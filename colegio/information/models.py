from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUserStudent, CustomUserTeachers, School
from django.conf import settings
import os
import random
from django.utils import timezone
import pytz

from django.contrib.auth import get_user_model
User = get_user_model()
UserProfes = CustomUserTeachers
UserAlumno = CustomUserStudent


TIPO_ACTIVIDAD = [
        ('EVALUATIVA', 'EVALUATIVA'),
        ('ASIMILATIVA', 'ASIMILATIVA'),
        ('EXPERIENCIAL', 'EXPERIENCIAL'),
        ('GESTION DE INFORMACION', 'GESTION DE INFORMACION'),
        ('APLICACION', 'APLICACION'),
        ('COMUNICATIVA', 'COMUNICATIVA'),
        ('PRODUCTIVA', 'PRODUCTIVA')
]

TIPO_RESTRICCION = [
        ('0', 'NO VERAN MAS LA ACTIVIDAD'),
        ('1', 'PUEDEN SUBIR LA ACTIVIDAD PERO CON ADVERTENCIA'),
]


def ano_actual():
    ano_electivo = timezone.now().year
    ano_electivo = int(ano_electivo)
    return ano_electivo

# Translate class: Anos_Electivos
class ElectiveYears(models.Model):
    year = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Creator_Elective_Year')
    state = models.BooleanField(default=True)

# Translate class: Horarios_Partes
class ScheduleParts(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True, related_name='ColegioHorariosPartes') #COLEGIO AL QUE PERTENECE EL USUARIO #colegio
    name = models.TextField() #titulo
    description = models.TextField() #descipcion
    state = models.BooleanField(default=True) #estado
    created_on = models.DateTimeField(auto_now_add=True) #create_on
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creador_de_materia') # author
    year_creation = models.IntegerField(default=ano_actual()) #ano_creacion
    hours = models.IntegerField(
        default=3,
        validators=[MinValueValidator(3), MaxValueValidator(22)]
    ) #horas
    school_cuts = models.IntegerField(
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(6)]
    ) #cortes

    def __str__(self):
        return "HORARIO DE " + self.name

def picture_materia_1(instance, filename):
    profile_picture_name = 'materias/media/{0}/{1}/{2}/picture.png'.format(instance.name_1, instance.teacher_1, random.randint(1, 9999))
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)
    if os.path.exists(full_path):
        os.remove(full_path)
    return profile_picture_name


# Translate class: Materias
class Subjects(models.Model):   
    elective = models.BooleanField(default=False) #electiva
    year_creation = models.IntegerField(default=ano_actual()) #ano_creacion
    ##################electivas##############
    photo = models.ImageField(default='materias/picture.png', upload_to=picture_materia_1, null=True, blank=True) #picture1
    cords = models.TextField(blank=True, null=False) #cords
    teacher_1 = models.ForeignKey(UserProfes,on_delete=models.CASCADE, blank=True, related_name='profesor_0') #profe1
    name_1 = models.TextField(blank=True, null=False) #titulo1
    description_1 = models.TextField(blank=True, null=False) #descripcion1
    location_1 = models.TextField(blank=True, null=False) #locate1
    students_1 = models.ManyToManyField(UserAlumno, blank=True, related_name='alumnos_electiva1') #alumnos1

    teacher_2 = models.ForeignKey(UserProfes,on_delete=models.CASCADE, blank=True, null=True, related_name='profesor_1') #profe2
    name_2 = models.TextField(blank=True, null=True) #titulo2
    location_2 = models.TextField(blank=True, null=False) #locate2
    description_2 = models.TextField(blank=True, null=True) #descripcion2
    students_2 = models.ManyToManyField(UserAlumno, blank=True, related_name='alumnos_electiva2') #alumnos2
    ##########################################
    state = models.BooleanField(default=True) #estado
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creador_materia')

    def __str__(self):
        return f'{self.name_1}'
    
class GradeBase(models.Model):
    grade_name = models.CharField(max_length=50)
    grade_number = models.IntegerField()
    schedule_parts = models.ForeignKey(ScheduleParts, on_delete=models.SET_NULL, blank=True, null=True)
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="grade_bases"
    )

    def __str__(self):
        return f"{self.grade_name} ({self.grade_number})"


# Translate class: Grado 
class Grade(models.Model):
    grade_base = models.ForeignKey(
        GradeBase,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="grades"
    )
    year_creation = models.IntegerField(default=ano_actual) #ano_creacion
    grade_name = models.TextField() #grado_nom
    description = models.TextField() #descripcion
    state = models.BooleanField(default=True) #estado
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creador_grado')
    subjects = models.ManyToManyField(Subjects, blank=True, related_name='materias_grado') #materias
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True, related_name='ColegioGrado') #COLEGIO AL QUE PERTENECE EL USUARIO #colegio

    def __str__(self):
        return self.grade_name
    # --- Constants for thresholds ---
    APPROVED_THRESHOLD = 70
    AT_RISK_LOW = 55
    AT_RISK_HIGH = 75

    def get_students(self):
        """Return all students in this grade."""
        return CustomUserStudent.objects.filter(grade=self)

    def get_average_for_student(self, student, court=None):
        """
        Calculate weighted average grade for a student.
        If `court` is provided, filter activities only for that court.
        """
        subjects = self.subjects.all()
        total, count = 0, 0

        for subject in subjects:
            ratings = Rating.objects.filter(student=student, activity__subject=subject)

            # 🔑 Filter by court if provided
            if court is not None:
                ratings = ratings.filter(
                    activity__start_date__gte=court.start_date,
                    activity__end_date__lte=court.end_date
                )


            if ratings.exists():
                weighted_sum = sum(r.rating * (r.activity.percentage / 100) for r in ratings)
                total_percentage = sum(r.activity.percentage for r in ratings)

                if total_percentage > 0:
                    avg = weighted_sum / (total_percentage / 100)
                    total += avg
                    count += 1

        return total / count if count > 0 else 0

    # --- Category filters ---
    def get_approved(self, court=None):
        """Return list of students with average >= APPROVED_THRESHOLD."""
        return [
            s for s in self.get_students()
            if self.get_average_for_student(s, court) >= self.APPROVED_THRESHOLD
        ]

    def get_failed(self, court=None):
        """Return list of students with average < APPROVED_THRESHOLD."""
        return [
            s for s in self.get_students()
            if self.get_average_for_student(s, court) < self.APPROVED_THRESHOLD
        ]

    def get_at_risk(self, court=None):
        """
        Return list of students with average between AT_RISK_LOW and AT_RISK_HIGH.
        """
        return [
            s for s in self.get_students()
            if self.AT_RISK_LOW <= self.get_average_for_student(s, court) < self.AT_RISK_HIGH
        ]
def get_current_date():
    fecha_actual = timezone.now().date()
    # Convertir la fecha a una cadena en el formato 'YYYY-MM-DD'
    fecha_actual_formateada = fecha_actual.strftime('%Y-%m-%d')

    return fecha_actual_formateada

def get_current_time():
    now = timezone.now()
    return now.replace(second=0, microsecond=0).time()

class StudentAcademicYear(models.Model):
    student = models.ForeignKey(CustomUserStudent, on_delete=models.CASCADE)
    grade_base = models.ForeignKey(GradeBase, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, blank=True)
    year = models.IntegerField()

    approved = models.BooleanField(null=True)

    class Meta:
        unique_together = ('student', 'year')



# Translate class: ActividadesTipo
class ActivitiesType(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True, related_name='ActividadesColegio') #COLEGIO AL QUE PERTENECE EL USUARIO #colegio
    name = models.TextField(null=False, blank=False) #titulo
    description = models.TextField(null=False, blank=False) #description
    state = models.BooleanField(default=True) #estado
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creador_de_tipo_actividad')
    year_creation = models.IntegerField(default=ano_actual()) #ano_creacion
    
    def __str__(self):
        return f"Actividad: {self.name}"


# Translate class: Actividades
class Activities(models.Model):
    name = models.TextField() #titulo
    description = models.TextField() #descripcion
    percentage = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)]) #porcentaje
    type = models.ForeignKey(ActivitiesType, on_delete=models.CASCADE, related_name='actividades') #tipo
    restriction = models.CharField(max_length=50, choices=TIPO_RESTRICCION, default='0') #restriccion
    start_date = models.DateField(default=get_current_date) #fecha_inicio
    end_date = models.DateField(default=get_current_date) #fecha_final
    start_time = models.TimeField(default=get_current_time) #hora_inicio
    end_time = models.TimeField(default=get_current_time) #hora_final
    
    ######
    location_time_zone= models.TextField(null=True) #lugar_zona_horaria
    time_zone = models.BooleanField(default=True) # cuando este activa significa que sera en el lugar que se encuntre el profesor en este momento #zona_horaria
    #si esta inactiva significa que se colocara la fecha donde se creo su perfil!
    #esta opcion solo aprece cuando los lugares y la zona horario es diferente
    
    year_creation = models.IntegerField(default=ano_actual()) #ano_creacion
    state = models.BooleanField(default=True) #estado
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creador_actividad')
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=True, blank=True, related_name='ActividadMateria') #materia

    def __str__(self):
        return f"{self.name} ({self.pk})"


def files(instance, filename):
    # Genera un nombre de archivo único
    archivo_guia = 'actividades_profesores/media/grado{0}({1})/{2}'.format(
        instance.activity.name, instance.activity.pk, filename)
    
    full_path = os.path.join(settings.MEDIA_ROOT, archivo_guia)
    
    # Verifica si el archivo ya existe y lo elimina si es necesario
    if os.path.exists(full_path):
        os.remove(full_path)
    
    return archivo_guia


#Ratings
class Rating(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='StudentRating')
    teacher= models.ForeignKey(User, on_delete=models.CASCADE, related_name="TeacherActivity") # Creator of activity
    activity = models.ForeignKey(Activities, on_delete=models.CASCADE, related_name='ActivityRating')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    created_on = models.DateTimeField(default=timezone.now)
    message = models.TextField(blank=False, null=True)
    
    def __str__(self):
        return f'Rating: User:{self.student}, Activity: {self.activity}'

# Translate class: Archivo
class File(models.Model):
    activity = models.ForeignKey(Activities, on_delete=models.CASCADE, related_name='activity') #actividad
    file = models.FileField(upload_to=files) #archivo
    name = models.CharField(max_length=40, blank=False) #nombre
    description = models.CharField(max_length=255, blank=False) #descripcion

    def __str__(self):
        return self.name or self.file.name


def files_respuesta(instance, filename):
    archivo_respuesta = 'respuesta_estudiantes_actividades/{0}/{1}'.format(
        instance.activity_answer.activity, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, archivo_respuesta)
    if os.path.exists(full_path):
        os.remove(full_path)
    return archivo_respuesta


# Translate class: Actividades_Respuesta_Estudiantes
class StudentResponse(models.Model):
    answer = models.TextField() #respuesta
    description = models.TextField() #descripcion
    delivery_date = models.DateField(default=get_current_date) #fecha_entrega
    delivery_time = models.TimeField(default=get_current_time) #hora_entrega
    timezone_response = models.TextField(null=True) #lugar_zona_horaria
    same_zone = models.BooleanField(default=True) # Si el estudiante cambia la fecha, este elemento saldrá como falso #misma_zona
    year_creation = models.IntegerField(default=ano_actual) #ano_creacion
    state = models.BooleanField(default=True) #estado
    created_on = models.DateTimeField(default=timezone.now) #create_on
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creador_respuesta')
    activity = models.ForeignKey(Activities, on_delete=models.CASCADE, null=True, blank=True, related_name='file') #actividad

    def __str__(self):
        return f"ACTIVIDAD ENTREGADA POR: {self.author}"

# Translate class: ArchivoEstudiantes
class StudentFiles(models.Model):
    activity_answer = models.ForeignKey(StudentResponse, on_delete=models.CASCADE, related_name='files') #actividad_respuesta
    file = models.FileField(upload_to=files_respuesta) #archivo

    def __str__(self):
        return f"Archivo para {self.activity_answer.author}: {self.file}"

# Translate class: HorarioDiario
class DailySchedule(models.Model): #Materias por dia (DEPENDIENDO DEL HORARIO SE VA A ITERAR SOBRE ESTE MODELO PARA CREAR LAS CLASES DIARIAS NECESARIAS)
    year_creation = models.IntegerField(default=ano_actual()) #ano_creacion
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE) #grado
    start_time = models.TimeField(blank=True, null=True) #hora_inicio
    end_time = models.TimeField(blank=True, null=True) #hora_fin
    """LOS MODELOS TIENEN NOMBRES DE DIAS PERO REALMENTE SE REFIEREN A LAS MATERIAS DE ESTE DIA
         |
        \|/                                                                               """
    monday = models.ForeignKey(Subjects, on_delete=models.SET_NULL, blank=True, null=True, related_name='subjects_grade_1')#lunes
    tuesday = models.ForeignKey(Subjects, on_delete=models.SET_NULL, blank=True, null=True, related_name='subjects_grade_2') #martes
    wednesday = models.ForeignKey(Subjects, on_delete=models.SET_NULL, blank=True, null=True, related_name='subjects_grade_3') #miercoles
    thursday = models.ForeignKey(Subjects, on_delete=models.SET_NULL, blank=True, null=True, related_name='subjects_grade_4') #jueves 
    friday = models.ForeignKey(Subjects, on_delete=models.SET_NULL, blank=True, null=True, related_name='subjects_grade_5') #viernes
    saturday = models.ForeignKey(Subjects, on_delete=models.SET_NULL, blank=True, null=True, related_name='subjects_grade_6') #viernes

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"


# Translate class: HorarioCortes
class ScheduleCourts(models.Model): 
    year_creation = models.IntegerField(default=ano_actual()) #ano_creacion
    schedule = models.ForeignKey(ScheduleParts, on_delete=models.CASCADE) #horario
    start_date = models.DateField(blank=True, null=True) #fecha_inicio
    end_date = models.DateField(blank=True, null=True) #fecha_fin
    court_number = models.IntegerField(blank=False) #corte_num
    file = models.BooleanField(default=False) #archivo
    
    def __str__(self):
        return f"{self.start_date} - {self.end_date}"
    
    # get courts
    # cortes = ScheduleCourts.objects.filter(schedule=grado.schedule_parts)
    
    def get_current_court(self, user, schedule, time):
        """
        Returns the current court based on the user's timezone.
        If 'time' is provided, it searches for the court that includes that date.
        """
        # Get user's timezone from profile, default to UTC if not available
        user_tz = getattr(user, 'time_zone', 'UTC')

        try:
            # Convert current time to user's timezone
            user_timezone = pytz.timezone(user_tz)
            current_time = time if time else timezone.now().astimezone(user_timezone).date()  # Use provided time or current date
        except pytz.UnknownTimeZoneError:
            # If the timezone is invalid, fallback to UTC
            current_time = time if time else timezone.now().date()

        # Find the court where the selected date falls within the start and end dates
        current_court = ScheduleCourts.objects.filter(
            start_date__lte=current_time, 
            end_date__gte=current_time,
            schedule=schedule,
        ).first()
        
        return current_court

def user_directory_path(instance, filename):
    # archivo se guarda en: chat_files/user_3/2025_06_23_UUID.png
    import uuid
    from datetime import datetime
    ext = filename.split('.')[-1]
    date_str = datetime.now().strftime('%Y_%m_%d')
    return f'chat_files/user_{instance.sender.id}/{date_str}_{uuid.uuid4()}.{ext}'

# Messages 
class ChatMessage(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    
    content = models.TextField(blank=True)  # text
    file = models.FileField(upload_to=user_directory_path, null=True, blank=True)

    deleted = models.BooleanField(default=False)
    sent_at = models.DateTimeField(default=timezone.now)  # date sent
    read = models.BooleanField(default=False)  # is the message read? 
    read_at = models.DateTimeField(blank=True, null=True)  # when the message was read?
    
    reply_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='replies')  # do you want to reply a message?
    important = models.BooleanField(default=False)  # is the message important?

    class Meta:
        ordering = ['sent_at']

    def __str__(self):
        return f"{self.sender} → {self.receiver}: {self.content[:30]}{'...' if len(self.content) > 30 else ''}"
    
class GlobalMessages(models.Model):
    message = models.TextField()  # message
    created_on = models.DateTimeField(auto_now_add=True)  # created_on
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_global_message')  # author
    startOn=models.DateTimeField(auto_now_add=True)  # startOn
    endOn=models.DateTimeField()  # endOn

    def __str__(self):
        return f"Global message by {self.author}: {self.message[:30]}{'...' if len(self.message) > 30 else ''}"