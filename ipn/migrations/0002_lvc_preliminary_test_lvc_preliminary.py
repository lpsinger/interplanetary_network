# Generated by Django 4.2.2 on 2023-06-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lvc_Preliminary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('notice_date', models.DateTimeField()),
                ('notice_type', models.CharField()),
                ('trigger_num', models.CharField()),
                ('trigger_date', models.DateField()),
                ('trigger_time', models.CharField()),
                ('group_type', models.CharField()),
                ('search_type', models.CharField()),
                ('pipeline_type', models.CharField()),
                ('far', models.CharField()),
                ('trigger_id', models.CharField()),
                ('misc', models.CharField()),
                ('skymap_fits_url', models.CharField()),
                ('eventpage_url', models.CharField()),
                ('comments', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Test_Lvc_Preliminary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('notice_date', models.DateTimeField()),
                ('notice_type', models.CharField()),
                ('trigger_num', models.CharField()),
                ('trigger_date', models.DateField()),
                ('trigger_time', models.CharField()),
                ('group_type', models.CharField()),
                ('search_type', models.CharField()),
                ('pipeline_type', models.CharField()),
                ('far', models.CharField()),
                ('trigger_id', models.CharField()),
                ('misc', models.CharField()),
                ('skymap_fits_url', models.CharField()),
                ('eventpage_url', models.CharField()),
                ('comments', models.CharField()),
                ('prob_ns', models.CharField()),
                ('prob_remnant', models.CharField()),
                ('prob_bns', models.CharField()),
                ('prob_nsbh', models.CharField()),
                ('prob_bbh', models.CharField()),
                ('prob_massgap', models.CharField()),
                ('prob_terres', models.CharField()),
            ],
        ),
    ]
