from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from information.models import (
    SchoolYear, SubjectsTemplate, GradeTemplate, GradeBase, ScheduleParts
)
from django.urls import resolve
