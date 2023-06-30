from gcn_kafka import Consumer
from ipn.repo.message.process import process

def listen():
  consumer = Consumer(
    client_id='redacted',
    client_secret='redacted',
    domain='gcn.nasa.gov')

  topics = [
    'gcn.classic.text.FERMI_GBM_ALERT',
    'gcn.classic.text.INTEGRAL_SPIACS',
    'gcn.classic.text.LVC_INITIAL',
    'gcn.classic.text.LVC_PRELIMINARY',
    'gcn.classic.text.LVC_RETRACTION',
    'gcn.classic.text.LVC_UPDATE']
  consumer.subscribe(topics)
  # this topic can cause a segfault so I removed it for now
  # 'gcn.classic.text.SWIFT_BAT_GRB_ALERT',

  while True:
    for message in consumer.consume(timeout=1):
      print('-------------------------------------------')
      print('message would be queued for processing here')
      try:
        print("@@@@@@@@@@@@@@@@@")
        print(message.value())
        print("@@@@@@@@@@@@@@@@@")
        process(message.value())
      except Exception as e:
        print("!!!!! LISTENER ERROR: !!!!!")
        print(e)
