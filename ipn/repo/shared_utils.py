import zoneinfo
from django.utils.dateparse import parse_datetime

def format_trigger_date(date, time):
  date_list = str(date).split(';')
  date_found = list(filter(lambda x: '(yyyy/mm/dd)' in x, date_list))

  if not date_found:
    return None

  date_formatted = date_found[0].replace('(yyyy/mm/dd)', '').lstrip().rstrip().replace('/', '-')
  time_list = str(time).split('SOD')
  time_found = list(filter(lambda x: 'UT' in x, time_list))
  time_formatted = time_found[0].replace('{', '').replace('} UT', '')
  full_datetime_string = date_formatted + time_formatted
  naivedatetime = parse_datetime(full_datetime_string)

  return naivedatetime.replace(tzinfo=zoneinfo.ZoneInfo("UTC"))

