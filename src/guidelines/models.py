from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    
class Folder(models.Model):
    title = models.CharField(max_length=120)
    # children = models.ManyToManyField('self', blank=True, null=True,)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.PROTECT)
    content = models.ManyToManyField(Document)

class Guideline(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    folderId = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.PROTECT) # TODO: adjust after create Folder
