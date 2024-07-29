from django.contrib import admin
from .models import Student, Mark

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'class_name')

class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks_obtained', 'total_marks', 'test_date')
    list_filter = ('test_date',)
    date_hierarchy = 'test_date'

admin.site.register(Student, StudentAdmin)
admin.site.register(Mark, MarkAdmin)
