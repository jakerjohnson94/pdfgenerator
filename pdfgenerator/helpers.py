import sys
import os
import subprocess
import time
from django.conf import settings


def convert_doc_to_pdf(doc):
    if not os.path.isdir(settings.PDF_PATH):
        os.mkdir(settings.PDF_PATH)

    filename, ext = doc.split(".")
    initial_path = os.path.join(settings.UPLOAD_PATH, f"{filename}.{ext}")
    destination_path = os.path.join(settings.PDF_PATH, f"{filename}.pdf")

    call = [
        settings.PANDOC_PATH,
        initial_path,
        "-s",
        "--pdf-engine",
        settings.PDF_ENGINE_PATH,
        "-o",
        destination_path,
    ]

    try:
        subprocess.check_output(call)
        return destination_path

    except Exception as e:
        print(f"Something went wrong. {e}")
        return FileNotFoundError

