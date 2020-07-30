from django.conf.urls import url, include
from django.urls import path, re_path
from django.http import HttpResponse, FileResponse
#from catalog import views as catalog_views
from django.conf import settings
from django.views.static import serve

from user import views as user_views
from authentication import views as auth_views
from catalog import views as catalog_views
from album import views as album_views

from core.views import main

def icon(request):
    return FileResponse(open('favicon.ico', 'rb'))

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),

    url(r'^user/create$', user_views.create),
    url(r'^user/view$', user_views.view),
    url(r'^user/delete$', user_views.delete),
    url(r'^user/update$', user_views.update),
    url(r'^user/change_password$', user_views.change_password),

    url(r'^auth/login$', auth_views.auth_login),
    url(r'^auth/logout$', auth_views.auth_logout),
#    url(r'^user/profile$', user_views.profile_user),

    url(r'^catalog/create$', catalog_views.create_item),
    url(r'^catalog/update/(?P<item_id>\d+)$', catalog_views.update_item),
    url(r'^catalog/view/(?P<item_id>\d+)$', catalog_views.view_item),
    url(r'^catalog/delete/(?P<item_id>\d+)$', catalog_views.delete_item),

    url(r'^catalog/update/(?P<item_id>\d+)/photo/create$', album_views.create_photo),
    url(r'^catalog/update/(?P<item_id>\d+)/photo/delete/(?P<photo_id>\d+)$', album_views.delete_photo),

    url(r'^catalog/list/(?P<offset>\d+)$', catalog_views.view_catalog),
    url(r'^catalog/list$', catalog_views.view_catalog),

    url(r'^favicon.ico$', icon),
    url(r'^', main),
    url(r'^/', main),
]
