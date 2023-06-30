from django.shortcuts import render
from ipn.models.Message import Message
from ipn.models.Lvc_Preliminary import Lvc_Preliminary

def get_message(request, id):
  message = Message.objects.get(id=id)
  related_lvc_data = Lvc_Preliminary.objects.filter(message_id=id).values()[0]

  context = {
    "message": message,
    "lvc_data": related_lvc_data
  }
  return render(request, "message_detail.html", context)

def get_messages(request):
  messages = Message.objects.all()
  context = {
    "messages": messages
  }
  return render(request, "messages_index.html", context)
