from django.db import models
from teacher.models import Teacher
# Create your models here.


class Classroom(models.Model):
    name = models.CharField(max_length=50)
    class_code = models.PositiveSmallIntegerField()
    class_description = models.TextField()
    class_start_date = models.DateField()
    class_end_date = models.DateField()
    class_capacity = models.PositiveIntegerField()
    class_teacher = models.ManyToManyField(Teacher, related_name='classrooms')

    def __str__(self):
        return self.class_name
