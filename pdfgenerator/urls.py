from django.contrib import admin
from django.urls import path
from pdfgenerator.views import model_form_upload, pdf_download
from pdfgenerator.models import Upload, Converted_Pdf
from django.conf import settings
from django.conf.urls.static import static


admin.site.register(Upload)
admin.site.register(Converted_Pdf)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", model_form_upload, name="home"),
    path("download/<int:file_id>", pdf_download, name="download"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

