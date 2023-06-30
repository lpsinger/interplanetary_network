from ipn.models.Integral_Pointing_Direction import Integral_Pointing_Direction

def create_integral_pointing_direction_from_message(message_json, message):
  Integral_Pointing_Direction.objects.create(
    title = message_json.get('TITLE', None),
    notice_date = message_json.get('NOTICE_DATE', None),
    notice_type = message_json.get('NOTICE_TYPE', None),
    next_point_ra = message_json.get('NEXT_POINT_RA', None),
    next_point_dec = message_json.get('NEXT_POINT_DEC', None),
    slew_time = message_json.get('SLEW_TIME', None),
    slew_date = message_json.get('SLEW_DATE', None),
    sun_postn = message_json.get('SUN_POSTN', None),
    sun_dist = message_json.get('SUN_DIST', None),
    moon_postn = message_json.get('MOON_POSTN', None),
    moon_dist = message_json.get('MOON_DIST', None),
    gal_coords = message_json.get('GAL_COORDS', None),
    ecl_coords = message_json.get('ECL_COORDS', None),
    comments = message_json.get('COMMENTS', None),
    message = message
  )
