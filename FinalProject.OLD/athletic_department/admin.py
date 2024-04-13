from django.contrib import admin
from .models import Team, Employee, Athlete, Equipment, Event

admin.site.register(Team)
admin.site.register(Employee)
admin.site.register(Athlete)
admin.site.register(Equipment)
admin.site.register(Event)

#test