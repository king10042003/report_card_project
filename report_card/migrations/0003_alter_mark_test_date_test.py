# Generated by Django 5.0.3 on 2024-07-25 18:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_card', '0002_mark_test_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='test_date',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100)),
                ('test_date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report_card.student')),
            ],
        ),
    ]
