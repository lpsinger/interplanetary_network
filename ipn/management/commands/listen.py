from django.core.management.base import BaseCommand, CommandError
from ipn.listeners.gcn_listener import listen

class Command(BaseCommand):
  help = "starts listener for kafka"

  def handle(self, *args, **options):
    try:
      listen()
    except Exception as e:
      print("ERROR at command level")
      print(e)
