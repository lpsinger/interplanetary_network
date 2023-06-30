from django.db import models
from ipn.models.Message import Message
from ipn.repo.shared_utils import format_trigger_date

class Lvc_Retraction(models.Model):
  title = models.CharField(default=None, blank=True, null=True)
  notice_date = models.CharField(default=None, blank=True, null=True)
  notice_type = models.CharField(default=None, blank=True, null=True)
  trigger_num = models.CharField(default=None, blank=True, null=True)
  trigger_date = models.CharField(default=None, blank=True, null=True)
  trigger_time = models.CharField(default=None, blank=True, null=True)
  sequence_num = models.BigIntegerField(default=None, blank=True, null=True)
  trigger_id = models.CharField(default=None, blank=True, null=True)
  misc = models.CharField(default=None, blank=True, null=True)
  comments = models.CharField(default=None, blank=True, null=True)
  event_date_utc = models.DateTimeField(default=format_trigger_date(trigger_date, trigger_time), blank=True, null=True)
  message = models.ForeignKey(Message, on_delete=models.CASCADE, default=None)

class Meta(object):
  app_label = 'ipn'
  db_table = 'ipn_lvc_retraction'
