# Generated by Django 4.2.2 on 2023-06-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipn', '0017_lvc_preliminary_event_date_utc'),
    ]

    operations = [
        migrations.AddField(
            model_name='integral_spi_acs_trigger',
            name='event_date_utc',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='lvc_retraction',
            name='event_date_utc',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='lvc_update_skymap',
            name='event_date_utc',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='test_integral_spi_acs_trigger',
            name='event_date_utc',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='test_lvc_initial_skymap',
            name='event_date_utc',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='test_lvc_preliminary',
            name='event_date_utc',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]