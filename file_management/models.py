from django.db import models

class File(models.Model):
    file_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=50)
    file_path = models.CharField(max_length=500)  # Stores the path to the file in the file system

    def __str__(self):
        return self.file_name  # Enhances readability in the admin interface