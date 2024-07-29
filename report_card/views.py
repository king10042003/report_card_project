from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Mark
from .forms import StudentForm, MarkForm
from django.contrib import messages

def welcome(request):
    return render(request, 'report_card/welcome.html')

def search_results(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(name__icontains=query)
        if students.exists():
            return render(request, 'report_card/student_report.html', {'students': students})
        else:
            return redirect('add_student')
    return redirect('welcome')

def student_detail(request, student_pk):
    student = get_object_or_404(Student, pk=student_pk)
    return render(request, 'report_card/student_detail.html', {'student': student})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'report_card/student_list.html', {'students': students})

def student_edit(request, student_pk):
    student = get_object_or_404(Student, pk=student_pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', student_pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'report_card/student_edit.html', {'form': form, 'student': student})

def student_delete(request, student_pk):
    student = get_object_or_404(Student, pk=student_pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'report_card/student_delete.html', {'student': student})

def delete_student(request, student_pk):
    student = get_object_or_404(Student, pk=student_pk)
    if request.method == 'POST':
        student.delete()
        return redirect('welcome')  # Redirect to the home page or wherever you want after deletion
    return render(request, 'report_card/delete_confirm.html', {'student': student})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('add_mark', student_pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'report_card/add_student.html', {'form': form})

def add_mark(request, student_pk):
    student = get_object_or_404(Student, pk=student_pk)
    subjects = get_subjects_for_student(student)

    # Convert subjects list into a tuple of tuples for the ChoiceField
    subject_choices = [(subject, subject) for subject in subjects]

    if request.method == 'POST':
        form = MarkForm(request.POST)
        form.fields['subject'].choices = subject_choices  # Set the choices
        if form.is_valid():
            subject = form.cleaned_data['subject']
            marks_obtained = form.cleaned_data['marks_obtained']
            total_marks = form.cleaned_data['total_marks']
            test_date = form.cleaned_data['test_date']

            mark = Mark(
                student=student,
                subject=subject,
                marks_obtained=marks_obtained,
                total_marks=total_marks,
                test_date=test_date
            )
            mark.save()
            return redirect('student_report', student_pk=student.pk)
    else:
        form = MarkForm()
        form.fields['subject'].choices = subject_choices  # Set the choices

    return render(request, 'report_card/add_mark.html', {
        'form': form,
        'student': student,
        'subjects': subjects
    })


def get_subjects_for_student(student):
    if student.class_name in ['8th', '9th', '10th']:
        return ['Maths', 'Physics', 'Chemistry', 'Biology', 'Mental Ability', 'Science']
    elif student.class_name in ['11th JEE', '12th JEE']:
        return ['Physics', 'Chemistry', 'Maths']
    elif student.class_name in ['11th NEET', '12th NEET']:
        return ['Physics', 'Chemistry', 'Biology']
    return []



def student_report(request, student_pk):
    student = get_object_or_404(Student, pk=student_pk)
    marks = Mark.objects.filter(student=student)
    
    context = {
        'student': student,
        'marks': marks
    }
    return render(request, 'report_card/student_report.html', context)
