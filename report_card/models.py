from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=20)

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    marks_obtained = models.IntegerField(null=True, blank=True)
    total_marks = models.IntegerField(null=True, blank=True)
    test_date = models.DateField(null=True, blank=True)