from django.contrib import admin
from .models import Skill, Project, Contact

# Register your models here.


# class skills(admin.ModelAdmin):
#     list_display= ('name', 'img')

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Contact)