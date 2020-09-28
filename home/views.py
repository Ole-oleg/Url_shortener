from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.shortcuts import redirect
import redis
from api.views import shortener_universal

database = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


@require_GET
def go_to(request, slug):
    """ Takes slug and redirects to the connected cite """
    if slug in database:
        url = database.get(slug)
        url.decode()
        return redirect(f'http://{url.decode()}')
    else:
        return HttpResponse('<h>This slug is empty.</h>')


def home_page(request):
    """ just returns home page """
    return HttpResponse(render(request, 'index.html'))


def show_url(request):
    """ returns html page with the shorten link or (if url is empty) just reloads home page """
    if request.GET.get('url', ''):
        data = shortener_universal(request)
        return HttpResponse(render(request, 'shorten.html', data))
    else:
        return redirect('homepage')
