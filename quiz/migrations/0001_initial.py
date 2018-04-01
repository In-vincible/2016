# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('category', models.CharField(verbose_name='Category', max_length=250, unique=True, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('score', models.CommaSeparatedIntegerField(verbose_name='Score', max_length=1024)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Progress',
                'verbose_name_plural': 'User progress records',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('figure', models.ImageField(verbose_name='Figure', upload_to='udya/static/uploads/%Y/%m/%d', blank=True, null=True)),
                ('content', models.CharField(verbose_name='Question', max_length=1000, help_text='Enter the question text that you want displayed')),
                ('explanation', models.TextField(verbose_name='Explanation', max_length=2000, help_text='Explanation to be shown after the question has been answered.', blank=True)),
                ('category', models.ForeignKey(to='quiz.Category', verbose_name='Category', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=60)),
                ('description', models.TextField(verbose_name='Description', help_text='a description of the quiz', blank=True)),
                ('start_time', models.DateTimeField(verbose_name='Start_time', blank=True, null=True)),
                ('end_time', models.DateTimeField(verbose_name='End_time', blank=True, null=True)),
                ('duration', models.IntegerField(verbose_name='Duration', help_text='duration in minutes', blank=True)),
                ('url', models.SlugField(verbose_name='user friendly url', max_length=60, help_text='a user friendly url')),
                ('random_order', models.BooleanField(verbose_name='Random Order', default=False, help_text='Display the questions in a random order or as they are set?')),
                ('max_questions', models.PositiveIntegerField(verbose_name='Max Questions', help_text='Number of questions to be answered on each attempt.', blank=True, null=True)),
                ('answers_at_end', models.BooleanField(verbose_name='Answers at end', default=False, help_text='Correct answer is NOT shown after question. Answers displayed at the end.')),
                ('exam_paper', models.BooleanField(verbose_name='Exam Paper', default=False, help_text='If yes, the result of each attempt by a user will be stored. Necessary for marking.')),
                ('single_attempt', models.BooleanField(verbose_name='Single Attempt', default=False, help_text='If yes, only one attempt by a user will be permitted. Non users cannot sit this exam.')),
                ('pass_mark', models.SmallIntegerField(verbose_name='Pass Mark', default=0, help_text='Percentage required to pass exam.', blank=True, validators=[django.core.validators.MaxValueValidator(100)])),
                ('success_text', models.TextField(verbose_name='Success Text', help_text='Displayed if user passes.', blank=True)),
                ('fail_text', models.TextField(verbose_name='Fail Text', help_text='Displayed if user fails.', blank=True)),
                ('draft', models.BooleanField(verbose_name='Draft', default=False, help_text='If yes, the quiz is not displayed in the quiz list and can only be taken by users who can edit quizzes.')),
                ('category', models.ForeignKey(to='quiz.Category', verbose_name='Category', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.CreateModel(
            name='Sitting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question_order', models.CommaSeparatedIntegerField(verbose_name='Question Order', max_length=1024)),
                ('question_list', models.CommaSeparatedIntegerField(verbose_name='Question List', max_length=1024)),
                ('incorrect_questions', models.CommaSeparatedIntegerField(verbose_name='Incorrect questions', max_length=1024, blank=True)),
                ('current_score', models.IntegerField(verbose_name='Current Score')),
                ('complete', models.BooleanField(verbose_name='Complete', default=False)),
                ('user_answers', models.TextField(verbose_name='User Answers', default='{}', blank=True)),
                ('start', models.DateTimeField(verbose_name='Start', auto_now_add=True)),
                ('end', models.DateTimeField(verbose_name='End', blank=True, null=True)),
                ('quiz', models.ForeignKey(verbose_name='Quiz', to='quiz.Quiz')),
                ('user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_sittings', 'Can see completed exams.'),),
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sub_category', models.CharField(verbose_name='Sub-Category', max_length=250, blank=True, null=True)),
                ('category', models.ForeignKey(to='quiz.Category', verbose_name='Category', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Sub-Category',
                'verbose_name_plural': 'Sub-Categories',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ManyToManyField(verbose_name='Quiz', to='quiz.Quiz', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='sub_category',
            field=models.ForeignKey(to='quiz.SubCategory', verbose_name='Sub-Category', null=True, blank=True),
        ),
    ]
