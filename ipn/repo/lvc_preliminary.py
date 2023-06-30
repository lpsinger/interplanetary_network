from ipn.models.Lvc_Preliminary import Lvc_Preliminary
from ipn.models.Lvc_Retraction import Lvc_Retraction

def create_lvc_preliminary_from_message(message_json, message):
  Lvc_Preliminary.objects.create(
    title = message_json.get('TITLE', None),
    notice_date = message_json.get('NOTICE_DATE', None),
    notice_type = message_json.get('NOTICE_TYPE', None),
    trigger_num = message_json.get('TRIGGER_NUM', None),
    trigger_date = message_json.get('TRIGGER_DATE', None),
    trigger_time = message_json.get('TRIGGER_TIME', None),
    group_type = message_json.get('GROUP_TYPE', None),
    search_type = message_json.get('SEARCH_TYPE', None),
    pipeline_type = message_json.get('PIPELINE_TYPE', None),
    far = message_json.get('FAR', None),
    trigger_id = message_json.get('TRIGGER_ID', None),
    misc = message_json.get('MISC', None),
    skymap_fits_url = message_json.get('SKYMAP_FITS_URL', None),
    eventpage_url = message_json.get('EVENTPAGE_URL', None),
    comments = message_json.get('COMMENTS', None),
    message = message
  )

def try_retract_by_trigger_num(trigger_num):
  lvc_data = Lvc_Preliminary.objects.filter(trigger_num=trigger_num).first()
  lvc_retraction = Lvc_Retraction.objects.filter(trigger_num=trigger_num).first()

  if (lvc_data is not None and lvc_retraction is not None):
    lvc_data.lvc_retraction = lvc_retraction
    lvc_data.save(update_fields=['lvc_retraction'])
