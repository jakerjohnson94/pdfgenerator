from django.db import models


class Upload(models.Model):
    upload = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Download(models.Model):
    upload = models.FileField(upload_to="pdf/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

