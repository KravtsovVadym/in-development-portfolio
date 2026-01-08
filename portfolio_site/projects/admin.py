from django.contrib import admin
from .models import Project, Profile, Skill, SkillIcon


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(SkillIcon)
