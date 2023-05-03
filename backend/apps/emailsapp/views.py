from rest_framework import viewsets
from .serializers import EmailSerializer
from .models import Email


class EmailViewSet(viewsets.ModelViewSet):
    serializer_class = EmailSerializer

    def get_queryset(self):
        queryset = Email.objects.all()
        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset
