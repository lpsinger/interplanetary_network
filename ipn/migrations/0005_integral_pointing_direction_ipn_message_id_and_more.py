# Generated by Django 4.2.2 on 2023-06-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipn', '0004_message_notice_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='integral_pointing_direction',
            name='ipn_message_id',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='lvc_preliminary',
            name='ipn_message_id',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='lvc_retraction',
            name='ipn_message_id',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='test_lvc_preliminary',
            name='ipn_message_id',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='integral_pointing_direction',
            name='comments',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='integral_pointing_direction',
            name='ecl_coords',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='integral_pointing_direction',
            name='gal_coords',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='integral_pointing_direction',
            name='moon_dist',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='integral_pointing_direction',
            name='moon_postn',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='integral_pointing_direction',
            name='next_point_dec',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='integral_pointing_direction',
            name='next_point_ra',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='integral_pointing_direction',
            name='notice_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='integral_pointing_direction',
            name='notice_type',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='integral_pointing_direction',
            name='slew_date',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='integral_pointing_direction',
            name='slew_time',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='integral_pointing_direction',
            name='sun_dist',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='integral_pointing_direction',
            name='sun_postn',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='integral_pointing_direction',
            name='title',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_preliminary',
            name='comments',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_preliminary',
            name='eventpage_url',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_preliminary',
            name='far',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_preliminary',
            name='group_type',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_preliminary',
            name='misc',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_preliminary',
            name='notice_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_preliminary',
            name='notice_type',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_preliminary',
            name='pipeline_type',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_preliminary',
            name='search_type',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_preliminary',
            name='skymap_fits_url',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_preliminary',
            name='title',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_preliminary',
            name='trigger_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_preliminary',
            name='trigger_id',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_preliminary',
            name='trigger_num',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_preliminary',
            name='trigger_time',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_retraction',
            name='comments',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_retraction',
            name='misc',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_retraction',
            name='notice_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_retraction',
            name='notice_type',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_retraction',
            name='sequence_num',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_retraction',
            name='title',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_retraction',
            name='trigger_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_retraction',
            name='trigger_id',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_retraction',
            name='trigger_num',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lvc_retraction',
            name='trigger_time',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='comments',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='eventpage_url',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='far',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='group_type',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='misc',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='notice_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='notice_type',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='pipeline_type',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='prob_bbh',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='prob_bns',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='prob_massgap',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='prob_ns',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='prob_nsbh',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='prob_remnant',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='prob_terres',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='search_type',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='skymap_fits_url',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='title',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='trigger_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='trigger_id',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='trigger_num',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='test_lvc_preliminary',
            name='trigger_time',
            field=models.CharField(blank=True, default=None, null=True),
        ),
    ]
