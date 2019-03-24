import sys
import os
import subprocess


def convert_doc_to_pdf(docs):
    for doc in docs:
        name, ext = doc.split(".")

        initial_path = os.path.abspath(f"uploads/{doc}")

        # destination_folder = os.
        destination_path = os.path.abspath(f"pdfs/{name}.pdf")
        if not os.path.isdir("pdfs"):
            os.mkdir("pdfs")

        try:
            output = subprocess.check_output(
                ["pandoc", initial_path, "-s", "-o", destination_path]
            )
        except Exception:
            print("Something went wrong. Ensure File type is valid.")


# def make_dir(path):
#     try:
#         os.makedirs()
