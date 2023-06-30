from ipn.models.Message import Message
from datetime import timedelta
import json

def scan_groups_by_message():
  result = {
    "messages": [],
  }
  grouping_detected = False
  for message in Message.objects.all():
    if message.event_date_utc:
      message_group = Message.objects.filter(event_date_utc=(message.event_date_utc + timedelta(seconds=100)))
      for msg in message_group:
        result["messages"].append(msg.id)

  print(result)
