# Generated by Django 5.0.7 on 2024-07-14 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('class_code', models.PositiveSmallIntegerField()),
                ('class_description', models.TextField()),
                ('class_start_date', models.DateField()),
                ('class_end_date', models.DateField()),
                ('class_capacity', models.PositiveIntegerField()),
                ('class_teacher', models.ManyToManyField(related_name='classrooms', to='teacher.teacher')),
            ],
        ),
    ]
