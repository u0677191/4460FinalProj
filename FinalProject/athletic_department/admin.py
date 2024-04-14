from django.contrib import admin
from .models import Team, Employee, Athlete, Equipment, Event


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'net_income_s1', 'net_income_s2')

    def net_income_s1(self, obj):
        return obj.incomeS1 - obj.costS1
    net_income_s1.short_description = 'Net Income Season 1'

    def net_income_s2(self, obj):
        return obj.incomeS2 - obj.costS2
    net_income_s2.short_description = 'Net Income Season 2'    

admin.site.register(Team, TeamAdmin)
admin.site.register(Employee)
admin.site.register(Athlete)
admin.site.register(Equipment)
admin.site.register(Event)