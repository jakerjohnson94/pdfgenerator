from django.contrib import admin
from django.urls import path
from pdfgenerator.views import upload, download
from pdfgenerator.models import Upload, Converted_Pdf, Queue
from django.conf import settings
from django.conf.urls.static import static


admin.site.register(Upload)
admin.site.register(Converted_Pdf)
admin.site.register(Queue)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", upload, name="home"),
    path("download/<int:file_id>", download, name="download"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

