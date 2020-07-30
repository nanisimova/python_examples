import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

from album.models import get_photos
from catalog.models import Catalog
from catalog.forms import CreateItemForm, UpdateItemForm

def create_item(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateItemForm(request.POST, request.FILES)
            if form.is_valid():
                rec = Catalog(
                    name = form.cleaned_data['name'],
                    description = form.cleaned_data['description'],
                    create_date = datetime.datetime.today(),
                    user_id = request.user.id,
                    category_id = form.cleaned_data['category'].id,
                )
                rec.save()

            return HttpResponseRedirect('/catalog/view/' + str(rec.id))
        else:
            form = CreateItemForm()
            return render(request, 'catalog/create_item.html', {'form': form})
    else:
        return HttpResponseRedirect('/auth/login')


def update_item(request, item_id):
    if request.user.is_authenticated:
        try:
            res = Catalog.objects.get(id = item_id, user_id = request.user.id)
            print("ARG", res)
            if request.method == 'POST':
                form = UpdateItemForm(request.POST, request.FILES)
                if form.is_valid():
                    res.name = form.cleaned_data['name']
                    res.description = form.cleaned_data['description']
                    res.save()
                return HttpResponseRedirect('/catalog/view/' + item_id)

            else:
                initial = {'name': res.name, 'description': res.description }
                form = UpdateItemForm(initial=initial)

                return render(request, 'catalog/update_item.html', {'form': form, 'item_id': item_id})
        except:
            # такой item не найден
            return HttpResponseNotFound("404")
    else:
        return HttpResponseRedirect('/auth/login')


def delete_item(request, item_id):
    if request.user.is_authenticated:
        res = Catalog.objects.get(id = item_id, user_id = request.user.id)
        res.delete_date = datetime.datetime.today()
        res.is_active = 0
        res.save()

    return render(request, 'catalog/delete_item.html')


def view_item(request, item_id):
    items = Catalog.objects.filter(id = item_id)
    photos = get_photos(item_id)

    if items.count() > 0:
        return render(request, 'catalog/view_item.html', { 'item': items.values_list()[0],
            'photos': photos }, content_type='text/html')
    else:
        return HttpResponseNotFound("404")


def view_catalog(request, offset = 0):
    #Entry.objects.all()[5:10] # OFFSET 5 LIMIT 5
    limit = 10
    items = Catalog.objects.all()[int(offset):limit]

    return render(request, 'catalog/view_catalog.html', { 'items': items.values_list() }, content_type='text/html')

