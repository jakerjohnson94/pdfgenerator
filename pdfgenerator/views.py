from pdfgenerator.forms import UploadForm
from django.shortcuts import redirect, render
from pdfgenerator.helpers import convert_doc_to_pdf
from pdfgenerator.models import Upload
import os


def model_form_upload(request):
    html = "upload_form.html"
    conversion_queue = []
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            filename = str(form.cleaned_data["upload"])
            conversion_queue.append(filename)
            convert_doc_to_pdf(conversion_queue)
            return redirect("home")
    else:
        form = UploadForm()
    return render(request, html, {"form": form})


def download_view(request):
    pass
