# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-11 13:26
from __future__ import unicode_literals

import buckets.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalQuestion',
            fields=[
                ('id', models.CharField(db_index=True, max_length=24)),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(blank=True, max_length=500, null=True)),
                ('type', models.CharField(choices=[('IN', 'integer'), ('DE', 'decimal'), ('TX', 'text'), ('S1', 'select one'), ('SM', 'select all that apply'), ('NO', 'note'), ('GP', 'geopoint'), ('GT', 'geotrace'), ('GS', 'geoshape'), ('DA', 'date'), ('TI', 'time'), ('DT', 'dateTime'), ('CA', 'calculate'), ('AC', 'acknowledge'), ('PH', 'photo'), ('AU', 'audio'), ('VI', 'video'), ('BC', 'barcode'), ('ST', 'start'), ('EN', 'end'), ('TD', 'today'), ('DI', 'deviceid'), ('SI', 'subsciberid'), ('SS', 'simserial'), ('PN', 'phonenumber')], max_length=2)),
                ('required', models.BooleanField(default=False)),
                ('constraint', models.CharField(blank=True, max_length=50, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical question',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalQuestionGroup',
            fields=[
                ('id', models.CharField(db_index=True, max_length=24)),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(blank=True, max_length=500, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical question group',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalQuestionnaire',
            fields=[
                ('id', models.CharField(db_index=True, max_length=24)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('id_string', models.CharField(max_length=50)),
                ('xls_form', buckets.fields.S3FileField(upload_to='xls-forms')),
                ('xml_form', buckets.fields.S3FileField(default=False, upload_to='xml-forms')),
                ('version', models.IntegerField(default=1)),
                ('md5_hash', models.CharField(default=False, max_length=50)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organization.Project')),
            ],
            options={
                'verbose_name': 'historical questionnaire',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalQuestionOption',
            fields=[
                ('id', models.CharField(db_index=True, max_length=24)),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=200)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical question option',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(blank=True, max_length=500, null=True)),
                ('type', models.CharField(choices=[('IN', 'integer'), ('DE', 'decimal'), ('TX', 'text'), ('S1', 'select one'), ('SM', 'select all that apply'), ('NO', 'note'), ('GP', 'geopoint'), ('GT', 'geotrace'), ('GS', 'geoshape'), ('DA', 'date'), ('TI', 'time'), ('DT', 'dateTime'), ('CA', 'calculate'), ('AC', 'acknowledge'), ('PH', 'photo'), ('AU', 'audio'), ('VI', 'video'), ('BC', 'barcode'), ('ST', 'start'), ('EN', 'end'), ('TD', 'today'), ('DI', 'deviceid'), ('SI', 'subsciberid'), ('SS', 'simserial'), ('PN', 'phonenumber')], max_length=2)),
                ('required', models.BooleanField(default=False)),
                ('constraint', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionGroup',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('id_string', models.CharField(max_length=50)),
                ('xls_form', buckets.fields.S3FileField(upload_to='xls-forms')),
                ('xml_form', buckets.fields.S3FileField(default=False, upload_to='xml-forms')),
                ('version', models.IntegerField(default=1)),
                ('md5_hash', models.CharField(default=False, max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaires', to='organization.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionOption',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='questionnaires.Question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='questiongroup',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_groups', to='questionnaires.Questionnaire'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='questionnaires.QuestionGroup'),
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='questionnaires.Questionnaire'),
        ),
        migrations.AddField(
            model_name='historicalquestionoption',
            name='question',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='questionnaires.Question'),
        ),
        migrations.AddField(
            model_name='historicalquestiongroup',
            name='questionnaire',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='questionnaires.Questionnaire'),
        ),
        migrations.AddField(
            model_name='historicalquestion',
            name='question_group',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='questionnaires.QuestionGroup'),
        ),
        migrations.AddField(
            model_name='historicalquestion',
            name='questionnaire',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='questionnaires.Questionnaire'),
        ),
    ]
