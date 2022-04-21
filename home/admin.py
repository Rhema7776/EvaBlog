from django.contrib import admin

# Register your models here.

from .models import Todo,Taglag,Tag_level,Tagjob,Dev

admin.site.register(Todo)
admin.site.register(Taglag)
admin.site.register(Tag_level)
admin.site.register(Tagjob)
admin.site.register(Dev)
