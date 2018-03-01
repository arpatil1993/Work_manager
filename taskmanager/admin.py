from django.contrib import admin
from taskmanager.models import UserProfile, Task, Project, Developer, Supervisor

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Supervisor)
admin.site.register(Developer)
admin.site.register(Project)
admin.site.register(Task)
