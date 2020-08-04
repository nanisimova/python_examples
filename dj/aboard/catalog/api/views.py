from rest_framework import generics
from catalog.models import Catalog
from catalog.api.serializers import CatalogSerializer


class CatalogListView(generics.ListAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


