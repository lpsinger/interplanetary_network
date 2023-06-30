from ipn.models.Test_Lvc_Preliminary import Test_Lvc_Preliminary

def create_test_lvc_preliminary_from_message(message_json, message):
  Test_Lvc_Preliminary.objects.create(
    title = message_json.get('TITLE', None),
    notice_date = message_json.get('TITLE', None),
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
    prob_ns = message_json.get('PROB_NS', None),
    prob_remnant = message_json.get('PROB_REMNANT', None),
    prob_bns = message_json.get('PROB_BNS', None),
    prob_nsbh = message_json.get('PROB_NSBH', None),
    prob_bbh = message_json.get('PROB_BBH', None),
    prob_massgap = message_json.get('PROB_MASSGAP', None),
    prob_terres = message_json.get('PROB_TERRES', None),
    message = message
  )
