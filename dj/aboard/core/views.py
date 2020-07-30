from django.shortcuts import render

from catalog.models import Catalog

def main(request):
    return render(request, 'index.html')