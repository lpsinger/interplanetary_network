# Generated by Django 4.2.2 on 2023-06-22 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipn', '0005_integral_pointing_direction_ipn_message_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_Lvc_Initial_Skymap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, null=True)),
                ('notice_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('notice_type', models.CharField(blank=True, default=None, null=True)),
                ('trigger_num', models.CharField(blank=True, default=None, null=True)),
                ('trigger_date', models.DateField(blank=True, default=None, null=True)),
                ('trigger_time', models.CharField(blank=True, default=None, null=True)),
                ('trigger_id', models.CharField(blank=True, default=None, null=True)),
                ('sequence_num', models.BigIntegerField(blank=True, default=None, null=True)),
                ('group_type', models.CharField(blank=True, default=None, null=True)),
                ('search_type', models.CharField(blank=True, default=None, null=True)),
                ('pipeline_type', models.CharField(blank=True, default=None, null=True)),
                ('far', models.CharField(blank=True, default=None, null=True)),
                ('skymap_fits_url', models.CharField(blank=True, default=None, null=True)),
                ('eventpage_url', models.CharField(blank=True, default=None, null=True)),
                ('prob_ns', models.CharField(blank=True, default=None, null=True)),
                ('prob_remnant', models.CharField(blank=True, default=None, null=True)),
                ('prob_bns', models.CharField(blank=True, default=None, null=True)),
                ('prob_nsbh', models.CharField(blank=True, default=None, null=True)),
                ('prob_bbh', models.CharField(blank=True, default=None, null=True)),
                ('prob_massgap', models.CharField(blank=True, default=None, null=True)),
                ('prob_terres', models.CharField(blank=True, default=None, null=True)),
                ('comments', models.CharField(blank=True, default=None, null=True)),
                ('ipn_message_id', models.BigIntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]