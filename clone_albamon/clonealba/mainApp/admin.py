from django.contrib import admin
from .models import notice, comment

# Register your models here.

admin.site.register(notice),
admin.site.register(comment),