import sys
import os
import subprocess


def convert_doc_to_pdf(docs):
    for doc in docs:
        name, ext = doc.split(".")
        initial_path = os.path.abspath(f"pdfgenerator/media/uploads/{doc}")
        destination_path = os.path.abspath(
            f"pdfgenerator/media/pdfs/{name}.pdf"
        )

        # if not os.path.isdir("pdfgenerator/static/pdfs"):
        #     os.mkdir("pdfgenerator/static/pdfs")

        try:
            output = subprocess.check_output(
                ["pandoc", initial_path, "-s", "-o", destination_path]
            )
            return destination_path
        except Exception:
            print("Something went wrong. Ensure File type is valid.")

