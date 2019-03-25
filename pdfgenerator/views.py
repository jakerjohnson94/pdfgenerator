from pdfgenerator.forms import UploadForm
from pdfgenerator.helpers import convert_doc_to_pdf
from pdfgenerator.models import Upload, Converted_Pdf
from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from django.core.files.storage import default_storage
from wsgiref.util import FileWrapper
from django.conf import settings

import os


def model_form_upload(request):
    html = "upload_form.html"
    conversion_queue = []
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            filename = str(form.cleaned_data["file"])
            conversion_queue.append(filename)
            converted_pdf = convert_doc_to_pdf(conversion_queue)
            download = Converted_Pdf.objects.create(file=converted_pdf)
            return redirect("download", download.id)
    else:
        form = UploadForm()
    return render(request, html, {"form": form})


def pdf_download(request, file_id):
    html = "download.html"
    file = get_object_or_404(Converted_Pdf, pk=file_id)
    name = str(file).split("/")[-1]
    path = f"{settings.MEDIA_URL}/pdfs/{name}"
    print(path)
    return render(request, html, {"path": path, "name": name})

