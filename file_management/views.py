from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.conf import settings
import os

from .models import File
from .serializers import FileSerializer

@api_view(['POST'])
def upload_file(request):
  """
  Upload a file and save its metadata.
  """
  try:
    file = request.FILES.get('file')
    if not file:
      return Response({'message': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

  # Create and save file metadata
    file_metadata = File(
      file_name=file.name,
      file_size=file.size,
      file_type=file.content_type,
      file_path=file_path
    )
    file_metadata.save()
    return Response({'message': 'File uploaded successfully', 'file_id': file_metadata.id}, status=status.HTTP_201_CREATED)
  except Exception as e:
    return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def read_file(request, file_id):
  """
  Retrieve a specific file based on its ID.
  """
  try:
      file = File.objects.get(id=file_id)
      file_path = file.file_path

      if not os.path.exists(file_path):
          return Response({'message': 'File not found'}, status=status.HTTP_404_NOT_FOUND)

      response = FileResponse(open(file_path, 'rb'), content_type=file.file_type)
      response['Content-Disposition'] = f'attachment; filename="{file.file_name}"'
      return response
  except File.DoesNotExist:
      return Response({'message': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
  except Exception as e:
      return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_file(request, file_id):
  """
  Update an existing file or its metadata, deleting the old file if a new one is uploaded.
  """
  try:
      file = File.objects.get(id=file_id)

      if 'file' in request.FILES:
          # Delete the old file from the file system
          if os.path.exists(file.file_path):
              os.remove(file.file_path)

          fs = FileSystemStorage()
          filename = fs.save(request.FILES['file'].name, request.FILES['file'])
          file_path = os.path.join(settings.MEDIA_ROOT, filename)

          # Update the file metadata
          file.file_path = file_path
          file.file_name = request.FILES['file'].name
          file.file_size = request.FILES['file'].size
          file.file_type = request.FILES['file'].content_type
          file.save()

          serializer = FileSerializer(file)
          return Response(serializer.data, status=status.HTTP_200_OK)

      return Response({'message': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
  except File.DoesNotExist:
      return Response({'message': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
  except Exception as e:
      return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_file(request, file_id):
  """
  Delete a specific file based on its ID.
  """
  try:
      file = File.objects.get(id=file_id)
      if os.path.exists(file.file_path):
          os.remove(file.file_path)
      file.delete()
      return Response({'message': 'File deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
  except File.DoesNotExist:
      return Response({'message': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
  except Exception as e:
      return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def list_files(request):
  """
  List all available files and their metadata.
  """
  try:
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  except Exception as e:
      return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)