# Generated by Django 5.0.3 on 2024-07-26 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_card', '0004_mark_exam_name_delete_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='exam_name',
        ),
        migrations.AlterField(
            model_name='mark',
            name='subject',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.CharField(max_length=20),
        ),
    ]
