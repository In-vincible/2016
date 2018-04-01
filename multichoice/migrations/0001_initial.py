# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.CharField(verbose_name='Content', max_length=1000, help_text='Enter the answer text that you want displayed')),
                ('correct', models.BooleanField(verbose_name='Correct', default=False, help_text='Is this a correct answer?')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='MCQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(primary_key=True, to='quiz.Question', parent_link=True, auto_created=True, serialize=False)),
                ('answer_order', models.CharField(max_length=30, choices=[('content', 'Content'), ('random', 'Random'), ('none', 'None')], null=True, verbose_name='Answer Order', help_text='The order in which multichoice answer options are displayed to the user', blank=True)),
            ],
            options={
                'verbose_name': 'Multiple Choice Question',
                'verbose_name_plural': 'Multiple Choice Questions',
            },
            bases=('quiz.question',),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name='Question', to='multichoice.MCQuestion'),
        ),
    ]
