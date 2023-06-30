from django.db import models
from ipn.models.Message import Message

class Integral_Pointing_Direction(models.Model):
  title = models.CharField(default=None, blank=True, null=True)
  notice_date = models.CharField(default=None, blank=True, null=True)
  notice_type = models.CharField(default=None, blank=True, null=True)
  next_point_ra = models.CharField(default=None, blank=True, null=True)
  next_point_dec = models.CharField(default=None, blank=True, null=True)
  slew_time = models.CharField(default=None, blank=True, null=True)
  slew_date = models.CharField(default=None, blank=True, null=True)
  sun_postn = models.CharField(default=None, blank=True, null=True)
  sun_dist = models.CharField(default=None, blank=True, null=True)
  moon_postn = models.CharField(default=None, blank=True, null=True)
  moon_dist = models.CharField(default=None, blank=True, null=True)
  gal_coords = models.CharField(default=None, blank=True, null=True)
  ecl_coords = models.CharField(default=None, blank=True, null=True)
  comments = models.CharField(default=None, blank=True, null=True)
  message = models.ForeignKey(Message, on_delete=models.CASCADE, default=None)

class Meta(object):
  app_label = 'ipn'
  db_table = 'ipn_integral_pointing_direction'
