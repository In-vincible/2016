# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TF_Question',
            fields=[
                ('question_ptr', models.OneToOneField(primary_key=True, to='quiz.Question', parent_link=True, auto_created=True, serialize=False)),
                ('correct', models.BooleanField(verbose_name='Correct', default=False, help_text='Tick this if the question is true. Leave it blank for false.')),
            ],
            options={
                'verbose_name': 'True/False Question',
                'verbose_name_plural': 'True/False Questions',
                'ordering': ['category'],
            },
            bases=('quiz.question',),
        ),
    ]
