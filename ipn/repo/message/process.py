from datetime import datetime
from django.utils import timezone
import json
import traceback
from .format import format_message
from ipn.models.Message import Message
from .sort import sort
from ipn.repo.event import create_event_from_message

def process(body):
  message_dict = format_message(body)

  try:
    message = Message.objects.create(received=timezone.make_aware(datetime.now()), message_json=json.dumps(message_dict, indent=2), notice_type=message_dict["NOTICE_TYPE"])

  except Exception as e:
    print('ERROR: MESSAGE was not CREATED in processor')
    print(e)
    traceback.print_exc()

  # TODO: remove this once event model is in massive but okay shape
  try:
    sort(message_dict, message)
  except Exception as e:
    print('ERROR: message was not SORTED in processor')
    print(e)
    traceback.print_exc()

  try:
    create_event_from_message(message_dict, message)
  except Exception as e:
    print('ERROR: EVENT was not CREATED in processor')
    print(e)
    traceback.print_exc()

  # if (message_dict["NOTICE_TYPE"] == "LVC Retraction"):
  #   try:
  #     try_retract_by_trigger_num(message_dict["TRIGGER_NUM"])
  #   except Exception as e:
  #     print('ERROR: EVENT was not CREATED in processor')
  #     print(e)
  #     traceback.print_exc()
