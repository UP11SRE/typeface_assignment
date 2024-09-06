# Typeface Backend Assignment (Dropbox service)

## Project Overview:

This project implements a simplified Dropbox-like service that allows users to upload, retrieve, update, delete, and list files through a set of RESTful APIs. The service is built using Django and Django Rest Framework (DRF), providing a robust and scalable solution for file management.

## Features:

- Upload File: Users can upload files, which are stored in the server's file system, and their metadata is saved in a SQLite database.
- Read File: Users can retrieve files based on their unique identifiers.

- Update File: Users can update existing files and their metadata. When a new file is uploaded, the old file is deleted from the server to prevent orphaned files.

- Delete File: Users can delete specific files based on their unique identifiers, which also removes the file from the server's file system.

- List Files: Users can list all available files along with their metadata.

## File Storage:

- Files are stored in the media/ directory of the project. When a user uploads a file, the file is saved in this directory, and its metadata (including the file name, size, type, and path) is stored in the SQLite database.

- When a user updates a file, the old file is deleted from the server's file system before saving the new file. Similarly, when a file is deleted, it is removed from both the database and the file system.

## Technologies Used:

- Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.

- Django Rest Framework (DRF): A powerful toolkit for building Web APIs in Django.

- SQLite: A lightweight database for storing file metadata.

- Python: The programming language used for developing the application.

## Installation Instructions:

- Clone the Repository:

  git clone <https://github.com/UP11SRE/typeface_assignment.git>

  cd typeface_assignment

- Set Up a Virtual Environment:

  python -m venv venv

  Activate the script: cd `.\.venv\Scripts\Activate`

- Install Dependencies:

  pip install -r requirements.txt

- Run Migrations:

  python manage.py migrate

- Start the Development Server:

  python manage.py runserver

- Access the API: The API will be available at http://127.0.0.1:8000/api/.

## Run with Docker:

To run the project easily using Docker, We have a Docker image. Here’s a basic outline of how to use that image:

- Build the Docker Image:

  docker build -t typeface_assignment .

- Run the Docker Container:

  docker run -p 8000:8000 typeface_assignment

## API Endpoints

1. Upload File Endpoint: POST /api/files/upload

Request Method: POST

URL: http://127.0.0.1:8000/api/files/upload

Body: Form-data

Key: file

Value: [Select the file you want to upload]

Response:

Success: json

    {
      "message": "File uploaded successfully",
      "file_id": 1  // Example file ID
    }
    ```

Error:
json

    {
      "message": "No file provided"
    }
    ```

2. Read File Endpoint: GET /api/files/{file_id}

Request Method: GET

URL: http://127.0.0.1:8000/api/files/{file_id}

Replace {file_id} with the actual ID of the file you want to retrieve (e.g., http://127.0.0.1:8000/api/files/1).

Response:

Success: File binary data.

Error:
json

    {
      "message": "File not found"
    }
    ```

3. Update File Endpoint: PUT /api/files/update/{file_id}

Request Method: PUT

URL: http://127.0.0.1:8000/api/files/update/{file_id}

Replace {file_id} with the ID of the file you want to update (e.g., http://127.0.0.1:8000/api/files/update/1).

Body: Form-data

Key: file

Value: [Select the new file you want to upload]

Response:

Success json:

    {
      "id": 1,
      "file_name": "new_file_name.pdf",
      "created_at": "2024-09-06T12:51:16Z",
      "file_size": 2048,
      "file_type": "application/pdf",
      "file_path": "/media/new_file_name.pdf"
    }
    ```

Error json:

    {
      "message": "No file provided"
    }
    ```

4. Delete File Endpoint: DELETE /api/files/delete/{file_id}

Request Method: DELETE

URL: http://127.0.0.1:8000/api/files/delete/{file_id}

Replace {file_id} with the ID of the file you want to delete (e.g., http://127.0.0.1:8000/api/files/delete/1).

Response:

Success json:

    {
      "message": "File deleted successfully"
    }
    ```

Error json:

    {
      "message": "File not found"
    }
    ```

5. List Files Endpoint: GET /api/files

Request Method: GET

URL: http://127.0.0.1:8000/api/files

Response:

Success json:

    {
      "files": [
        {
          "id": 1,
          "file_name": "Investment Memo.pdf",
          "created_at": "2024-09-06T12:51:16Z",
          "file_size": 1024,
          "file_type": "application/pdf",
          "file_path": "/media/Investment Memo.pdf"
        },
        {
          "id": 2,
          "file_name": "Naman_New(INSTA).pdf",
          "created_at": "2024-09-06T12:51:16Z",
          "file_size": 2048,
          "file_type": "application/pdf",
          "file_path": "/media/Naman_New(INSTA).pdf"
        }
      ]
    }

## Error Handling

The API provides meaningful error messages and appropriate HTTP status codes for various scenarios, such as:

- 400 Bad Request: When no file is provided.
- 404 Not Found: When a file does not exist.
- 500 Internal Server Error: For unexpected errors.
