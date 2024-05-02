from django.db import models

class FileMetadata(models.Model):
    filename = models.CharField(max_length=15)
    prefix = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2)
    insertion_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'file_metadata'

    def __str__(self):
        return self.file_name
    