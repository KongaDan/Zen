from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
admin.site.register(Promotion)
admin.site.register(Section)
admin.site.register(CoursSemaines)
class UserAdmin(admin.ModelAdmin):
    model=get_user_model()
    list_display=['username','email','last_name','numero']
admin.site.register(User,UserAdmin)

class HoraireAdmin(admin.ModelAdmin):
    model=Semaines
    list_display=['jour']
admin.site.register(Semaines,HoraireAdmin)

class TacheAdmin(admin.ModelAdmin):
    model=Tache
    list_display=['nom','heure_creation','heure_fin']
    list_filter=['heure_fin']
admin.site.register(Tache,TacheAdmin)

class CoursAdmin(admin.ModelAdmin):
    model=Cours
    list_display=['nom','promotion']
admin.site.register(Cours,CoursAdmin)
