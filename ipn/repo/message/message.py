from ipn.repo.shared_utils import format_trigger_date
import json

def format_event_date(message_json):
  try:
    loaded_message = json.loads(message_json)

    if "TRIGGER_DATE" in loaded_message:
      return format_trigger_date(str(loaded_message["TRIGGER_DATE"]), str(loaded_message["TRIGGER_TIME"]))
    else:
      return None
  except Exception as e:
    print(e)
