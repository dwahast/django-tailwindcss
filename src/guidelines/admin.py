from django.contrib import admin

from .models import Guideline, Document, Folder
# Register your models here.

admin.site.register(Guideline)
admin.site.register(Document)
admin.site.register(Folder)