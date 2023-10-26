from rest_framework import status
from rest_framework.response import Response
from api.models import File
from api.serializers import FileSerializer
from rest_framework import viewsets
from rest_framework.decorators import action

from api.tasks import process_file


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    http_method_names = ['get', 'post']

    @action(methods=['post'],
            detail=False,
            url_path='upload',
            url_name='upload')
    def upload_file(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            process_file.delay(serializer.data.get('id'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
