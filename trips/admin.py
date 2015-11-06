from django.contrib import admin
from trips.models import Trip, Experience, Picture

# Add in this class to customized the Admin Interface
class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 0

class PictureInline(admin.StackedInline):
    model = Picture
    extra = 0
    
class TripAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    inlines = [ExperienceInline]
    
class ExperienceAdmin(admin.ModelAdmin):
    inlines = [PictureInline]   

# Update the registeration to include this customised interface
admin.site.register(Trip, TripAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Picture)