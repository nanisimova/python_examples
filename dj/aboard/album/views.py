from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect

from album.forms import CreatePhotoForm
from album.models import Photo

def create_photo(request, item_id):
    if request.user.is_authenticated:
        if not int(item_id) > 0:
            return HttpResponseRedirect('/')

        if request.method == 'POST':
            form = CreatePhotoForm(request.POST, request.FILES)
            if form.is_valid():
                rec = Photo(
                    catalog_id = item_id,
                    name = form.cleaned_data['image'],
                    image = form.cleaned_data['image'],
                )
                rec.save()

            return HttpResponseRedirect('/catalog/view/' + item_id)
        else:
            form = CreatePhotoForm()
            return render(request, 'album/create_photo.html', {'form': form, 'item_id': item_id})


    else:
        return HttpResponseRedirect('/auth/login')


def delete_photo(request, item_id, photo_id):
    if request.user.is_authenticated:
        Photo.objects.get(id = photo_id).delete()
        return HttpResponseRedirect('/catalog/view/' + item_id)
    else:
        return HttpResponseRedirect('/auth/login')


