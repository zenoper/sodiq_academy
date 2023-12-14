import mimetypes
from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path

def serve_file(request, file_path):
    # Your other view logic here

    # Get the file extension and determine the content type
    file_extension = Path(file_path).suffix
    content_type, encoding = mimetypes.guess_type(file_path)
    if not content_type:
        content_type = 'application/octet-stream'  # Default content type for unknown file types

    # Create an HttpResponse object and set the content type
    response = HttpResponse(content_type=content_type)

    # Render the file
    return render(request, file_path, context={}, HttpResponse=response)

def landing_page(request):
    # Your landing page view logic here
    return render(request, 'SodiqAcademy/index.html', context={})
