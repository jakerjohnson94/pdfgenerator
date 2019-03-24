from django.contrib import admin
from django.urls import path
from pdfgenerator.views import model_form_upload
from pdfgenerator.models import Upload, Download

admin.site.register(Upload)
admin.site.register(Download)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", model_form_upload, name="home"),
]
