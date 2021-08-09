from django.db import models
from django.conf import settings
from django.urls import reverse

# add this in foreignkey later


class Class(models.Model):
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.class_name

    def get_absolute_url(self):
        return reverse('class-student-list', args=[self.id])


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    tickets = models.IntegerField(default=0)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse('class-student-list', args=[self.class_name.id])
