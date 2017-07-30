from django.contrib import admin
from models import Zone, Player, Corp, Kill_PureText, Kill, AttackDetails, Robot

# Register your models here.

admin.site.register(Kill_PureText)

admin.site.register(Zone)
admin.site.register(Player)
admin.site.register(Corp)
admin.site.register(Kill)
admin.site.register(AttackDetails)
admin.site.register(Robot)

