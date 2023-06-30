from django.core.management.base import BaseCommand, CommandError
from ipn.repo.message.test import test

class Command(BaseCommand):
  help = "helps me test things"
  def add_arguments(self, parser):
    parser.add_argument('mid', nargs='*', type=int, help='message id')

  def handle(self, *args, **kwargs):
    print(kwargs)
    try:
      test()
    except Exception as e:
      print("ERROR")
      print(e)
