from django.db import models
from django.db import models
from student.models import Student


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    code_id = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=20)
    students = models.ManyToManyField(Student, related_name='teacher')
    phone_number = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    office_hours = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
