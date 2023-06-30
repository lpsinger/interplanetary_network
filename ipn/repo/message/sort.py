from ipn.repo.integral_pointing_direction import create_integral_pointing_direction_from_message
from ipn.repo.integral_spi_acs_trigger import create_integral_spi_acs_trigger_from_message
from ipn.repo.lvc_update_skymap import create_lvc_update_skymap_from_message
from ipn.repo.test_integral_spi_acs_trigger import create_test_integral_spi_acs_trigger_from_message
from ipn.repo.test_lvc_initial_skymap import create_test_lvc_initial_skymap_from_message
from ipn.repo.test_lvc_preliminary import create_test_lvc_preliminary_from_message
from ipn.repo.lvc_retraction import create_lvc_retraction_from_message
from ipn.repo.lvc_preliminary import create_lvc_preliminary_from_message

def sort(message_dict, message):
  print("sorting message type:")
  print(message_dict["NOTICE_TYPE"])

  if (message_dict["NOTICE_TYPE"] == "TEST LVC Initial Skymap"):
    create_test_lvc_initial_skymap_from_message(message_dict, message)

  elif (message_dict["NOTICE_TYPE"] == "LVC Update Skymap"):
    create_lvc_update_skymap_from_message(message_dict, message)

  elif (message_dict["NOTICE_TYPE"] == "TEST INTEGRAL SPI ACS Trigger"):
    create_test_integral_spi_acs_trigger_from_message(message_dict, message)

  elif (message_dict["NOTICE_TYPE"] == "INTEGRAL SPI ACS Trigger"):
    create_integral_spi_acs_trigger_from_message(message_dict, message)

  elif (message_dict["NOTICE_TYPE"] == "TEST LVC Preliminary"):
    create_test_lvc_preliminary_from_message(message_dict, message)

  elif (message_dict["NOTICE_TYPE"] == "INTEGRAL Pointing Direction"):
    create_integral_pointing_direction_from_message(message_dict, message)

  elif (message_dict["NOTICE_TYPE"] == "LVC Retraction"):
    create_lvc_retraction_from_message(message_dict, message)

  elif (message_dict["NOTICE_TYPE"] == "LVC Preliminary"):
    create_lvc_preliminary_from_message(message_dict, message)

  else:
    print("UNSORTED MESSAGE TYPE:")
    print(message_dict["NOTICE_TYPE"])
