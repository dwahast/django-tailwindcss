from django.contrib import admin

# from django.urls import reverse
# from django.utils.http import urlencode
# from django.utils.html import format_html

from .models import Guideline, Document, Folder

# Register your models here.

# admin.site.register(Guideline)
# admin.site.register(Document)
# admin.site.register(Folder)


@admin.register(Guideline)
class GuidelineAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "content")

    # def view_parent_link(self, obj):
    #     result = Document.parent
    #     return result["grade__avg"]

    # view_parent_link.short_description = "Parents"
