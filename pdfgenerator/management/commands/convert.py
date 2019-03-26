from django.core.management.base import BaseCommand, CommandError
from django.shortcuts import get_object_or_404
from pdfgenerator.models import Queue, Converted_Pdf
from pdfgenerator.helpers import convert_doc_to_pdf
import time


class Command(BaseCommand):
    help = "Converts file to pdf"

    def handle(self, *args, **options):
        while True:
            queued_items = Queue.objects.filter(completed=False).order_by(
                "source__created"
            )
            for item in queued_items:

                filename = item.source.file.name
                item.completed = True
                item.save()
                pdf_path = convert_doc_to_pdf(filename)

                new_pdf = Converted_Pdf.objects.create(
                    file=pdf_path, source=item.source
                )

                self.stdout.write(self.style.SUCCESS(f"Converted {filename}"))
            time.sleep(5)
