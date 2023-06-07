from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.IndexView.as_view(), name='index_view'),
    path("load-more-films-index/",
         views.IndexView.load_more_films, name="load-more-films-index"),
    path("load-more-films-index/genre/<str:genre>/",
         views.GenreView.load_more_films, name="load-more-films-genre"),
    path('films/<str:film>/',views.FilmView.as_view(), name='film_view'),
    path("films/genre/<str:genre>/", views.GenreView.as_view(), name="genre_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
