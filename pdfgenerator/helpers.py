import sys
import os
import subprocess
import time
from django.conf import settings


def convert_doc_to_pdf(doc):
    filename, ext = doc.split(".")
    initial_path = os.path.join(settings.MEDIA_ROOT, f"uploads/{doc}")
    destination_path = os.path.join(settings.MEDIA_ROOT, f"pdfs/{filename}.pdf")

    pdf_path = os.path.join(settings.MEDIA_ROOT, "pdfs")
    if not os.path.isdir(pdf_path):
        os.mkdir(pdf_path)

    try:
        output = subprocess.check_output(
            [
                settings.PANDOC_PATH,
                initial_path,
                "-s",
                "--pdf-engine",
                settings.PDF_ENGINE_PATH,
                "-o",
                destination_path,
            ]
        )
        return destination_path
    except Exception as e:
        print(f"Something went wrong. Ensure File type is valid. {e}")

