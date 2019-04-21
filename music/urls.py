from django.urls import path

from django.contrib import admin
from django.urls import path, include
from .views import ListSongsView, ListSongsByArtistView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('songsbyartist/', ListSongsByArtistView.as_view(), name="songs-by-artist"),
    # path('', views.index, name='index'),
    # path('1', views.index2, name='index2'),
    # path('2', views.index3, name='index3'),x`
]
