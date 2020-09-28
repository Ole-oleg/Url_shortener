from django.views.decorators.http import require_http_methods
from requests.exceptions import ConnectionError
from rest_framework.reverse import reverse_lazy
from django.http import JsonResponse
from django.conf import settings
import requests
import random
import string
import redis


database = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


def api_decorator(func):
    def wrapper(request):
        data = func(request)
        return JsonResponse(data)
    return wrapper


@require_http_methods(['GET', 'POST'])
def shortener_universal(request):
    """ Takes url and hum_readable parameters from request, validates given url, returns JSON with 'fail'
    if connection via this url cannot be established. If everything is Ok, function saves url and its slag in
    Redis and returns JSON with some data. """

    url = request.GET.get('url', '')
    slug = request.GET.get('slug', '')

    if '://' in url:
        url = url.split('://')[-1]

    try:
        requests.get(f'http://{url}', verify=False)
    except ConnectionError:
        return {'status': 'fail',
                'comment': 'url validation fail', 'url': url}

    if slug:
        if slug not in database:
            database.set(slug, url)
        else:
            return {'status': 'fail',
                    'comment': 'slug in database', 'slug': slug}

    else:
        slug = make_slug()
        database.set(slug, url)
    return {'status': 'ok', 'urll': url,
            'short_url': reverse_lazy('home', (slug,), request=request)}


shortener = api_decorator(shortener_universal)


def make_slug():
    slug = ''.join(random.choices(string.ascii_letters, k=5))
    return slug if slug not in database else make_slug()
