from ipn.models.Test_Integral_Spi_Acs_Trigger import Test_Integral_Spi_Acs_Trigger

def create_test_integral_spi_acs_trigger_from_message(message_json, message):
  Test_Integral_Spi_Acs_Trigger.objects.create(
    title = message_json.get('TITLE', None),
    notice_date = message_json.get('TITLE', None),
    notice_type = message_json.get('NOTICE_TYPE', None),
    trigger_num = message_json.get('TRIGGER_NUM', None),
    trigger_date = message_json.get('TRIGGER_DATE', None),
    trigger_time = message_json.get('TRIGGER_TIME', None),
    grb_inten = message_json.get('GRB_INTEN', None),
    grb_time = message_json.get('GRB_TIME', None),
    grb_date = message_json.get('GRB_DATE', None),
    comments = message_json.get('COMMENTS', None),
    message = message
  )
