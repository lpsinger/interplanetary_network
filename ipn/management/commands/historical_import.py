from django.core.management.base import BaseCommand, CommandError
from ipn.listeners.historical_gcn_import import historical_import

class Command(BaseCommand):
  help = "starts listener for kafka"

  def handle(self, *args, **options):
    try:
      historical_import()
    except Exception as e:
      print("ERROR at command level")
      print(e)
