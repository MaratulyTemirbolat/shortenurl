import uuid
from typing import Optional

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
)
from django.core.handlers.wsgi import WSGIRequest

from shortner.models import Url


def index(request: WSGIRequest) -> HttpResponse:  # noqa
    return render(
        request=request,
        template_name='base.html'
    )


def create(request: WSGIRequest) -> HttpResponse:  # noqa
    if request.method == 'POST':
        link: str = request.POST['link']
        uid: str = str(uuid.uuid4())[:7]
        new_url: Url = Url(
            link=link,
            uuid=uid
        )
        new_url.save()
        return HttpResponse(uid)


def go(request: WSGIRequest, uid: str) -> HttpResponseRedirect:  # noqa
    url_details: Optional[Url] = get_object_or_404(Url,
                                                   uuid=uid,
                                                   is_deleted=False)
    return redirect(url_details.link)
