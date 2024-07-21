from django.db import models


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=20)
    course_duration = models.DurationField() 
    course_description = models.TextField()
    course_id = models.PositiveSmallIntegerField()
    course_department = models.CharField(max_length=20)
    course_status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])

    def __str__(self):
        return self.course_name
     