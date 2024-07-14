from django.db import models
from classroom.models import Classroom
# Create your models here.


class ClassPeriod(models.Model):
    start_time = models.DurationField()
    end_time = models.DurationField()
    course = models.CharField(max_length=255)
    classroom = models.ManyToManyField(Classroom, related_name='classrooms')
    day_of_week = models.CharField(max_length=255)