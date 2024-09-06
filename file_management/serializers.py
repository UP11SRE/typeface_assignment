from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
       class Meta:
           model = File
           fields = ['id', 'file_name', 'created_at', 'file_size', 'file_type', 'file_path']