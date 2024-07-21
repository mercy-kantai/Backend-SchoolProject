from django.db import models
from teacher.models import Teacher
# Create your models here.


class Classroom(models.Model):
    name = models.CharField(max_length=50)
    class_code = models.PositiveSmallIntegerField()
    class_description = models.TextField()
    class_capacity = models.PositiveIntegerField()
    class_teacher = models.ManyToManyField(Teacher, related_name='teacher')
    number_of_groups = models.PositiveIntegerField()
    class_art = models.CharField(max_length=20)

    def __str__(self):
        return self.name
