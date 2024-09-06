from django.urls import path
from . import views

urlpatterns = [
  path('files/upload', views.upload_file, name='upload_file'),
  path('files/<int:file_id>', views.read_file, name='read_file'),
  path('files/update/<int:file_id>', views.update_file, name='update_file'),
  path('files/delete/<int:file_id>', views.delete_file, name='delete_file'),
  path('files', views.list_files, name='list_files'),
]