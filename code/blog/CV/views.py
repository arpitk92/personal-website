from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf.urls.static import static
from django.conf import settings

# Create your views here.
class DownloadCV(APIView):
    def get(self, request):
        static_file_path = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        pdf_path = f'{static_file_path}/assets/CV(Arpit Khanna).pdf'
        pdf_data = open(pdf_path, 'rb').read()
        return Response(pdf_data, mimetype='application/pdf')