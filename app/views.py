from django.http import HttpResponseRedirect
from rest_framework import generics

from app.models import URLMapper
from app.serializers import URLMapperSerializer


class FetchURL(generics.ListCreateAPIView):
    queryset = URLMapper.objects.all()
    serializer_class = URLMapperSerializer

    def get_queryset(self):
        date_from = self.request.GET.get("from")
        if date_from is not None:
            date_to = self.request.GET.get("to")
            return URLMapper.objects.filter(create__lte=date_to, create__gte=date_from)
        search_value = self.request.GET.get("search", "")
        return URLMapper.objects.filter(url__contains=search_value)


class FetchShortURL(generics.RetrieveAPIView):
    queryset = URLMapper.objects.all()
    serializer_class = URLMapperSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return HttpResponseRedirect(redirect_to=instance.url)
