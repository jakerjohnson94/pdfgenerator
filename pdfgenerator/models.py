from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

fs_upload = FileSystemStorage(location="pdfgenerator/media/uploads/")
fs_pdf = FileSystemStorage(location="pdfgenerator/media/pdfs/")


class Upload(models.Model):
    file = models.FileField(storage=fs_upload)
    created = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(
        User,
        verbose_name="Uploader",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        name = self.file.name.split("/")[-1]
        return name


class Converted_Pdf(models.Model):
    file = models.FileField(storage=fs_pdf, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        name = self.file.name.split("/")[-1]
        return name


class Queue(models.Model):
    source = models.ForeignKey(
        Upload, verbose_name="Source File", on_delete=models.CASCADE
    )
    completed = models.BooleanField("Completed", default=False)

    def __str__(self):
        return self.source.file.name
