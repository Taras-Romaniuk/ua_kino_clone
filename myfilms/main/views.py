from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Films
from django.views.generic import View, TemplateView
from django.core.serializers import serialize
import json
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        # context = super(IndexView, self).get_context_data(*args, **kwargs)
        films_limit = 20
        films = Films.objects.all()
        paginator = Paginator(films, films_limit)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return {'page_obj': page_obj}

    def load_more_films(request):
        films_limit = 20
        films = Films.objects.all()
        paginator = Paginator(films, films_limit)
        page = int(request.GET.get("page"))
        page_obj = list(paginator.get_page(page))
        serialized_data = serialize("json", page_obj)
        serialized_data = json.loads(
            serialized_data) if page <= paginator.num_pages else ""
        return JsonResponse(data={"page_obj": serialized_data})


class FilmView(TemplateView):
    template_name = 'film.html'

    def get_context_data(self, film, *args, **kwargs):
        # context = super(IndexView, self).get_context_data(*args, **kwargs)
        film_obj = Films.objects.get(pk=film)
        film_obj.film_genre = list(map(lambda elem: elem.strip(), film_obj.film_genre.split(",")))
        return {'film_obj': film_obj}


class GenreView(TemplateView):
    template_name = 'genres.html'

    def get_context_data(self, genre, *args, **kwargs):
        # context = super(IndexView, self).get_context_data(*args, **kwargs)
        films_limit = 20
        films = Films.objects.filter(film_genre__contains=genre).values()
        paginator = Paginator(films, films_limit)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # film_obj.film_genre = film_obj.film_genre.replace(" ", "").split(",")
        return {'page_obj': page_obj, "genre": genre}

    def load_more_films(request, genre):
        films_limit = 20
        page = int(request.GET.get("page"))
        films = Films.objects.filter(film_genre__contains=genre).values()
        paginator = Paginator(films, films_limit)
        page_obj = list(paginator.get_page(page))
        # serialized_data = serialize("json", page_obj) # !!!
        # serialized_data = json.loads(
            # serialized_data) if page <= paginator.num_pages else ""
        return JsonResponse(data={"page_obj": page_obj if page <= paginator.num_pages else ""})
