# Generated by Django 5.0.3 on 2024-11-06 09:50

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='uploaded_image')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='uploaded_image')),
            ],
        ),
        migrations.CreateModel(
            name='CBTQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(help_text='Question for the CBT')),
                ('option_a', models.CharField(max_length=200)),
                ('option_b', models.CharField(max_length=200)),
                ('option_c', models.CharField(max_length=200)),
                ('option_d', models.CharField(max_length=200)),
                ('correct_option', models.CharField(choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D')], max_length=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cbt_questions', to='main.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='departments',
            field=models.ManyToManyField(related_name='courses', to='main.department'),
        ),
        migrations.CreateModel(
            name='PastQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(blank=True)),
                ('year', models.CharField(help_text='Year of the examination', max_length=4)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='past_questions', to='main.course')),
            ],
        ),
        migrations.CreateModel(
            name='KeyPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(blank=True, help_text='Key points or brief answers related to past questions')),
                ('past_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='key_points', to='main.pastquestions')),
            ],
        ),
        migrations.CreateModel(
            name='PracticeExplanations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explanation', ckeditor.fields.RichTextField(help_text='Explanation for the correct answer in CBT')),
                ('cbt_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='explanations', to='main.cbtquestion')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='uploaded_image')),
                ('phone', models.IntegerField(null=True)),
                ('school', models.CharField(max_length=255, null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='main.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('content', ckeditor.fields.RichTextField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='main.course')),
            ],
        ),
    ]
