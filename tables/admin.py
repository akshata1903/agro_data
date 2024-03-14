from django.contrib import admin

from tables.models import Crop, Plot, Soil, Issue, Tool
# Soil, Disease, Issue, Pest
# Register your models here.


#Crop
class CropAdmin(admin.ModelAdmin):
    list_display = ('user','datetime','location','fieldcropid','croptype','cropvariety','name','expecyieldpeh','avgplanthei','expecperi')

admin.site.register(Crop, CropAdmin)

#Plot
class PlotAdmin(admin.ModelAdmin):
    list_display = ('user','datetime','location','field','farm','farmer','plot','rows','columns','plants')

admin.site.register(Plot, PlotAdmin)

#Soil
class SoilAdmin(admin.ModelAdmin):
    list_display = ('user','datetime','location','dailyweat','mintemp','maxtemp','windspeed','humidity','sunshinehrs')

admin.site.register(Soil, SoilAdmin)

#Issue
class IssueAdmin(admin.ModelAdmin):
    list_display = ('user','datetime','location','issueid','solution')

admin.site.register(Issue, IssueAdmin)

#Tool
class ToolAdmin(admin.ModelAdmin):
    list_display = ('user','datetime','location','toolid','toolname','rate')

admin.site.register(Tool, ToolAdmin)