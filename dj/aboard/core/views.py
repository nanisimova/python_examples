from sphinxapi import SphinxClient

from django.shortcuts import render

from catalog.models import Catalog
from core.forms import SearchForm

def main(request):

    form = SearchForm()
    return render(request, 'index.html', {'form': form })


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_string = form.cleaned_data['search_string']
            s = SphinxClient()
            s.SetServer('192.168.102.2', 9312)
            s.SetLimits(0, 100)
            if s.Status():
                res = s.Query(search_string)
                return render(request, 'search.html', {'items': res, 'form': form })

    form = SearchForm()
    return render(request, 'search.html', {'form': form })