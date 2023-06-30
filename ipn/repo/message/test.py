from ipn.repo.shared_utils import format_trigger_date
from ipn.models.Message import Message
import json
from ipn.repo.lvc_preliminary import try_retract_by_trigger_num
import traceback
from ipn.jobs.scan_for_groupings import scan_groups_by_message
# this is just for testing
def test():
  try:
    scan_groups_by_message()
        # MS230629p
  except Exception as e:
    print(e)
    traceback.print_exc()
    # loaded_message = json.loads(message_json)
    # print(loaded_message["TRIGGER_DATE"])
    # message.event_date_utc = format_trigger_date(message.trigger_date, message.trigger_time)
    # message.save()
    # results = Profile.objects.filter(preferences__daily_email=True)
    # print(message.message_json)
