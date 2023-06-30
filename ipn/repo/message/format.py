import json
import xmltodict

def format_message(body):
  message_dict = format_body(body)
  return format_fields(message_dict)

def format_body(body):
  if (isinstance(body, (bytes))):
    return format_byte_message(body)
  try:
    return xmltodict.parse(body)
  except:
    print("@@@@ UNHANDLED FILE FORMAT @@@")
    print(body)

def format_byte_message(body):
  message_string = body.decode('utf-8')
  split_message = message_string.splitlines()
  result = {}
  previous_field = ''
  for line in split_message:
    new_line = line.split(":")
    line_length = len(new_line)
    if ((new_line[0] == previous_field) and (new_line[0] == 'COMMENTS')):
      result[previous_field] = result[previous_field] + "\n" + new_line[1].lstrip().rstrip()
    elif (line_length == 2):
      result[new_line[0]] = new_line[1].lstrip().rstrip()
      previous_field = new_line[0]
    elif (line_length > 2):
      field_to_remove = new_line[0]+":"
      result[new_line[0]] = line.replace(field_to_remove, '').lstrip().rstrip()
      previous_field = new_line[0]
    elif (line_length == 1):
      result[previous_field] = result[previous_field] + "\n" + new_line[0].lstrip().rstrip()
    else:
      error = "unexpected byte line length:" + str(len(new_line))
      print(error)
  return result

def format_fields(message_dictionary):
  fully_formatted_message = {}
  for key, value in message_dictionary.items():
    if (key == 'GRB_RA' or key == 'GRB_DEC'):
      fully_formatted_message[key] = value.split('\n')
    else:
      fully_formatted_message[key] = value
  return fully_formatted_message
