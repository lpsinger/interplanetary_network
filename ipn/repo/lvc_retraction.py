from ipn.models.Lvc_Retraction import Lvc_Retraction
from ipn.repo.lvc_preliminary import try_retract_by_trigger_num

def create_lvc_retraction_from_message(message_json, message):
  retraction = Lvc_Retraction.objects.create(
    title = message_json.get('TITLE', None),
    notice_date = message_json.get('NOTICE_DATE', None),
    notice_type = message_json.get('NOTICE_TYPE', None),
    trigger_num = message_json.get('TRIGGER_NUM', None),
    trigger_date = message_json.get('TRIGGER_DATE', None),
    trigger_time = message_json.get('TRIGGER_TIME', None),
    sequence_num = message_json.get('SEQUENCE_NUM', None),
    trigger_id = message_json.get('TRIGGER_ID', None),
    misc = message_json.get('MISC', None),
    comments = message_json.get('COMMENTS', None),
    message = message
  )

  try_retract_by_trigger_num(retraction.trigger_num)
