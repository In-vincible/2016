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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('category', models.CharField(verbose_name='Category', null=True, unique=True, blank=True, max_length=250)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('score', models.CommaSeparatedIntegerField(verbose_name='Score', max_length=1024)),
                ('user', models.OneToOneField(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Progress',
                'verbose_name_plural': 'User progress records',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('figure', models.ImageField(verbose_name='Figure', upload_to='udya/static/uploads/%Y/%m/%d', null=True, blank=True)),
                ('content', models.CharField(help_text='Enter the question text that you want displayed', verbose_name='Question', max_length=1000)),
                ('explanation', models.TextField(help_text='Explanation to be shown after the question has been answered.', verbose_name='Explanation', blank=True, max_length=2000)),
                ('category', models.ForeignKey(verbose_name='Category', blank=True, to='quiz.Category', null=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(verbose_name='Title', max_length=60)),
                ('description', models.TextField(help_text='a description of the quiz', verbose_name='Description', blank=True)),
                ('start_time', models.DateTimeField(verbose_name='Start_time', null=True, blank=True)),
                ('end_time', models.DateTimeField(verbose_name='End_time', null=True, blank=True)),
                ('duration', models.IntegerField(help_text='duration in minutes', verbose_name='Duration', blank=True)),
                ('url', models.SlugField(help_text='a user friendly url', verbose_name='user friendly url', max_length=60)),
                ('random_order', models.BooleanField(help_text='Display the questions in a random order or as they are set?', verbose_name='Random Order', default=False)),
                ('max_questions', models.PositiveIntegerField(help_text='Number of questions to be answered on each attempt.', verbose_name='Max Questions', null=True, blank=True)),
                ('answers_at_end', models.BooleanField(help_text='Correct answer is NOT shown after question. Answers displayed at the end.', verbose_name='Answers at end', default=False)),
                ('exam_paper', models.BooleanField(help_text='If yes, the result of each attempt by a user will be stored. Necessary for marking.', verbose_name='Exam Paper', default=False)),
                ('single_attempt', models.BooleanField(help_text='If yes, only one attempt by a user will be permitted. Non users cannot sit this exam.', verbose_name='Single Attempt', default=False)),
                ('pass_mark', models.SmallIntegerField(help_text='Percentage required to pass exam.', verbose_name='Pass Mark', validators=[django.core.validators.MaxValueValidator(100)], blank=True, default=0)),
                ('success_text', models.TextField(help_text='Displayed if user passes.', verbose_name='Success Text', blank=True)),
                ('fail_text', models.TextField(help_text='Displayed if user fails.', verbose_name='Fail Text', blank=True)),
                ('draft', models.BooleanField(help_text='If yes, the quiz is not displayed in the quiz list and can only be taken by users who can edit quizzes.', verbose_name='Draft', default=False)),
                ('category', models.ForeignKey(verbose_name='Category', blank=True, to='quiz.Category', null=True)),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.CreateModel(
            name='Sitting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('question_order', models.CommaSeparatedIntegerField(verbose_name='Question Order', max_length=1024)),
                ('question_list', models.CommaSeparatedIntegerField(verbose_name='Question List', max_length=1024)),
                ('incorrect_questions', models.CommaSeparatedIntegerField(verbose_name='Incorrect questions', blank=True, max_length=1024)),
                ('current_score', models.IntegerField(verbose_name='Current Score')),
                ('complete', models.BooleanField(verbose_name='Complete', default=False)),
                ('user_answers', models.TextField(verbose_name='User Answers', blank=True, default='{}')),
                ('start', models.DateTimeField(verbose_name='Start', auto_now_add=True)),
                ('end', models.DateTimeField(verbose_name='End', null=True, blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sub_category', models.CharField(verbose_name='Sub-Category', null=True, blank=True, max_length=250)),
                ('category', models.ForeignKey(verbose_name='Category', blank=True, to='quiz.Category', null=True)),
            ],
            options={
                'verbose_name': 'Sub-Category',
                'verbose_name_plural': 'Sub-Categories',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ManyToManyField(verbose_name='Quiz', blank=True, to='quiz.Quiz'),
        ),
        migrations.AddField(
            model_name='question',
            name='sub_category',
            field=models.ForeignKey(verbose_name='Sub-Category', blank=True, to='quiz.SubCategory', null=True),
        ),
    ]
