from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    
    def __str__(self):
        return f"{self.title}"
    
class Folder(models.Model):
    title = models.CharField(max_length=120)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.DO_NOTHING)
    document = models.ForeignKey(Document, blank=True, null=True, related_name='document', on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"{self.title}"

class Guideline(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.PROTECT) # TODO: adjust after create Folder
    
    def __str__(self):
        return f"{self.title}"
