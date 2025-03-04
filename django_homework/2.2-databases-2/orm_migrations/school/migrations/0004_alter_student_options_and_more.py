# Generated by Django 5.0.7 on 2024-08-06 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_rename_teachers_student_teacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['group'], 'verbose_name': 'Ученик', 'verbose_name_plural': 'Ученики'},
        ),
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='StudentTeachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.teacher')),
            ],
        ),
    ]
