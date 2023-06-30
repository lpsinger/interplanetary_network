from django.contrib import admin
from .models import Message, Lvc_Preliminary, Test_Lvc_Preliminary, Integral_Pointing_Direction, Lvc_Retraction

admin.site.register(Message)
admin.site.register(Lvc_Preliminary)
admin.site.register(Test_Lvc_Preliminary)
admin.site.register(Integral_Pointing_Direction)
admin.site.register(Lvc_Retraction)
