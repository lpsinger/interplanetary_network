from gcn_kafka import Consumer
from ipn.repo.message.process import process

config = {'group.id': '',
          'auto.offset.reset': 'earliest'}

consumer = Consumer(config=config,
                    client_id='5ft47ajoahp4a84cu367fh7kqa',
                    client_secret='rffk4b9hkbhujhhcvid215qm08ujnqr58u16ufuaa7r8gr3lkkl',
                    domain='gcn.nasa.gov')

topics = [
  'gcn.classic.text.FERMI_GBM_ALERT',
  'gcn.classic.text.INTEGRAL_SPIACS',
  # 'gcn.classic.text.SWIFT_BAT_GRB_ALERT',
  'gcn.classic.text.LVC_INITIAL',
  'gcn.classic.text.LVC_PRELIMINARY',
  'gcn.classic.text.LVC_RETRACTION',
  'gcn.classic.text.LVC_UPDATE']
consumer.subscribe(topics)

while True:
  for message in consumer.consume(timeout=1):
    print("@@@@@@@@@@@@@@@@@")
    print(message.value())
    print("@@@@@@@@@@@@@@@@@")
    process(message.value())
