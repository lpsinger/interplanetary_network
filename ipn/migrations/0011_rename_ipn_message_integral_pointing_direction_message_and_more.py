# Generated by Django 4.2.2 on 2023-06-23 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipn', '0010_rename_ipn_message_id_integral_pointing_direction_ipn_message_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='integral_pointing_direction',
            old_name='ipn_message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='lvc_preliminary',
            old_name='ipn_message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='lvc_retraction',
            old_name='ipn_message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='test_lvc_initial_skymap',
            old_name='ipn_message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='test_lvc_preliminary',
            old_name='ipn_message',
            new_name='message',
        ),
    ]
