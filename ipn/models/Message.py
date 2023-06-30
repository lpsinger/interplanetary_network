from django.db import models
from ipn.repo.message.message import format_event_date

class Message(models.Model):
  received = models.DateTimeField()
  message_json = models.JSONField(default=dict, help_text='Message in JSONSchema')
  notice_type = models.CharField(default=None, blank=True, null=True)
  event_date_utc = models.DateTimeField(default=format_event_date(message_json), blank=True, null=True)

class Meta(object):
  app_label = 'ipn'
  db_table = 'ipn_message'
