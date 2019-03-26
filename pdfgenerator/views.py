from pdfgenerator.forms import UploadForm
from pdfgenerator.helpers import convert_doc_to_pdf
from pdfgenerator.models import Upload, Converted_Pdf, Queue
from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from django.core.files.storage import default_storage
from wsgiref.util import FileWrapper
from django.conf import settings


import os


def upload(request):
    html = "upload.html"
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            source_file = form.save()

            filename = str(form.cleaned_data["file"])
            name, ext = filename.rsplit(".")
            name = name.rsplit("/")[-1]
            queue = Queue.objects.create(source=source_file)

            # converted_pdf = Converted_Pdf.objects.filter(pk=)
            return render(
                request, html, {"message": f"Successfully Uploaded {filename}"}
            )

    else:
        form = UploadForm()
    return render(request, html, {"form": form})


def download(request, file_id):
    html = "download.html"
    file = get_object_or_404(Converted_Pdf, pk=file_id)
    name = str(file).rsplit("/")[0]
    path = f"{settings.MEDIA_URL}/pdfs/{name}"
    return render(request, html, {"path": path, "name": name})

